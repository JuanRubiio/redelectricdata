from os import access
from fastapi import APIRouter, Depends, HTTPException
from .crud import crud
from .database import database
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decodeJWT, signJWT

api_router = APIRouter()

@api_router.get("/token", tags=["dev"])
async def getToken() -> dict:
    access_token = signJWT("juanignaciojimenezgutierrez@gmail.com")
    return access_token

@api_router.get("/consumo", tags=["consumo"])
def getConsumo() -> dict:
    with database.getSession() as db:
        consumo = crud.getConsumo(db)
        if consumo: return consumo
        else: raise HTTPException(status_code=404, detail="Not consumo")

