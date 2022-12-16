
from flask import *
from app.auth.forms import *
from app.auth import authentication as at
from app.auth.models import *
from flask_login import *


@at.route('/register', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()
    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('authentication.user_login'))

    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()

        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.user_login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.show_books'))
    return render_template('login.html', form=form)


@at.route('/logout')
@login_required
def user_logoff():
    logout_user()
    return redirect(url_for('main.show_books'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
