import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

dsn = cx_Oracle.makedsn(settings.ORACLE_HOST, settings.ORACLE_PORT, service_name=settings.ORACLE_SERVICE_NAME)
DATABASE_URL = f"oracle+cx_oracle://{settings.ORACLE_USER}:{settings.ORACLE_PASSWORD}@/?dsn={dsn}"

try:
    cx_Oracle.init_oracle_client(lib_dir="/Users/macbook/Documents/oracleInstance")
except Exception as e:
    print("Oracle client déjà initialisé ou erreur d'initialisation :", e)

engine = create_engine(
    DATABASE_URL,
    connect_args={"mode": cx_Oracle.SYSDBA},
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dépendance pour récupérer la session en endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
