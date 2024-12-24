from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str 
    age: int = None

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def user_registration(user: User,
                            username: Annotated[str, Path(min_length=5,
                                                          max_length=20,
                                                          title='Enter username')],
                            age: Annotated[int, Path(ge=18,
                                                     le=120,
                                                     title='Enter age')]):
    if not users:
        user.id = 1
    else:
        user.id = users[-1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user
        
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(gt=0,
                                                   le=100,
                                                   title='Enter ID')],
                      username: Annotated[str,Path(min_length=5,
                                                   max_length=20,
                                                   title='Enter username')],
                      age: Annotated[int,Path(ge=18,
                                              le=120,
                                              title='Enter age')],
                      user: str = Body()):
    try:
        user_edits = users[user_id - 1] 
        user_edits.username = username
        user_edits.age = age
        return user_edits
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    return HTTPException(status_code=404, detail='User was not found')