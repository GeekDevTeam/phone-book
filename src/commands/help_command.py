from telegram import Update
from telegram.ext import ContextTypes

import private.meny as meny

async def help_command(update: Update, context: ContextTypes.context):
    """
    Обработчик команды /help
    """
    reply_text = meny.msg_all_commands()
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=reply_text)
