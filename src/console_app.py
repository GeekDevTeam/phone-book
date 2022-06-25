from enum import IntEnum
import os
from pathlib import Path
import models.UserData as UserData
from private.convert_format import convert_format_by_format_id

import private.meny as meny
import core.format as format_core
import utils.io_helper as io_helper
import private.parsing_format as parsing_format
import private.convert_format as convert_format
from private.parsing_format import get_all_format_data, parse_all_format_data, parse_users_from_file

from utils.io_helper import read_text_from_file, write_text_in_file
from utils.list_helper import concate_sub_lst, is_exist_index

clear = lambda: os.system('cls')

DB_FULL_FILE_NAME = Path.cwd() / "phone-book.db"
OUTPUT_FULL_FILE_NAME = DB_FULL_FILE_NAME 
# For debug
#OUTPUT_FULL_FILE_NAME =  Path.cwd() / "phone-book-convert.db"

def select_format_view():
    """
    Представление с выбором нового формата данных
    """
    format_id = -1
    while is_exist_index(format_core.FORMATS, format_id) is False:
        clear()
        print(meny.msg_select_format_view())
        format_id = int(input("Введите пожалуйста format_id желаемого формата из меню: "))
        if is_exist_index(format_core.FORMATS, format_id) is True:
            clear()
            return format_id

        print(meny.msg_unknown_command())
        meny.print_pause()

def startup_view():
    """
    Представление с выбором операции над приложением
    """
    class StartupCommands(IntEnum):
        """
        Перечисление команд из текущего меню.
        """
        EXIT = 0 # Выход
        SHOW_DATA = 1 # Вывод данных по пользователям из БД 
        CONVERT_FORMAT = 2 # Преобразование формата хранения данны
        ADD_NEW_USER = 3 # Добавление нового пользователя

    answer = -1
    while answer != 0:
        clear()
        print(meny.msg_startup())
        answer = int(input())
        clear()
        if answer == StartupCommands.SHOW_DATA:
            format_data = read_text_from_file(DB_FULL_FILE_NAME)
            format_data_parse_res = parse_all_format_data(format_data)
            print(get_all_format_data(format_data_parse_res))
        elif answer == StartupCommands.CONVERT_FORMAT:
            format_id = select_format_view()

            users = parse_users_from_file(DB_FULL_FILE_NAME)
            format_data_convert_res = convert_format_by_format_id(users, format_id)
            
            write_text_in_file(OUTPUT_FULL_FILE_NAME, format_data_convert_res)
            print(meny.msg_success_convert_format(OUTPUT_FULL_FILE_NAME))
        elif answer == StartupCommands.ADD_NEW_USER:
            print(meny.msg_add_new_user_view())
            new_user_data =  UserData.parse(
                input().split(" ")
            )

            users = parse_users_from_file(DB_FULL_FILE_NAME)
            users.append(new_user_data.values())
            format_data_convert_res = convert_format_by_format_id(users)
            
            write_text_in_file(OUTPUT_FULL_FILE_NAME, format_data_convert_res)
            print(meny.msg_add_new_user_success(new_user_data))
        elif answer == StartupCommands.EXIT:
            print(meny.msg_shutdown())
            break
        else:
            print(meny.msg_unknown_command())
        meny.print_pause()
    
def run():
    startup_view()

if __name__ == '__main__':
    run()