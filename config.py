#config.py
import os

class Config:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'pierre')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'ton_mot_de_passe')
    DB_NAME = os.getenv('DB_NAME', 'wallet_db')
