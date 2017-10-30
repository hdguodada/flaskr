from flask import Flask, render_template
from flask import request
from flask import make_response

from flask_script import Manager

from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def index():
    return render_tempalte('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)



if __name__ == '__main__':
    manager.run()
