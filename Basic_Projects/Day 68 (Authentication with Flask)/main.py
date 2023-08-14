from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# create flask app and logi manager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()
login_manager.init_app(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    authenticated = db.Column(db.Boolean, default=False)

    def is_authenticated(self):
        return self.authenticated

    @staticmethod
    def is_active(self):
        return True

    @staticmethod
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email
 
 
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.email == user_id)).scalar()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # error message for login
        error = None
        # hashing password
        hashed_password = generate_password_hash(
            password=request.form.get("password"),
            method="pbkdf2:sha256",
            salt_length=8
        )
        try:
            # adding new user to db
            new_user = User(
                email=new_user_email,
                password=hashed_password,
                name=request.form.get("name"),
            )
            db.session.add(new_user)
            db.session.commit()
        except:
            # error for email already exists
            error = "Email already used in an account. Please, login:"
        print(error)
        return render_template("login.html", error=error, logged_in=current_user.is_authenticated)
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        # getting user object
        user_id = request.form.get("email")
        user = db.session.execute(db.select(User).where(User.email == user_id)).scalar()
        if user:
            if check_password_hash(pwhash=user.password, password=request.form.get("password")):
                user.authenticated = True
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("secrets", logged_in=current_user.is_authenticated))
            else:
                error = "Wrong password."
        else:
            error = "Email not found."
    return render_template("login.html", error=error, logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    user = current_user
    user.authenticated = False
    db.session.commit()
    logout_user()
    return redirect(url_for("home", logged_in=current_user.is_authenticated))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static", path="files/cheat_sheet.pdf", as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
