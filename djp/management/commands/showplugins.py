from django.core.management.base import BaseCommand
from djp import get_plugins
import json


class Command(BaseCommand):
    help = "Show installed plugins"

    def handle(self, *args, **options):
        plugins = get_plugins()
        print(json.dumps(plugins, indent=2))
