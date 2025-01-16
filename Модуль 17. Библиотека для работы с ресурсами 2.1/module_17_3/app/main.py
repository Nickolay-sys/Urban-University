from fastapi import FastAPI
from routers import task, user

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskamnager"}

app.include_router(task.router)
app.include_router(user.router)