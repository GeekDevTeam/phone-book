# Метод считывает и возвращает считанные данные с файла file_name
def read_text_from_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

# Метод позволяет записать текст в файл
def write_text_in_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)