# Домашнее задание по теме "Валидация данных".

# импорт библиотеки FastAPI
from fastapi import FastAPI, Path
from typing import Annotated

# Создано приложение(объект) FastAPI
app = FastAPI()


# Создан декоратор маршрута к главной странице на выходе строка
@app.get("/")
async def get_p_main() -> str:
    return f'Главная страница'


# Создан декоратор маршрута к странице администратора на выходе строка
@app.get("/user/admin")
async def get_p_admin() -> str:
    return f'Вы вошли как администратор'


# Создан декоратор маршрута к странице пользователя c валидациeй аргумента user_id на выходе строка
@app.get("/user/{user_id}")
async def get_p_user_id(
        user_id:Annotated[int, Path(ge=1,
                                    le=100,
                                    description= 'Введите свой ID',
                                    example='17')]
) -> str:
    return f'Вы вошли как пользователь №{user_id}'
    

# Создан декоратор маршрута к страницам пользователей c валидациeй аргументов username и age на выходе строка
@app.get("/user/{username}/{age}")
async def get_p_data_user(
        username:Annotated[str, Path(min_length=5,
                                     max_length=20,
                                     description='Введите свое имя',
                                     example='Vasiliy')],
        age:Annotated[int, Path(ge=18,
                                le=120,
                                description='Введите свой возраст',
                                example='21')]
) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
