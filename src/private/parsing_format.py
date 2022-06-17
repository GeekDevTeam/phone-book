from src.core.format import FORMATS

def parse_user_properties_by_delimeter(properties, user_properties_delimeter):
    list_properties = properties.split(user_properties_delimeter)
    return list_properties
 

def parse_user_data_by_delimeter(users_data, user_data_delimeter, user_properties_delimeter):
    parsed_users_data = []
    list_properties = users_data.split(user_data_delimeter)
    for data in list_properties:
        parsed_users_data.append(parse_user_properties_by_delimeter(data, user_properties_delimeter))
    return parsed_users_data


def parse_format_data_by_delimeter(format_data, format_id):
    '''
    разделяет массив format_data по разделителям formatDataDelimeter и далее полученные 
    массивы разделяет по userDataDelimeter и userPropertiesDelimeter
    '''
    temp_list = format_data.split(FORMATS[format_id]['formatDataDelimeter'])
    parsed_format_data = []
    for data in temp_list:
        parsed_format_data.append(parse_user_data_by_delimeter(data, FORMATS[format_id]['userDataDelimeter'], FORMATS[format_id]['userPropertiesDelimeter']))
    return parsed_format_data