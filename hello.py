from flask import Flask, render_template, url_for, flash, redirect, session
from flask import request
from flask import make_response

from flask_script import Manager

from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, BooleanField, SubmitField

from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'you will never guess'

bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('you has changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(404)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
