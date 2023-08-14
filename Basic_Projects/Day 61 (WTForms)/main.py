from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length
from flask_bootstrap import Bootstrap4


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
bootstrap = Bootstrap4(app)
app.secret_key = 'batata'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        admin_email = "admin@email.com"
        admin_password = "12345678"
        if login_form.email.data == admin_email and login_form.password.data == admin_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
