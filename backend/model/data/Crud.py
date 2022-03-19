import hashlib
import os
import uuid
from fastapi import UploadFile
from sqlalchemy.orm import Session
from backend.model.Models import Reservation, Team
from model import Models
from model.Schemas import CreateUser, PatchUserForm

def getUserByID(db: Session, publicId: int):
    return db.query(Models.User).filter(Models.User.publicId == publicId).first()

def createUser(user: CreateUser, db: Session):
    passw_encoded = user.password.encode()
    password_sha256 = hashlib.sha256(passw_encoded).hexdigest()
    public_id = str(uuid.uuid4())
    dbUser = Models.Person(publicId = public_id, firstName = user.firstName, lastName = user.lastName, isAdmin = False, role = user.role, teamID = user.teamId, email = user.email, password = password_sha256)
    db.add(dbUser)
    db.commit()
    return dbUser

def createTeam(team: Team, db:Session):
    public_id = str(uuid.uuid4())
    dbTeam = Models.Team(publicId = public_id, teamName = team.teamName)
    db.add(dbTeam)
    db.commit()
    return dbTeam

def createReservation(reservation: Reservation, db: Session):
    public_id = str(uuid.uuid4())
    dbReservation = Models.Reservation(publicId = public_id, roomId = reservation.roomId, reservationStart = reservation.reservationStart, reservationEnd = reservation.reservationEnd)
    db.add(dbReservation)
    db.commit()
    return dbReservation

#promjena