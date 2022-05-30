from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import MetaData
import contextlib
import urllib.parse
from .config import config

settings = config.get_settings()

conn = f"""Driver={settings.db_driver};Server=tcp:{settings.DB_HOST},{settings.DB_PORT};Database={settings.DB_DATABASE};Uid={settings.DB_USER};Pwd={settings.DB_PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""

params = urllib.parse.quote_plus(conn)
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_midb_dev = create_engine(conn_str, echo=True)
Session_mi_dev = sessionmaker(autocommit=False, autoflush=False, bind=engine_midb_dev)

Base_data = automap_base()
Base_data.prepare(engine_midb_dev, reflect =True, schema='dbo')

@contextlib.contextmanager
def getSession():
    conn = Session_mi_dev()
    try:
        yield conn
    finally:
        conn.close()

