from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.context):
    """
    Обработчик команды /start
    """
    #msg = update.message.text - для получения сообщения от пользователя
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Добро пожаловать в 'Телефонный справочник'")
