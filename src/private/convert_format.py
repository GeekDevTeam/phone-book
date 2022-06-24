from core.format import FORMATS

def convert_format_by_format_id(users: list, format_id: int = 0):
    """
    Конвертирует формат хранения данных в format_id.

    users = [
        ["Фамилия_1", "Имя_1", "Телефон_1", "Описание_1"],
        ["Фамилия_2", "Имя_2", "Телефон_2", "Описание_2"],
        ...
    ]

    format_id - идентификатор формата из списка FORMATS
    """
    user_properties_delimeter = FORMATS[format_id]["userPropertiesDelimeter"]
    user_data_delimeter = FORMATS[format_id]["userDataDelimeter"]
    format_data_delimeter = FORMATS[format_id]["formatDataDelimeter"]
    format_data_str = []

    for properties in users:
        user_data_str = []
        user_data_str.append(user_properties_delimeter +
            f'{user_properties_delimeter * 2}'.join(properties) +
            user_properties_delimeter)
        format_data_str.append(user_data_delimeter +
            f'{user_data_delimeter * 2}'.join(user_data_str) +
            user_data_delimeter)
    format_data = (format_data_delimeter +
        f'{format_data_delimeter * 2}'.join(format_data_str) +
        format_data_delimeter)
    return format_data