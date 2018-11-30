import os
class Development(object):
    """
    dev environ configuration
    """
    POSTGRES = {
    'user':'keronei',
    'pw':'',
    'db':'model',
    'host':'localhost',
    'port':'5432'
}
    
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI =  'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s'%POSTGRES
    
class Production(object):
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
    