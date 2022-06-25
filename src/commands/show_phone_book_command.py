from telegram import Update
from telegram.ext import ContextTypes
from pathlib import Path
from private.parsing_format import get_all_format_data, parse_all_format_data
from utils.io_helper import read_text_from_file

import configurations.environments as env


async def show_phone_book_command(update: Update, context: ContextTypes.context):
    """
    Обработчик команды /show
    """
    DB_FULL_FILE_NAME = Path.cwd() / env.items['db_file_name']
    format_data = read_text_from_file(DB_FULL_FILE_NAME)
    format_data_parse_res = parse_all_format_data(format_data)
    msg = get_all_format_data(format_data_parse_res)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text = msg)