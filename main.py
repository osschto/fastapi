from fastapi import FastAPI
from pydantic import BaseModel
import hashlib, json

data = {}

app = FastAPI()

class Log_Pas(BaseModel):
    log : str
    pas : str

@app.post("/register/")
async def get_log_pas(log_pas : Log_Pas):

    hash_password = hashlib.sha256(log_pas.pas.encode()).hexdigest()
    data[log_pas.log] = hash_password

    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

    return log_pas