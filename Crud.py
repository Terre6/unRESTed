import hashlib
import os
import uuid
from fastapi import UploadFile
from sqlalchemy.orm import Session
from model import Models
from model.Schemas import CreateUser, PatchUserForm

def getUserByID(db: Session, publicId: int):
    return db.query(Models.User).filter(Models.User.publicId == publicId).first()

def createUser(user: CreateUser, db: Session):
    passw_encoded = user.password.encode()
    password_encoded_sha256 = hashlib.sha256(passw_encoded).hexdigest()
    password_sha256 = password_encoded_sha256 
    public_id = str(uuid.uuid4())
    dbUser = Models.User(publicId = public_id, firstName = user.firstName, lastName = user.lastName, password = user.password, passwordSha256 = password_sha256)
    db.add(dbUser)
    db.commit()
    return dbUser