import os
class OverallConfig(object):
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    
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
    
app_config = {
    'development': Development,
    'production': Production,
}
        
