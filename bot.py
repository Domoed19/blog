import os
from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.effective_chat.id)
    await update.message.reply_text(f"Start {update.effective_user.first_name}")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Message {update.effective_user.first_name}")


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(~filters.COMMAND, message))
    app.run_polling()
