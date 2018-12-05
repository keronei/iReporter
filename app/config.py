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
class Development(OverallConfig):
    """
    dev environ configuration
    """
    DEBUG = True
    TESTING = True
    
class Production(OverallConfig):
    """
    pro env config
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    
    
app_config = {
    'development': Development,
    'production': Production,
}