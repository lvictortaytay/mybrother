from flask_wtf import FlaskForm
from wtforms import  StringField , PasswordField
from wtforms.validators import Email , InputRequired 

# from wtfforms.validators import InputRequired


class LoginForm(FlaskForm):
    """login form"""
    Username = StringField("username" , validators = [InputRequired(message = "please enter username")])
    Password = PasswordField("password" , validators = [InputRequired(message = "please enter password")])

class RegisterForm(FlaskForm):
    """login form"""
    Username = StringField("username" , validators = [InputRequired(message = "please enter username")])
    Email = StringField("email" , validators = [Email(message = "please enter a valid email address")])
    Password = StringField("password" , validators = [InputRequired(message = "please enter password")])
    RePassword = StringField("re-enter password" , validators = [InputRequired(message = "please re-enter password")])
    