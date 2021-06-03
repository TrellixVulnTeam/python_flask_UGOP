from flask import Blueprint, render_template
home = Blueprint("home", __name__, template_folder='templates')


@home.route('/home')
def index():
    return render_template('index.html')