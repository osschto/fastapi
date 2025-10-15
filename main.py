from fastapi import FastAPI
from pydantic import BaseModel
import hashlib, json

app = FastAPI()

data = {}

class LogPas(BaseModel):
    log : str
    pas : str

@app.post("/register/", tags=["Регистрация"], summary="Получение логина и пароля")
async def get_log_pas(log_pas : LogPas):

    hash_password = hashlib.sha256(log_pas.pas.encode()).hexdigest()
    data[log_pas.log] = hash_password

    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

    return ...