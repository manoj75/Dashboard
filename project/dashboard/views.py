from flask import Blueprint,render_template, redirect,url_for,request,flash
from project.models import User 

dashboard_blueprint =   Blueprint(
    'dashboard',
    __name__,
    template_folder='templates'
)

@dashboard_blueprint.route("/sample1")
def sample1():
    return render_template('dashboard/index.html')

@dashboard_blueprint.route("/sample2")
def sample2():
    return render_template('dashboard/dashboard2.html')
