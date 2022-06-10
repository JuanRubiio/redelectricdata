from os import access
from fastapi import APIRouter, Depends, HTTPException
import crud, database, schema
from auth.auth_bearer import JWTBearer
from auth.auth_handler import decodeJWT, signJWT
from fastapi import status

api_router = APIRouter()


@api_router.get("/token", tags=["dev"])
async def getToken(email:str) -> dict:
    with database.getSession() as db:
        user_email = crud.getUserByEmail(db, email)
        if user_email:
            access_token = signJWT(email)
            return access_token
        else: raise  HTTPException(status_code=401, detail="Invalid user email")

@api_router.get("/consumo", tags=["consumo"], dependencies=[Depends(JWTBearer())])
def getConsumo(skip:int, limit:int, accese_token:str = Depends(JWTBearer())) -> dict:
    with database.getSession() as db:
        consumo = crud.getConsumo(db, skip, limit)
        if consumo: return consumo
        else: raise HTTPException(status_code=404, detail="Not consumo")


@api_router.get("/consumoByPostal", tags=["consumo"], dependencies=[Depends(JWTBearer())])
def getConsumoByPostal(codPostal:str, skip:int, limit:int, accese_token:str = Depends(JWTBearer())) -> dict:
    with database.getSession() as db:
        consumo = crud.getConsumoByPostal(db, codPostal, skip, limit)
        if consumo: return consumo
        else: raise HTTPException(status_code=404, detail="Not consumo")

@api_router.get("/consumoBySector", tags=["consumo"], dependencies=[Depends(JWTBearer())])
def getConsumoBySector(sector:str, skip:int, limit:int, accese_token:str = Depends(JWTBearer())) -> dict:
    with database.getSession() as db:
        consumo = crud.getConsumoBySector(db, sector, skip, limit)
        if consumo: return consumo
        else: raise HTTPException(status_code=404, detail="Not consumo")

@api_router.get("/prediccionElectrica", tags=["electricidad"], dependencies=[Depends(JWTBearer())])
def getPrediccionElectrica(co2:float, gas:float, brent:float, accese_token:str = Depends(JWTBearer())) -> dict:
    prediccion = crud.predictLuz(co2, gas, brent)
    if prediccion: return prediccion
    else: raise HTTPException(status_code=404, detail="Not prediccion")
