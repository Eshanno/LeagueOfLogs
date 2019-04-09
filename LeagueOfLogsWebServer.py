from flask import Flask , request, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
import os
#

SECRET_KEY=os.environ['SECRET_FLASK']

app=Flask(__name__)
bootstrap=Bootstrap(app)
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')

    return render_template('/homepage/home.html')
