from .hookspecs import hookimpl
from . import hookspecs
import itertools
from pluggy import PluginManager
from typing import List

pm = PluginManager("djp")
pm.add_hookspecs(hookspecs)
pm.load_setuptools_entrypoints("djp")


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
