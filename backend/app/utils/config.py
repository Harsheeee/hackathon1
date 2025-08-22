import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent  # points to app/
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    app_name: str = "Story_Telling_API"
    GOOGLE_API_KEY: str
    CLOUDINARY_CLOUD_NAME: str 
    CLOUDINARY_API_KEY: int
    CLOUDINARY_API_SECRET: str

    class Config:
        env_file = ENV_FILE

settings = Settings()

print("GOOGLE_API_KEY:", settings.GOOGLE_API_KEY)
print("CLOUDINARY_CLOUD_NAME:", settings.CLOUDINARY_CLOUD_NAME)
print("CLOUDINARY_API_KEY:", settings.CLOUDINARY_API_KEY)
print("CLOUDINARY_API_SECRET:", settings.CLOUDINARY_API_SECRET)
