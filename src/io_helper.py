# Метод read_text_from_file(file_name) считывает данные с файла, закрывает его и возвращает считанные данные

def read_text_from_file(file_name):
    data = open(file_name)
    text_from_file = data.read()
    data.close
    return text_from_file
    
# Метод write_text_in_file(file_name, text) открывает файл, записывает текст и закрывает его

def write_text_in_file(file_name, text):
    data = open(file_name, 'a')
    data.writelines('\n' + text)
    data.close