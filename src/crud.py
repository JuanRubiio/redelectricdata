from sqlalchemy.orm import Session
import model

def getConsumo(db:Session):
    return db.query(model.CONSUMO).order_by(model.CONSUMO.consumo_id).all()