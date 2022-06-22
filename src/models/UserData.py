

from typing import TypedDict

class UserData(TypedDict):
    """
    Сущность описывающая данные пользователя.
    """
    surname: str
    name: str
    phone: str
    about_oneself: str

def parse(user_data: list) -> UserData:
    return UserData(
        surname=user_data[0],
        name=user_data[1],
        phone=user_data[2],
        about_oneself=user_data[3]
    )

def to_str(user_data: UserData):
    return f"""
    Фамилия: {user_data['surname']}
    Имя: {user_data['name']}
    Телефон: {user_data['phone']}
    О себе: {user_data['about_oneself']}
    """