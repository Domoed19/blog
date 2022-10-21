from django.core.management.base import BaseCommand

# Почитать про signals отдельно
from domoed.bot import run_bot


class Command(BaseCommand):
    help = "Run BOT"

    def handle(self, *args, **options):
        run_bot()
