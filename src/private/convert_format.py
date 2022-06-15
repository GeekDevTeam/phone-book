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
       
    formatDataStr = []
    for userData in FormatData:
        for userProperties in userData:
            userDataStr = []
            userDataStr.append(f'{FORMATS[formatId]["userPropertiesDelimeter"]}'.join(userProperties))
            formatDataStr.append(f'{FORMATS[formatId]["userDataDelimeter"]}'.join(userDataStr))
    FormatData=(f'{FORMATS[formatId]["formatDataDelimeter"]}'.join(formatDataStr))
    return FormatData
    
print(convert_format_by_formaId([
    [["Фамилия_1", "Имя_1", "Телефон_1", "Описание_1"], 
    ["Фамилия_2", "Имя_2", "Телефон_2", "Описание_2"], 
    ["Фамилия_3", "Имя_3", "Телефон_3", "Описание_3"]]
    ], 0))