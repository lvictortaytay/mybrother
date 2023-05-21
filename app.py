from flask import Flask  , render_template , redirect , session , request
from models import db , connect_db , User , Post
from forms import LoginForm , RegisterForm
import json



app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mybrother'
app.config['SECRET_KEY'] = 'WDIEOC'


connect_db(app)
@app.route("/")
def getHomePage():
    session['userId'] = ''
    return render_template("welcome.html")


@app.route("/home")
def welcomePage():
    return render_template("home.html")


@app.route("/login" , methods = ["GET" , "POST"])
def loginPage():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.Username.data
        password = form.Password.data
        user = User.authenticate(username , password)
        
        
        if user:
            print("im in")
            session['loggedIn'] = 'True'
            session['user'] = username
            session['userId'] = user.id
            return render_template("welcomeUser.html" , user = username)
        else:

            return "doesnt work"
    print("failed")
    return render_template("login.html", form = form)
        

        


@app.route("/register" , methods = ["GET" , "POST"])
def registerPage():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.Username.data)
        print("validated")
        username = form.Username.data
        email = form.Email.data
        password = form.Password.data
        newUser = User.register(username = username , email = email ,pwd = password)
        db.session.add(newUser)
        db.session.commit()
        return redirect("/")
    else:
        print("did not validate")
        return render_template("register.html" , form = form)



@app.route("/makePost" , methods = ["POST" , "GET"] )
def makepost():
    text = request.args.get("text")
    id = session.get('userId')
    newPost = Post(userId = id , text = text)
    print(session)
    db.session.add(newPost)
    db.session.commit()
    print(newPost)
    users = Post.query.all()
    return render_template("home.html", users = users)



@app.route("/versions")
def getHomePage1():
    versions = []
    res = requests.get("https://api.scripture.api.bible/v1/bibles", headers= {"api-key":"378b8ef9f012dece789566d4542e04c0"}).json()
    x = 0
    while x <= len(res['data']):
        print(x)
        data = res['data'][x -1]
        for name in data:
            if name == "name":
                versions.append(data[name])
        
        x += 1
    print(versions)
    print(x)
    
    return render_template("index.html" , versions = versions )
    