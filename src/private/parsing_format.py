from ast import pattern
import re

from core.format import FORMATS
import models.UserData as UserData
from utils.io_helper import read_text_from_file
from utils.list_helper import concate_sub_lst

# Парсит данные между двумя разделителями
def parse_all_data_between_delimeter(data: str, delimeter_start: str, delimeter_end: str):
    if data == '':
        return []

    res = re.findall(delimeter_start + '(.*?)' + delimeter_end, data, re.DOTALL)
    if res is None:
        return []
    
    return res

# Парсит свойства пользователя между разделителем user_properties_delimeter
def parse_user_properties_by_delimeter(properties: str, user_properties_delimeter: str):
    return parse_all_data_between_delimeter(properties, user_properties_delimeter, user_properties_delimeter)
 
# Парсит данные пользователей между разделителем user_data_delimeter
def parse_user_data_by_delimeter(users_data, user_data_delimeter, user_properties_delimeter):
    parsed_users_data = []
    parsed_users = parse_all_data_between_delimeter(users_data, user_data_delimeter, user_data_delimeter)
    for user in parsed_users:
        parsed_users_data.append(parse_user_properties_by_delimeter(user, user_properties_delimeter))
    return parsed_users_data


def parse_format_data_by_delimeter(format_data: str, format_id: int):
    parsed_format_data = []
    formatDataDelimeter = FORMATS[format_id]['formatDataDelimeter']
    tmp_parsed_format_data = parse_all_data_between_delimeter(format_data, formatDataDelimeter, formatDataDelimeter)
    for data in tmp_parsed_format_data:
        parsed_format_data.append(parse_user_data_by_delimeter(data, FORMATS[format_id]['userDataDelimeter'], FORMATS[format_id]['userPropertiesDelimeter']))
    return parsed_format_data

def parse_all_format_data(format_data: str):
    parsed_format_data = []
    for format_id in range(len(FORMATS)):
        parsed_format_data.append(parse_format_data_by_delimeter(format_data, format_id))
    return parsed_format_data

def get_all_format_data(parsed_format_data: list) -> str:
    """
    Возвращает данные с телефонного справочника в виде:
    Format={format_id}) formatDataDelimeter='0', userDataDelimeter=';', userPropertiesDelimeter=','
    UserId=0)
        Фамилия: Иванов
        Имя: Иван
        Телефон: 88005553535
        О себе: Я такой весь хороший
    """
    output: str = ''

    for format_id in range(len(FORMATS)):
        formatDataDelimeter = FORMATS[format_id]['formatDataDelimeter']
        userDataDelimeter = FORMATS[format_id]['userDataDelimeter']
        userPropertiesDelimeter = FORMATS[format_id]['userPropertiesDelimeter']

        output +=f'Format={format_id}) formatDataDelimeter=\'{formatDataDelimeter}\', userDataDelimeter=\'{userDataDelimeter}\', userPropertiesDelimeter=\'{userPropertiesDelimeter}\''
        for users in parsed_format_data[format_id]:
            for i in range(len(users)):
                output += f'\nUserId={i})'
                user_data = users[i]
                user_data_dict = UserData.parse(user_data)
                user_data_str = UserData.to_str(user_data_dict)
                output += f'{user_data_str}\n'
    return output

def parse_users_from_file(file_name: str) -> list:
    """
    Парсит список с данными пользователей из файла и возвращает его.
    """
    format_data = read_text_from_file(file_name)
    format_data_parse_res = parse_all_format_data(format_data)
    any_formats_users = concate_sub_lst(format_data_parse_res)
    users = concate_sub_lst(any_formats_users)
    return users