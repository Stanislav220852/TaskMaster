from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    BOT_TOKEN:str = os.getenv("BOT_TOKEN")

    DB_URL:str = os.getenv("DB_URL")
    DB_ECHO:bool = os.getenv("DB_ECHO")
    DB_AUTOFLUSH: bool = os.getenv("DB_AUTOFLUSH")
    DB_AUTOCOMMIT: bool = os.getenv("DB_AUTOCOMMIT")
    DB_EXPIRE_ON_COMMIT: bool  = os.getenv("DB_EXPIRE_ON_COMMIT")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    
    class Config:
        env_file = ".env"

settings = Settings()