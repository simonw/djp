from django.core.management.base import BaseCommand
from djp import pm
import json


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


class Command(BaseCommand):
    help = "Show installed plugins"

    def handle(self, *args, **options):
        plugins = get_plugins()
        print(json.dumps(plugins, indent=2))
