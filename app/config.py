import os
class OverallConfig(object):
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    POSTGRES = {
    'user':'keronei',
    'pw':'',
    'db':'model',
    'host':'localhost',
    'port':'5432'
    }
    SQLALCHEMY_DATABASE_URI =  'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s'%POSTGRES
class Development(OverallConfig):
    """
    dev environ configuration
    """
    DEBUG = True
    TESTING = True
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class Production(OverallConfig):
    """
    pro env config
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
    
app_config = {
    'development': Development,
    'production': Production,
}

