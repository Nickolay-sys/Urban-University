from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int 
    username: str 
    age: int 
    
@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length= 5,
                                                 max_length= 20,
                                                 title= 'Enter username')
                                       ],
                   age: Annotated[int, Path(ge= 18,
                                            le= 120,
                                            title= 'Enter age')]) -> User:
    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id= user_id, username= username, age= age)
    users.append(new_user)
    return new_user
    
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(gt= 0,
                                                   le= 100,
                                                   title= 'Enter ID')
                                         ], 
                      username: Annotated[str, Path(min_length= 5,
                                                    max_length= 20,
                                                    title= 'Enter new username')
                                          ], 
                      age: Annotated[int, Path(ge= 18,
                                               le= 120,
                                               title= 'Enter new age')
                                     ]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age 
            return user
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def del_user(user_id: Annotated[int, Path(gt= 0,
                                                le= 100,
                                                title= 'Enter ID for deletion')]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail='User was not found')
