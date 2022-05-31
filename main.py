from typing import List
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel
import os
import urllib

#DATABASE_URL = "sqlite:///./test.db"
DB_HOST = 'tfmdb1.database.windows.net'
DB_PORT = '1433'
DB_DATABASE = 'tfmdb1'
DB_USER = 'adm'
DB_PASSWORD = 'Pa$$w0rd01'
db_driver:str = "{ODBC Driver 17 for SQL Server}"


conn = f"""Driver={db_driver};Server=tcp:{DB_HOST},{DB_PORT};Database={DB_DATABASE};Uid={DB_USER};Pwd={DB_PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""

params = urllib.parse.quote_plus(conn)
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

engine_midb_dev = create_engine(conn_str, echo=True)
Session_mi_dev = sessionmaker(autocommit=False, autoflush=False, bind=engine_midb_dev)

Base_data = automap_base()
Base_data.prepare(engine_midb_dev, reflect =True, schema='dbo')


app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware)

@app.get("/hello/", status_code = status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    return 'HELLO'
