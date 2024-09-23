from .hookspecs import hookimpl
from . import hookspecs
import itertools
import os
import pathlib
from pluggy import PluginManager
import sys
from typing import List
import types

pm = PluginManager("djp")
pm.add_hookspecs(hookspecs)
pm.load_setuptools_entrypoints("djp")


def _module_from_path(path, name):
    # Adapted from http://sayspy.blogspot.com/2011/07/how-to-import-module-from-just-file.html
    mod = types.ModuleType(name)
    mod.__file__ = path
    with open(path, "r") as file:
        code = compile(file.read(), path, "exec", dont_inherit=True)
    exec(code, mod.__dict__)
    return mod


plugins_dir = os.environ.get("DJP_PLUGINS_DIR")
if plugins_dir:
    for filepath in pathlib.Path(plugins_dir).glob("*.py"):
        mod = _module_from_path(str(filepath), name=filepath.stem)
        try:
            pm.register(mod)
        except ValueError as ex:
            print(ex, file=sys.stderr)
            # Plugin already registered
            pass


class Before:
    def __init__(self, item: str):
        self.item = item


class After:
    def __init__(self, item: str):
        self.item = item


def installed_apps() -> List[str]:
    return ["djp"] + list(itertools.chain(*pm.hook.installed_apps()))


def middleware(current_middleware: List[str]):
    before = []
    after = []
    default = []

    for batch in pm.hook.middleware():
        for item in batch:
            if isinstance(item, Before):
                before.append(item.item)
            elif isinstance(item, After):
                after.append(item.item)
            elif isinstance(item, str):
                default.append(item)

    combined = before + current_middleware + default + after
    return combined


def urlpatterns():
    return list(itertools.chain(*pm.hook.urlpatterns()))


def settings(current_settings):
    # First wrap INSTALLED_APPS
    installed_apps_ = current_settings["INSTALLED_APPS"]
    if isinstance(installed_apps_, tuple):
        installed_apps_ = list(installed_apps_)
    installed_apps_ += installed_apps()
    current_settings["INSTALLED_APPS"] = installed_apps_

    # Now MIDDLEWARE
    current_settings["MIDDLEWARE"] = middleware(current_settings["MIDDLEWARE"])

    # Now apply any other settings() hooks
    pm.hook.settings(current_settings=current_settings)


def get_plugins():
    plugins = []
    plugin_to_distinfo = dict(pm.list_plugin_distinfo())
    for plugin in pm.get_plugins():
        plugin_info = {
            "name": plugin.__name__,
            "hooks": [h.name for h in pm.get_hookcallers(plugin)],
        }
        distinfo = plugin_to_distinfo.get(plugin)
        if distinfo:
            plugin_info["version"] = distinfo.version
            plugin_info["name"] = (
                getattr(distinfo, "name", None) or distinfo.project_name
            )
        plugins.append(plugin_info)
    return plugins
