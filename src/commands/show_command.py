from telegram import Update
from telegram.ext import ContextTypes
import os
from pathlib import Path
from private.parsing_format import get_all_format_data, parse_all_format_data
from utils.io_helper import read_text_from_file

DB_FULL_FILE_NAME = Path.cwd() / "phone-book.db"

async def show_data(update: Update, context: ContextTypes.context):
    """
    Обработчик команды /show
    """
    format_data = read_text_from_file(DB_FULL_FILE_NAME)
    format_data_parse_res = parse_all_format_data(format_data)
    msg = get_all_format_data(format_data_parse_res)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text = msg)