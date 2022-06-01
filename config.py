import logging
from pydantic import BaseSettings
from functools import lru_cache

log = logging.getLogger('uvicorn')

class Settings(BaseSettings):
    ENV_VAR: str = ''
    
    app_name:str = ''
    app_description:str = ''
    app_version:str = '0.0.1'
    app_host:str = '0.0.0.0'
    app_port:int = 8000
    add_deamon:bool = True
    app_log_level:str = 'info'
    app_debug_mode:bool=True
    
    application_id = 'redelectricdata_dev'
    
    JWT_SECRET: str = ''
    JWT_ALGORITHM: str = ''
    
    db_driver:str = "{ODBC Driver 17 for SQL Server}"
    
    DB_HOST:str = ''
    DB_PORT:str = ''
    DB_DATABASE:str = ''
    DB_USER:str = ''
    DB_PASSWORD:str = ''
    
    env_root_path_local:str = ''
    env_root_path_dev:str = ''
    
    class Config:
        env_file = '.env'

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config")
    return Settings()
    