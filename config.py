import logging
from pydantic import BaseSettings
from functools import lru_cache

log = logging.getLogger('uvicorn')

class Settings(BaseSettings):

    app_name:str = 'ConsumoElectrico'
    app_description:str = ''
    app_version:str = '0.0.1'
    app_host:str = '0.0.0.0'
    app_port:int = 80
    add_deamon:bool = True
    app_log_level:str = 'info'
    app_debug_mode:bool=True
    
    application_id = 'redelectricdata_dev'

    db_driver:str = "{ODBC Driver 17 for SQL Server}"
    
    env_root_path_local:str = ''
    env_root_path_dev:str = ''
    
    ENV_VAR:str = 'dev'

    JWT_SECRET:str = '024646D38F6F23A5E48888A1BC01E04A66D620FCB380B64107F0F7F2EBD5FAEF'
    JWT_ALGORITHM:str = 'HS256'

    #TENANT INFO
    DB_HOST:str = 'tfmdb1.database.windows.net'
    DB_PORT:str = '1433'
    DB_DATABASE:str = 'tfmdb1'
    DB_USER:str = 'adm'
    DB_PASSWORD:str = 'Pa$$w0rd01'
    
    ERROR_500 = 500
    ERROR_404 = 404
    
    dev_name = 'Juan Ignacio Jiménez Gutiérrez'
    dev_email = 'juan12_rubio@hotmail.com'

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config")
    return Settings()
    