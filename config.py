from decouple import config


class Config:
    SECRET_KEY = 'Clave$ecret@12345'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    MYSQL_DB = 'qr_db'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}