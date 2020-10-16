from flask import render_template, request, Response, redirect, url_for, flash
from Hackathon_UTU import app
from Hackathon_UTU.forms import *
#from Hackathon_UTU.models import *
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import or_


@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

