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
    return list(itertools.chain(*pm.hook.installed_apps()))


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
    return pm.hook.urlpatterns()


def settings(current_settings):
    pm.hook.settings(current_settings=current_settings)
