from os import access
from fastapi import APIRouter, Depends, HTTPException
import crud 
import database
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decodeJWT, signJWT
from fastapi import status

api_router = APIRouter()


@api_router.get("/hello/", status_code = status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    return 'HELLO'

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

