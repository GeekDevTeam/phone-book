from commands.start_command import start_command

# Словарь команд телеграм бота 
commands = {
    'start': { # command_name - название команды для телеграм бота
        'command_handler': start_command, # обработчик команды
        'description': 'Отправляет приветственное сообщение' # описание команды
    },
    'show': {'comand_handler': show_command, 'description': 'Сообщает данные пользователя из справочника'}
}