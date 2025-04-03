from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    BOT_TOKEN:str = os.getenv("BOT_TOKEN")
    class Config:
        env_file = ".env"


settings = Settings()