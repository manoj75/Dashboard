from flask import Blueprint,render_template, redirect,url_for,request,flash
from project.models import User 

dashboard_blueprint =   Blueprint(
    'dashboard',
    __name__,
    template_folder='templates'
)

@dashboard_blueprint.route("/")
def hello():
    return "Dashboards will be here!"
