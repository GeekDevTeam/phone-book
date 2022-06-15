FORMATS = [
        { # по-хорошему задать массив через точное определние структуры с помощью классов, но пока я не пробовал классы в питоне
            'formatDataDelimeter': '\n', # разделитель между форматами хранения
            'userDataDelimeter': ';', # разделитель данных пользователей
            'userPropertiesDelimeter': ',',  # разделитель свойств пользователя

            # Пример входного файла с данными:
            # "\n;Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;\n"
        },
        {
            'formatDataDelimeter': '\t',
            'userDataDelimeter': ';',
            'userPropertiesDelimeter': ',',

            # пример входного файла с данными:
            # "   ;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;    "
        },
        {
            'formatDataDelimeter': '%',
            'userDataDelimeter': ';',
            'userPropertiesDelimeter': ',',

            # пример входного файла с данными:
            # "%;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;%"
        }

        # пример входного файла с данными:
        # "\n;Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;\n   ;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;    %;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;%"
    ]

# Добавить метод parse_userProperties_by_delimeter(properties: string, userPropertiesDelimeter: string).
# Метод должен возвращать массив, из данных properties, разделенных с помощью userPropertiesDelimeter
# Входные данные: "Фамилия_1,Имя_1,Телефон_1,Описание_1"
# Выходные данные: ["Фамилия_1", "Имя_1", "Телефон_1", "Описание_1"]

def parse_userProperties_by_delimeter(properties, user_properties_delimeter):
    list_properties = properties.split(user_properties_delimeter)
    return list_properties



#  Добавить метод parse_userData_by_delimeter(usersData: string, userDataDelimeter: string, userPropertiesDelimeter: string).
# Метод должен возвращать массив данных по каждому пользователю
# Входные данные: ";Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;"
# Выходные данные: [ ["Фамилия_1", "Имя_1", "Телефон_1", "Описание_1"], ["Фамилия_2", "Имя_2", "Телефон_2", "Описание_2"] ]
# Алгоритм:
# Разбиваем строку userData с помощью разделителя userDataDelimeter -> получаем массив строк свойств пользователя
# Для каждого элемента массива
# вызываем метод parse_userProperties_by_delimeter
# Полученный результат добавляем в массив parsed_usersData
# Возвращаем сформировавшийся массив parsed_usersData

def parse_userData_by_delimeter(users_data, user_data_delimeter, user_properties_delimeter):
    parsed_users_data = []
    list_properties = users_data.split(user_data_delimeter)
    for data in list_properties:
        parsed_users_data.append(parse_userProperties_by_delimeter(data, user_properties_delimeter))
    return parsed_users_data


#  Добавить метод parse_formatData_by_delimeter(formatData: string, formatId: int), formatId - индекс формата из массива
#  FORMATS
# Метод должен возвращать массив, из данных formatData, разделенных с помощью FORMATS[formatId][formatDataDelimeter]
# Входные данные: "\n;Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;\n"
# Выходные данные:
# [
#     [ ["Фамилия_1", "Имя_1", "Телефон_1", "Описание_1"], ["Фамилия_2", "Имя_2", "Телефон_2", "Описание_2"] ]
# ]
# Алгоритм:
# Разбиваем строку formatData с помощью разделителя formatDataDelimeter -> получаем массив строк одного формата хранения
# Для каждого элемента массива
# вызываем метод parse_userData_by_delimeter
# Полученный результат добавляем в массив parsed_formatData
# Возвращаем сформировавшийся массив parsed_formatData

def parse_formatData_by_delimeter(format_data, format_id):
    temp_list = format_data.split(FORMATS[format_id]['formatDataDelimeter'])
    for data in temp_list:
        parsed_formatData = list(map(parse_userData_by_delimeter, data, FORMATS[format_id]['userDataDelimeter'], FORMATS[format_id]['userPropertiesDelimeter'] ))
    return parsed_formatData


temp = '\n;Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;\n'


print(parse_formatData_by_delimeter(temp, 0))