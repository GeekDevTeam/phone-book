import os
import logging
import configurations.environments as env
from dotenv import load_dotenv
from pathlib import Path
from telegram.ext import ApplicationBuilder, CommandHandler, Application

def add_env():
    '''
    Добавляет в приложении переменные окружения
    '''
    dotenv_path = Path.cwd() / '.env'
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    for env_name in env.items:
        if not os.getenv(env.items[env_name]):
            raise Exception(f'Environment variable {env_name} is not defined')
        env.items[env_name] = os.getenv(env.items[env_name])

def add_logging():
    '''
    Добавляет настройки логирования
    '''
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def add_commands(application: Application):
    '''
    Добавляет команды для телеграм бота
    '''
    from commands.entry import commands

    for command_name in commands:
        application.add_handler(
            CommandHandler(command_name, commands[command_name]['command_handler'])
        )


def add_telegram_bot():
    '''
    Добавляет телеграм-бота
    '''
    application = ApplicationBuilder().token(env.items['telegram_bot_token']).build()
    add_commands(application)
    application.run_polling()