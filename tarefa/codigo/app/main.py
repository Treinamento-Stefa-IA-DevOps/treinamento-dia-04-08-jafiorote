import pickle
import pandas as pd
from fastapi import FastAPI, Response


app = FastAPI()
@app.post('/model')

def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

    x_test = pd.DataFrame({'Sex': [Sex], 'Age': [Age], 'Lifeboat': [Lifeboat], 'Pclass': [Pclass]})
    y = titanic.predict(x_test)[0]

    msg_True = "Viveu!"
    msg_False = "Morreu!"
    life_status = True if y else False
    message = msg_True if y else msg_False


    return {"survived": life_status, "status": 200, "message": message}

@app.get('/model')
def get():
    return {'hello':'test'}
