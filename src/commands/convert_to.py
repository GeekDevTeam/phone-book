from telegram import Update
from telegram.ext import ContextTypes
import os
from pathlib import Path
from private.parsing_format import parse_all_format_data
from private.convert_format import convert_format_by_format_id
from utils.io_helper import read_text_from_file
from utils.io_helper import write_text_in_file
from utils.list_helper import concate_sub_lst
from private.meny import print_converting_format, print_wrong_converting_command


def read_text_from_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data


DB_FULL_FILE_NAME = Path.cwd() / "phone-book.db"
OUTPUT_FULL_FILE_NAME = Path.cwd() / "phone-book-convert.db"


async def convert_to(update: Update, context: ContextTypes.context):
    """
    Обработчик команды /convert_to
    """

    msg = update.message.text
    print(msg)
    items = msg.split()

    format_id = int(items[1])
    print(format_id)
    if format_id > 2 or format_id < 0:
        msg = print_wrong_converting_command(update.message.text)
        await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg)
    else:
        format_data = read_text_from_file(DB_FULL_FILE_NAME)
        format_data_parse_res = parse_all_format_data(format_data)
        any_formats_users = concate_sub_lst(format_data_parse_res)
        users = concate_sub_lst(any_formats_users)
        format_data_convert_res = convert_format_by_format_id(users, format_id)
        write_text_in_file(OUTPUT_FULL_FILE_NAME, format_data_convert_res)
        msg = print_converting_format(format_data_convert_res, OUTPUT_FULL_FILE_NAME)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg)
    
