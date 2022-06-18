import os
from pathlib import Path

import meny
import core.format as format_core
import utils.io_helper as io_helper
import private.parsing_format as parsing_format
import private.convert_format as convert_format

clear = lambda: os.system('cls')

DB_FULL_FILE_NAME = Path.cwd() / "phone-book.db"
OUTPUT_FULL_FILE_NAME = Path.cwd() / "phone-book-convert.db"

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

def is_exist_index(lst, index):
    """
    Проверяет наличие индекса в списке
    """
    return index >= 0 and index < len(lst)

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
            format_data = io_helper.read_text_from_file(DB_FULL_FILE_NAME)
            format_data_parse_res = parsing_format.parse_all_format_data(format_data)
            parsing_format.print_all_format_data(format_data_parse_res)
        elif answer == 2:
            format_id = select_format_view()

            format_data = io_helper.read_text_from_file(DB_FULL_FILE_NAME)
            format_data_parse_res = parsing_format.parse_all_format_data(format_data)
            any_formats_users = concate_sub_lst(format_data_parse_res)
            users = concate_sub_lst(any_formats_users)
            format_data_convert_res = convert_format.convert_format_by_format_id(users, format_id)
            
            io_helper.write_text_in_file(OUTPUT_FULL_FILE_NAME, format_data_convert_res)
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