FORMATS = [
    {"formatDataDelimeter": "\n","userDataDelimeter": ";","userPropertiesDelimeter": ","},
    {"formatDataDelimeter": '\t',"userDataDelimeter": "_;_","userPropertiesDelimeter": ","},
    {"formatDataDelimeter": "%","userDataDelimeter": "__","userPropertiesDelimeter": "," }
    ]

def convert_format_by_formaId(FormatData, formatId: int):
  
    FormatData = [
        [["Фамилия_1", "Имя_1", "Телефон_1", "Описание_1"], 
        ["Фамилия_2", "Имя_2", "Телефон_2", "Описание_2"], 
        ["Фамилия_3", "Имя_3", "Телефон_3", "Описание_3"]]
        ]
       
    format_data_str = []
    for user_data in format_data:
        for user_properties in user_data:
            user_data_str = []
            user_data_str.append(f'{FORMATS[format_id]["user_properties_delimeter"]}'.join(user_properties))
            format_data_str.append(f'{FORMATS[format_id]["user_data_delimeter"]}'.join(user_data_str))
    converted_format_data=(f'{FORMATS[format_id]["format_data_delimeter"]}'.join(format_data_str))
    return converted_format_data
    
print(convert_format_by_formaId([
    [["Фамилия_1", "Имя_1", "Телефон_1", "Описание_1"], 
    ["Фамилия_2", "Имя_2", "Телефон_2", "Описание_2"], 
    ["Фамилия_3", "Имя_3", "Телефон_3", "Описание_3"]]
    ], 0))