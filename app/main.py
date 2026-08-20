# to run the app use the command: uvicorn app.main:app --reload
# asgi - Asynchronous Server Gateway Interface
# python imports module using . notation thatwhy we use app.main
# :app because of the server name app=FastAPI()

from fastapi import FastAPI
# fast api is a frameworking for building the application
# uvicorn is the server which handles the incomming request
from sqlalchemy import text
from app.database import engine

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Banking API is running"}


@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection: # make a connection with mysql
            result = connection.execute(text("SELECT 1"))
            return {
                "status": "Connected Successfully",
                "result": result.scalar()
            }
    except Exception as e:
        return {
            "status": "Connection Failed",
            "error": str(e)
        }