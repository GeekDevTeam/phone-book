from commands.start_command import start_command
from commands.convert_to import convert_to
# Словарь команд телеграм бота
commands = {
    'start': {  # command_name - название команды для телеграм бота
        'command_handler': start_command,  # обработчик команды
        'description': 'Отправляет приветственное сообщение'  # описание команды
    },
    'convert_to': {  # command_name - название команды для телеграм бота
        'command_handler': convert_to,  # обработчик команды
        'description': 'Преобразование формата хранения данных'  # описание команды
    }
}
