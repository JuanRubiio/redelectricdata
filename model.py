from database import Base, Base_data, engine_midb_dev
from sqlalchemy import Table
#CONSUMO = Base_data.classes.CONSUMO

class CONSUMO(Base):
    __table__ = Table('consumo', Base_data.metadata, autoload=True, autoload_with=engine_midb_dev)
    __mapper_args__ = {'primary_key':[__table__.c.id]}

class USER(Base):
    __table__ = Table('user', Base_data.metadata, autoload=True, autoload_with=engine_midb_dev)
    __mapper_args__ = {'primary_key':[__table__.c.user_id]}

class CONSUMO_PREDICT(Base):
    __table__ = Table('consumo_predict', Base_data.metadata, autoload=True, autoload_with=engine_midb_dev)
    __mapper_args__ = {'primary_key':[__table__.c.id]}

class EMPLEO(Base):
    __table__ = Table('empleo', Base_data.metadata, autoload=True, autoload_with=engine_midb_dev)
    __mapper_args__ = {'primary_key':[__table__.c.id]}

class PREDICCION_ELECTRICIDAD(Base):
    __table__ = Table('luz_gas_co2_brent', Base_data.metadata, autoload=True, autoload_with=engine_midb_dev)
    __mapper_args__ = {'primary_key':[__table__.c.id]}