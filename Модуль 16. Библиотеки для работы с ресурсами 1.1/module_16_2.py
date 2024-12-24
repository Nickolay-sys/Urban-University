from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def read_root() -> dict:
    return {'message':'Главная страница'}

@app.get('/user/admin')
async def read_adim() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def read_user_id(user_id: Annotated[int, Path(gt=0,
                                                    le=100,
                                                    title='Enter User ID')]
                       ) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get('/user/{username}/{age}')
async def read_user(username: Annotated[str, 
                                        Path(min_length=5,
                                             max_length= 20,
                                             title='Enter username') 
                                        ], 
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             title="Enter age")]
                    ) -> dict:
    return {"message": f'Информация о пользователе. Имя: {username}, Возраст: {age}'}