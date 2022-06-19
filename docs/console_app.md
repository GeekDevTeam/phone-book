# Архитектура консольного приложения "console_app.py"

![Architecture](Architecture.drawio.svg#center)

# Задание
    Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. Смысл - такой же, как на семинаре: сначала продумать архитектуру приложения, разбить задачу на отдельные модули и каждый модуль пишет отдельный человек (можно взять на себя и два, если количество модулей превышает количество человек).

    Под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель*

    *Фамилия_1*

    *Имя_1*

    *Телефон_1*

    *Описание_1*

    *Фамилия_2*

    *Имя_2*

    *Телефон_2*

    *Описание_2*

    *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***

    *Фамилия_1,Имя_1,Телефон_1,Описание_1*

    *Фамилия_2,Имя_2,Телефон_2,Описание_2*

    *и т.д.*

## Getting start

1. Открываем через консоль папку `/src` с содержимым `console_app.py`
2. Запускаем приложение с помощью команды `python console_app.py` 

## Описание модулей
| Модуль                                                                                                   | Описание                                              | Автор        | Task                                               |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------|--------------|----------------------------------------------------|
| [parsing_format.py](https://github.com/GeekDevTeam/phone-book/tree/master/src/private/parsing_format.py) | модуль для парсинга данных заданных в разных форматах | [Никита Савин](https://github.com/SavinNik89) | https://github.com/GeekDevTeam/phone-book/issues/1 |
| [io_helper.py](https://github.com/GeekDevTeam/phone-book/tree/master/src/utils/io_helper.py)             | модуль помощник при работе с файлами                  | [Ксения](https://github.com/xenia-t)       | https://github.com/GeekDevTeam/phone-book/issues/2 |
| [convert_format.py](https://github.com/GeekDevTeam/phone-book/tree/master/src/private/convert_format.py) | модуль конвертации формата хранения данных            | [Алексей](https://github.com/Alexey-Kokushkin)      | https://github.com/GeekDevTeam/phone-book/issues/3 |
| [meny.py](https://github.com/GeekDevTeam/phone-book/tree/master/src/apps/meny.py)                             | модуль для работы с менюшкой приложения               | [Руслан](https://github.com/Ruslan-Botyrov)       | https://github.com/GeekDevTeam/phone-book/issues/4 |
| [main.py](https://github.com/GeekDevTeam/phone-book/tree/master/src/apps/main.py)                             | точка входа программы с основной бизнес-логикой       | [Адиль](https://github.com/AdilBikeev)        | https://github.com/GeekDevTeam/phone-book/issues/5 |

