from sqlalchemy.orm import Session
import model, config, schema
from keras import models
import pandas as pd
from pickle import *


settings = config.get_settings()

def getConsumo(db:Session, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO).order_by(model.CONSUMO.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
def getConsumoByPostal(db:Session, codPostal:str, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO).filter(model.CONSUMO.codigo_postal == codPostal).order_by(model.CONSUMO.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
def getConsumoBySector(db:Session, sector:str, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO).filter(model.CONSUMO.sector == sector).order_by(model.CONSUMO.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500

def getUserByEmail(db:Session, email:str):
    try:
        return db.query(model.USER).filter(model.USER.email == email).first()
    except:return settings.ERROR_500
    
def predictLuz(co2:float, gas:float, brent:float):
    data = {'gas':  [gas],
        'co2': [co2],
        'brent': [brent],
        }

    scalerx = load(open("scaler.pkl", 'rb'))  
    scalery = load(open("scalery.pkl", 'rb'))  
  
    n_test = pd.DataFrame(data)
    n_test_x = scalerx.transform(n_test)
    n_test_x = n_test_x.reshape((n_test_x.shape[0], 1, n_test_x.shape[1]))

    model = models.load_model("modelo_luz.h5")
    n_predict=model.predict(n_test_x)

    predict = scalery.inverse_transform(n_predict)

    return {'Precio de la electricidad:': str(predict).replace("[", "").replace("]", "")+" €"}