from xmlrpc.client import Boolean
from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str

class CreateUser(BaseModel):
    firstName: str
    lastName: str
    isAdmin: Boolean
    role: str
    teamId: str
    email: str
    password: str

class PatchUser(BaseModel):
    firstName: str
    lastName: str
    isAdmin: Boolean
    role: str
    teamId: str
    email: str
    password: str

