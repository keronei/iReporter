"""This file is the model that handle requests from views. Manipulates the database accordingly"""
import psycopg2
import jwt
import json
from datetime import datetime, timedelta
from ....config import DataBase
from ....config import app_config


class UserModel():
    """Handles the requests from exposed endpoints"""
    def __init__(self):
        self.db_connect = DataBase().db
        self.migrations = DataBase().create_tables()
        self.checker = checker_sql = "SELECT id, email, password from users WHERE email = %s;"
    def add_user(self, data):
        """Adds a new user via sign up"""
        #fetch to see if exists:
        
        creator_sql = "INSERT into users(firstname, lastname, email, username, isadmin, password, phonenumber) VALUES (%s, %s, %s, %s, False, %s, %s) RETURNING id;"
        cursor = self.db_connect.cursor()
        parse_received_data = json.dumps(data)
        string_format = json.loads(parse_received_data)
        
        sent_firstname = string_format['firstname']
        sent_secondname = string_format['secondname']
        sent_mail = string_format['email'] 
        sent_phonenumber = string_format['phoneNumber']
        sent_username = string_format['username']
        sent_password = string_format['password']
        
        existing = cursor.execute(self.checker, (sent_mail,))
        found_count = cursor.fetchall()
        if cursor.rowcount > 0:
            return sent_mail ,"Already registered!"
        
        cursor.execute(creator_sql, (sent_firstname,sent_secondname, sent_mail, sent_username, sent_password, sent_phonenumber,))
        generated_id = cursor.fetchone()[0]
        self.db_connect.commit()
        cursor.close()
       
        return "user created with id:",generated_id
    def user_login(self, credentials):
        """Auth an existing user"""
        pass
    def generate_token(self,user_id):
        """Generate the token"""
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            jwt_string = jwt.encode(
                payload,
                app_config.get('SECRET'),
                algorithm='HS256'
            )
            return jwt_string
        except Exception as e:
            return str(e)
    @staticmethod
    def decode_token(token):
        """Decode auth token from header """
        try:
            payload = jwt.decode(token,  app_config.get('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Token expired, You may have to login again"
        except jwt.InvalidTokenError:
            return "Invalid token. Login or create an account instead"
    def user_helper(self, identifier):
        """"""
        flags = self.get_entry_helper(identifier)
        return {"Status":200, "Data":flags} 
    