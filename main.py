# main.py
from fastapi import FastAPI, Depends, HTTPException , status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html
from sqlalchemy.orm import Session
from app import model, config
from app.routers import users
from app.database import engine, get_db
from app.auth import auth

import secrets

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API", docs_url=None, redoc_url=None)

def create_default_admin(db: Session):
    admin_user = db.query(model.Admin).filter(model.Admin.email == config.settings.admin_username).first()
    if not admin_user:
        hashed_pw = auth.hash_password(config.settings.admin_password)
        new_admin = model.Admin(email=config.settings.admin_username, mot_de_passe=hashed_pw)
        db.add(new_admin)
        db.commit()

with next(get_db()) as db:
    create_default_admin(db)


app.include_router(users.router, prefix="/api", tags=["users"])


security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "secret")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identifiants incorrects",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/docs", include_in_schema=False)
def custom_swagger_ui(username: str = Depends(verify_credentials)):
    """
    Renvoie l'interface Swagger UI protégée par authentification.
    """
    return get_swagger_ui_html(openapi_url=app.openapi_url, title="Documentation de l'API")
