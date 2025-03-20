import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    admin_username: str = os.getenv("ADMIN_USERNAME", "admin@admin")
    admin_password: str = os.getenv("ADMIN_PASSWORD", "admin")
    ORACLE_HOST: str  = os.getenv("ORACLE_HOST", "localhost")
    ORACLE_PORT: str  = os.getenv("ORACLE_PORT", "1521")
    ORACLE_SERVICE_NAME: str  = os.getenv("ORACLE_SERVICE_NAME", "ORCLCDB")
    ORACLE_USER: str  = os.getenv("ORACLE_USER", "SYS")
    ORACLE_PASSWORD: str  = os.getenv("ORACLE_PASSWORD", "mypassword1")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    
    class Config:
        env_file = ".env"

settings = Settings()
