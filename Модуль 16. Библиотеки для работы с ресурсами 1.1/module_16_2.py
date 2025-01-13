from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def read_root() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def read_adim() -> str:
    return "Вы вошли как администратор"

@app.get('/user/{user_id}')
async def read_user_id(user_id: Annotated[int, Path(gt=0,
                                                    le=100,
                                                    title='Enter User ID',
                                                    examples='1')
                                          ]
                       ) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user/{username}/{age}')
async def read_user(username: Annotated[str, 
                                        Path(min_length=5,
                                             max_length= 20,
                                             title='Enter username',
                                             examples='Nikolay') 
                                        ], 
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             title="Enter age",
                                             examples='26')
                                   ]
                    ) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'