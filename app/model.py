import uuid
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Utilisateur(Base):
    __tablename__ = "user"
    id = Column(String(36), primary_key=True, default=generate_uuid)
    nom = Column(String(50))
    password = Column(String(50))
    email = Column(String(100), unique=True)


class Admin(Base):
    __tablename__ = "admin"
    id = Column(String(36), primary_key=True, default=generate_uuid)
    email = Column(String(100), unique=True)
    mot_de_passe = Column(String(128))
