from fastapi import FastAPI
from pydantic import BaseModel
import hashlib, json

app = FastAPI()

data = {}

class Reg(BaseModel):
    log : str
    pas : str

class Log(BaseModel):
    log : str
    pas : str

@app.post("/register/", tags=["Регистрация"], summary="Регистрация")
async def get_log_pas(reg : Reg):
    hash_reg_password = hashlib.sha256(reg.pas.encode()).hexdigest()
    data[reg.log] = hash_reg_password

    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)

@app.post("/authorize/", tags=["Авторизация"], summary="Вход")
async def auth(log : Log):
    with open("users.json", "r") as f:
        data = json.load(f)
    
    if log.log in data:
        hash_log_password = hashlib.sha256(log.pas.encode()).hexdigest()
        if hash_log_password == data[log.log]:
            return {"msg" : "Успешный вход"}
        else:
            return {"msg" : "Неверный пароль"}
    else:
        return {"msg" : "Пользователь не найден"}