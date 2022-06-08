from lib2to3.pytree import Base
from typing import List, Optional
from pydantic import BaseModel


class PrediccionElectrica(BaseModel):
    gas: float
    brent: float
    co2: float
    
    class Config:
        orm_model = True
        schema_extra = {
            "example":{
                "gas":21.57,
                "brent":55.4288,
                "co2":7.74
            }
        }