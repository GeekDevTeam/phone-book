from telegram import Update
from telegram.ext import ContextTypes
import os
from pathlib import Path
import utils.io_helper as io_helper
from private.parsing_format import parse_all_format_data
from private.convert_format import convert_format_by_format_id
from core.format import FORMATS


def concate_sub_lst(lst):
    """
    Понижает уровень хранения данных на 1 объединяя данные на одном уровне.
    Пример: [[1,2], [3,4]] => [1,2,3,4]
    """
    res = []
    for sub_lst in lst:
        for item in sub_lst:
            res.append(item)
    return res


def read_text_from_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data


def write_text_in_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)


def print_unknown_command():
    print("Неизвестная команда.")


def print_success_convert_format(output_full_file_name):
    print(f"""
Преобразование формата хранения данных прошло успешно.
Файл был сохранен по адресу:{output_full_file_name}
    """)


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
        msg= (f'Неизвестная команда.\n {update.message.text}')
        await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg)
    else:
        format_data = read_text_from_file(DB_FULL_FILE_NAME)
        format_data_parse_res = parse_all_format_data(format_data)
        any_formats_users = concate_sub_lst(format_data_parse_res)
        users = concate_sub_lst(any_formats_users)
        format_data_convert_res = convert_format_by_format_id(users, format_id)
        io_helper.write_text_in_file(
        OUTPUT_FULL_FILE_NAME, format_data_convert_res)
    msg = (
        f'Преобразование формата хранения данных: \n {format_data_convert_res} \n Преобразование формата хранения данных прошло успешно.\n Файл был сохранен по адресу:{OUTPUT_FULL_FILE_NAME}')

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=msg)
    
