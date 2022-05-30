from sqlalchemy.orm import Session
from . import model

def getConsumo(db:Session):
    #return db.query(model.CONSUMO).order_by(model.CONSUMO.id).all()
    return "hello"