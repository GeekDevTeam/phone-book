import os
from pathlib import Path
from private.convert_format import convert_format_by_format_id

import private.meny as meny
import core.format as format_core
from private.parsing_format import get_all_format_data, parse_all_format_data

from utils.io_helper import read_text_from_file, write_text_in_file
from utils.list_helper import concate_sub_lst, is_exist_index

clear = lambda: os.system('cls')

DB_FULL_FILE_NAME = Path.cwd() / "phone-book.db"
OUTPUT_FULL_FILE_NAME = Path.cwd() / "phone-book-convert.db"

def select_format_view():
    """
    Представление с выбором нового формата данных
    """
    format_id = -1
    while is_exist_index(format_core.FORMATS, format_id) is False:
        clear()
        meny.print_select_format_view()
        format_id = int(input("Введите пожалуйста format_id желаемого формата из меню: "))
        if is_exist_index(format_core.FORMATS, format_id) is True:
            clear()
            return format_id

        meny.print_unknown_command()
        meny.print_pause()

def startup_view():
    """
    Представление с выбором операции над приложением
    """
    answer = -1
    while answer != 0:
        clear()
        meny.print_startup()
        answer = int(input())
        clear()
        if answer == 1:
            format_data = read_text_from_file(DB_FULL_FILE_NAME)
            format_data_parse_res = parse_all_format_data(format_data)
            print(get_all_format_data(format_data_parse_res))
        elif answer == 2:
            format_id = select_format_view()

            format_data = read_text_from_file(DB_FULL_FILE_NAME)
            format_data_parse_res = parse_all_format_data(format_data)
            any_formats_users = concate_sub_lst(format_data_parse_res)
            users = concate_sub_lst(any_formats_users)
            format_data_convert_res = convert_format_by_format_id(users, format_id)
            
            write_text_in_file(OUTPUT_FULL_FILE_NAME, format_data_convert_res)
            meny.print_success_convert_format(OUTPUT_FULL_FILE_NAME)
        elif answer == 0:
            meny.print_shutdown()
            break
        else:
            meny.print_unknown_command()
        meny.print_pause()
    
def run():
    startup_view()

if __name__ == '__main__':
    run()