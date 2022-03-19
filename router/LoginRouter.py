import datetime
import hashlib
from fastapi import APIRouter, Depends, HTTPException
from model.Schemas import Login
from sqlalchemy.orm import Session
from model import Crud, Models, Schemas
from model.Database import SessionLocal, engine

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def postLogin(loginData : Login, db : Session = Depends(get_db)):
    password_encoded = loginData.password.encode()
    password_sha256 = hashlib.sha256(password_encoded).hexdigest()
    person = Crud.getLogin(db, password_sha256, loginData.email)

    if person:
        return {'response': 'Logged in'}
    raise HTTPException(status_code=404, detail=password_sha256)