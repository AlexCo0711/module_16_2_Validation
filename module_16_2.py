# Домашнее задание по теме "Валидация данных".

# импорт библиотеки FastAPI
from fastapi import FastAPI, Path
from typing import Annotated

# Создано приложение(объект) FastAPI
app = FastAPI()


# Создан декоратор маршрута к главной странице
@app.get("/")
async def get_p_main() -> dict:
    return f'Главная страница'


# Создан декоратор маршрута к странице администратора
@app.get("/user/admin")
async def get_p_admin() -> dict:
    return f'Вы вошли как администратор'


# Создан декоратор маршрута к странице пользователя c валидациeй аргумента user_id
@app.get("/user/{user_id}")
async def get_p_user_id(
        user_id:Annotated[int, Path(ge=1,
                                    le=100,
                                    description= 'Введите свой ID',
                                    example='17')]
) -> dict:
    return f'Вы вошли как пользователь №{user_id}'
    

# Создан декоратор маршрута к страницам пользователей c валидациeй аргументов username и age
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
) -> dict:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
