from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    """users class"""
    __tablename__ = "users"

    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String , nullable = False , unique = True)
    email = db.Column(db.Text , nullable = False , unique = True)
    password = db.Column(db.Text , nullable = False)

    @classmethod
    def register(cls , username ,email , pwd):
        """save the user in the database with hashed  password"""
        hashedPWD = bcrypt.generate_password_hash(pwd)
        #Have to turn the bytestring to normal utf8 encoding 
        hashed_utf8 = hashedPWD.decode("utf8")
        # last return the new user with hashed password , in the server you will commit this 
        u = cls(username = username ,email = email , password = hashed_utf8)
        return u


    @classmethod
    def authenticate(cls , username , pwd):
        """validate if user exist and pwd is valid , return user if valid else return false"""
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password , pwd):
            return u 
        else:
            return False
    


class Post(db.Model):
    """this is the posts table"""
    __tablename__ = "posts"

    id = db.Column(db.Integer , primary_key = True , auto_increment = 1)
    userId = db.Column(db.Integer , db.ForeignKey('users.id'))
    # category = db.Column(db.String , db.ForeignKey('categories.id'), unique = False)
    text = db.Column(db.String)


class Category(db.Model):
    """category list"""
    __tablename__ = "categories"
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String , unique = True)
    

