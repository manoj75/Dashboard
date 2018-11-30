from flask import Blueprint,render_template, redirect,url_for,request,flash
from project.models import User 

dashboard_blueprint =   Blueprint(
    'dashboard',
    __name__,
    template_folder='templates'
)

@dashboard_blueprint.route("/")
def Index():
    return render_template('dashboard/index.html')

@dashboard_blueprint.route("/ProfessionalInsights")
def ProfessionalInsights():
    return render_template('dashboard/index.html')

@dashboard_blueprint.route("/ContentInsights")
def ContentInsights():
    return render_template('dashboard/ContentInsights.html')

@dashboard_blueprint.route("/DeviceTypes")
def DeviceTypes():
    return render_template('dashboard/DeviceType.html')
