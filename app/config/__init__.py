import os


class Config:
    SECRET_KEY = "top secret"
    JWT_ACCESS_LIFESPAN = {"hours": 24}
    JWT_REFRESH_LIFESPAN = {"days": 30}
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace('postgres:', 'postgresql:')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
