import os
import psycopg2
class OverallConfig(object):
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
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
    
app_config = {
    'development': Development,
    'production': Production,
}
class DataBase():
    def __init__(self):
        self.db = psycopg2.connect(host="localhost", database="users", user="keronei", password="")
    def create_tables(self):
        #Create the tables, but first check if they exist.
        create = ("""
            CREATE TABLE IF NOT EXISTS  users (
                    id SERIAL PRIMARY KEY,
                    firstname VARCHAR(50) NOT NULL,
                    lastname VARCHAR(50) NOT NULL,
                    othernames VARCHAR(50),
                    email VARCHAR(50) NOT NULL,
                    username VARCHAR(50) NOT NULL,
                    registered TIMESTAMP,
                    phoneNumber VARCHAR(15) NOT NULL,
                    password VARCHAR(200) NOT NULL,
                    isAdmin BOOLEAN
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS  incident (
                    incident_id SERIAL PRIMARY KEY,
                    createdOn VARCHAR(50) NOT NULL,
                    createdBy INTEGER NOT NULL,
                    type VARCHAR(50) NOT NULL,
                    location VARCHAR(50),
                    status VARCHAR(50) NOT NULL,
                    images VARCHAR(250) NOT NULL,
                    videos VARCHAR(250) NOT NULL,
                    comment VARCHAR(250) NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS incidence_users (
                    id INTEGER NOT NULL,
                    incident_id INTEGER NOT NULL,
                    PRIMARY KEY (id , incident_id),
                    FOREIGN KEY (incident_id)
                        REFERENCES users (id)
                        ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (incident_id)
                        REFERENCES incident (incident_id)
                        ON UPDATE CASCADE ON DELETE CASCADE
            )
            """)
        cursor = self.db.cursor()
        for tables in create:
            cursor.execute(tables)
        cursor.close()
        self.db.commit()
        
