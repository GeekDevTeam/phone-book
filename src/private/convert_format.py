from core.format import FORMATS


def convert_format_by_format_id(format_data, format_id: int):

    format_data_str = []
    for user_data in format_data:
        for user_properties in user_data:
            user_data_str = []
            user_data_str.append(
                f'{FORMATS[format_id]["user_properties_delimeter"]}'.join(user_properties))
            format_data_str.append(
                f'{FORMATS[format_id]["user_data_delimeter"]}'.join(user_data_str))
    format_data = (
        f'{FORMATS[format_id]["format_data_delimeter"]}'.join(format_data_str))
    return format_data
