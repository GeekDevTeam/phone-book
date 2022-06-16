


def parse_userProperties_by_delimeter(properties, user_properties_delimeter):
        '''
        Возвращает массив, из данных properties, разделенных с помощью userPropertiesDelimeter
        '''
    list_properties = properties.split(user_properties_delimeter)
    return list_properties
 

def parse_userData_by_delimeter(users_data, user_data_delimeter, user_properties_delimeter):
        '''
        Возвращает массив данных parsed_users_data, разеленный user_data_delimeter на подмасивы данных о пользователе, которые разделены user_properties_delimeter
        '''
    parsed_users_data = []
    list_properties = users_data.split(user_data_delimeter)
    for data in list_properties:
        parsed_users_data.append(parse_userProperties_by_delimeter(data, user_properties_delimeter))
    return parsed_users_data


def parse_formatData_by_delimeter(format_data, format_id):
        '''
        Возвращает массив, из данных formatData, разделенных с помощью FORMATS[formatId][formatDataDelimeter]
        '''
    temp_list = format_data.split(FORMATS[format_id]['formatDataDelimeter'])
    for data in temp_list:
        parsed_formatData = list(map(parse_userData_by_delimeter, data, FORMATS[format_id]['userDataDelimeter'], FORMATS[format_id]['userPropertiesDelimeter'] ))
    return parsed_formatData
