import asyncio

from django.conf import settings
from django.core.management.base import BaseCommand

from domoed.services import send_message

from domoed.bot import run_bot


class Command(BaseCommand):
    help = "Run telegram bot"

    def handle(self, *args, **options):
        asyncio.run(send_message(chat_id=settings.CHAT_ID, text="Test notification"))
