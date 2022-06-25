# Телефонный справочник

## Docs

1. [Документация по консольному приложению](https://github.com/GeekDevTeam/phone-book/blob/main/docs/console_app.md)
2. [Документация по телеграм боту](https://github.com/GeekDevTeam/phone-book/blob/main/docs/telegram_bot.md)

## Файловая архитектура приложения

```
C:.
│   .gitattributes
│   .gitignore
│   Architecture.drawio.svg
│   LICENSE
│   README.md
│
├───docs # различная документация по приложению
│       console_app.md
│       telegram_bot.md
│
└───src # корень приложения
    │   .env # переменные окружения для приложения
    │   console_app.py # точка входа для консольного приложения
    │   phone-book.db # телефонный справочник
    │   startup.py # основная логика по загрузке конфигураций телеграм бота
    │   telegram_bot.py # точка входа для запуска телеграм бота
    │
    ├───commands # команды для телеграм бота
    │       entry.py # файл для загрузки всех команд в одну зависимость
    │       start_command.py # обработчик команды /start
    │
    ├───configurations # папка с различной конфигурацией телеграм бота
    │       configure.py # функции необходимые для конфигурации телеграм бота
    │       environments.py # словарь с переменными окружения
    │
    ├───core # различные переменные во всем проекте 
    │       format.py # список словарей с форматами хранения данных 
    │
    ├───models # сущности/модели используемые для промежуточного хранения данных 
    │
    ├───private # модули используемые во всем проекте
    │       convert_format.py # модуль конвертирования формата хранения данных из одного в другой
    │       meny.py # моудль для работы с меню приложения
    │       parsing_format.py # модуль для парсинга данных из телефонного справочника
    │
    └───utils # различные независимые модули-помощники, которые не решают бизнес-задачу, а нацелены на конкретное модульное действие
            io_helper.py
```

# Release Notes

1. [Реализация консольного варианта приложения](https://github.com/GeekDevTeam/phone-book/releases/tag/v1.0.0)
2. [Реализация телеграм-бота](https://github.com/GeekDevTeam/phone-book/releases/tag/v1.1.0)
