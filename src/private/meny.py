from core.format import FORMATS
import models.UserData as UserDataModule

def msg_startup():
    return """
Приложение "Телефонный справочник:"
    
МЕНЮ
1. Вывод данных по пользователям из БД 
2. Преобразование формата хранения данных 
3. Добавление нового пользователя
0. Выйти из приложения
    
Введите пожалуйста номер желаемого действия из меню: 
    """

def msg_shutdown():
    return """
Спасибо что воспользовались нашим приложением!
    """

def msg_unhandle_error():
    return """
Что-то пошло не так с приложением :'(
Пожалуйста перезапустите его
    """


def msg_unknown_command():
    return "Неизвестная команда."


def msg_wrong_converting_command(msg):
    return(f"""Неверная команда. Введите вариант конвертации от 0 до 2: \n {msg}""")


def msg_converting_format(format_data_convert_res, OUTPUT_FULL_FILE_NAME):
    return(f"""
Преобразование формата хранения данных:\n \n {format_data_convert_res} \n 
Преобразование формата хранения данных прошло успешно.
Файл был сохранен по адресу:{OUTPUT_FULL_FILE_NAME}
    """)


def msg_success_convert_format(output_full_file_name):
    return f"""
Преобразование формата хранения данных прошло успешно.
Файл был сохранен по адресу:{output_full_file_name}
    """


def msg_select_format_view():
    msg = f"""
Приложение "Телефонный справочник:"
    
МЕНЮ
"""
    for format_id in range(len(FORMATS)):
        formatDataDelimeter = FORMATS[format_id]['formatDataDelimeter']
        userDataDelimeter = FORMATS[format_id]['userDataDelimeter']
        userPropertiesDelimeter = FORMATS[format_id]['userPropertiesDelimeter']
        example = FORMATS[format_id]['example']
        msg += f'\nformat_id={format_id}) formatDataDelimeter=\'{formatDataDelimeter}\', userDataDelimeter=\'{userDataDelimeter}\', userPropertiesDelimeter=\'{userPropertiesDelimeter}\', example=\'{example}\''
    msg +="\n"

    return msg


def print_pause():
    input("Для продолжения нажмите Enter")


def msg_add_new_user_view():
    user_properties = map(
        lambda prop: f'[{prop}]', UserDataModule.UserData.__annotations__.keys())
    user_properties_str = ' '.join(user_properties)
    return f"""
Укажите данные пользователя в формате: '{user_properties_str}'

    """


def msg_add_new_user_success(user_data: UserDataModule.UserData):
    return f"""
Пользователь с данными
{UserDataModule.to_str(user_data)}
Успешно добавлен в БД!
    """

def msg_all_commands():
    from commands.entry import commands
    
    msg = ""
    command_names = commands.keys()
    for command_name in command_names:
        desc = commands[command_name]['description']
        msg += f"/{command_name} - {desc}\n"
    return msg