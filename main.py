from flask import Flask, request,make_response,redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER_SECRET'


ALL = ['Buy coffe', 'Send the request', 'Video Production']

class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error )


@app.errorhandler(500)
def Internal_Server_Error(error):
    return render_template('500.html', error=error )


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'] )
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
         'ALL': ALL,
         'login_form': login_form,
         'username': username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        return redirect(url_for('index'))

    return render_template('hello.html', **context)