from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1' : 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def user_registration(username: Annotated[str, Path(min_length=5,
                                                          max_length=20,
                                                          title='Enter username')],
                            age: Annotated[int, Path(ge=18,
                                                     le=120,
                                                     title='Enter age')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(gt=0,
                                                   le=100,
                                                   title='Enter ID')],
                      username: Annotated[str,Path(min_length=5,
                                                   max_length=20,
                                                   title='Enter username')],
                      age: Annotated[int,Path(ge=18,
                                              le=120,
                                              title='Enter age')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id) -> str:
    del users[user_id]
    return f'The user {user_id} has been deleted'