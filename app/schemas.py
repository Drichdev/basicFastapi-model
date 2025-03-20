# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UtilisateurBase(BaseModel):
    nom: str
    email: str

class UtilisateurCreate(UtilisateurBase):
    password: str

class UtilisateurUpdate(BaseModel):
    password: str

class UtilisateurOut(UtilisateurBase):
    id: str

    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    email: EmailStr

class AdminCreate(AdminBase):
    mot_de_passe: str

class Admin(AdminBase):
    id: str

    class Config:
        orm_mode = True
