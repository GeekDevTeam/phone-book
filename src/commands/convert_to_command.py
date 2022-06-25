from telegram import Update
from telegram.ext import ContextTypes

from pathlib import Path

import configurations.environments as env

import core.format as format_core

from private.parsing_format import parse_all_format_data
from private.convert_format import convert_format_by_format_id
import private.meny as meny

from utils.io_helper import read_text_from_file
from utils.io_helper import write_text_in_file
from utils.list_helper import concate_sub_lst, is_exist_index


async def convert_to_command(update: Update, context: ContextTypes.context):
    """
    Обработчик команды /convert_to
    """

    msg = update.message.text
    if msg: # Если сообщение не пустое
        items = msg.split()
        if (len(items) > 1 and # Если имеется параметр для команды
            items[1].isnumeric() and # Если параметр для команды явл. числом
            is_exist_index(format_core.FORMATS, int(items[1]))): # Если параметр - является существующим форматом
                format_id = int(items[1])
                DB_FULL_FILE_NAME = Path.cwd() / env.items['db_file_name']
                OUTPUT_FULL_FILE_NAME = DB_FULL_FILE_NAME

                format_data = read_text_from_file(DB_FULL_FILE_NAME)
                format_data_parse_res = parse_all_format_data(format_data)
                any_formats_users = concate_sub_lst(format_data_parse_res)
                users = concate_sub_lst(any_formats_users)
                format_data_convert_res = convert_format_by_format_id(users, format_id)
                write_text_in_file(OUTPUT_FULL_FILE_NAME, format_data_convert_res)
                msg = meny.msg_converting_format(format_data_convert_res, OUTPUT_FULL_FILE_NAME)
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=msg
                )
                return

    # Если из функции не вышли -> произошла ошибка
    msg = meny.msg_wrong_converting_command(update.message.text)
    await context.bot.send_message(
    chat_id=update.effective_chat.id,
    text=msg)
    
