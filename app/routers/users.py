# routers/user.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.model import Utilisateur
from app.schemas import UtilisateurCreate, UtilisateurOut, UtilisateurUpdate
from app.database import get_db
from app.auth.auth import get_password_hash
from app.auth import dependances

router = APIRouter()

@router.post("/users/", response_model=UtilisateurOut)
def create_user(user: UtilisateurCreate, db: Session = Depends(get_db),credentials: str = Depends(dependances.verify_admin_credentials)):
    db_user = db.query(Utilisateur).filter(Utilisateur.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = Utilisateur(nom=user.nom, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/", response_model=List[UtilisateurOut])
def get_users(db: Session = Depends(get_db), credentials: str = Depends(dependances.verify_admin_credentials)):
    users = db.query(Utilisateur).all()
    return users

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, db: Session = Depends(get_db), credentials: str = Depends(dependances.verify_admin_credentials) ):
    db_user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

@router.put("/users/{user_id}", response_model=UtilisateurOut)
def update_password(user_id: str, user: UtilisateurUpdate, db: Session = Depends(get_db), credentials: str = Depends(dependances.verify_admin_credentials)):
    db_user = db.query(Utilisateur).filter(Utilisateur.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.password = get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user
