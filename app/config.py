import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
