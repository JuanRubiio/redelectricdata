from sqlalchemy.orm import Session
import model, config, schema
#from keras import models, predict

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
    
#def predictLuz(datos:schema.PrediccionElectrica):
 #   model = models.load_model("modelo_luz.h5")