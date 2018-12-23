from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_migrate import Migrate
import pyodbc
import urllib.parse 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
modus = Modus(app)
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=***;DATABASE=***;UID=hcpdigital;PWD=****")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import a blueprint that we will create
from project.users.views import users_blueprint
from project.dashboard.views import dashboard_blueprint
from project.login.views import login_blueprint
from project.admin.views import admin_blueprint

from project.models import Profession,SpecialtyGroup,GeoRegions,Segment,Customer,User

# register our blueprints with the application
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')
app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(admin_blueprint,url_prefix='/admin')

@app.context_processor
def filters():
    professions=Profession.query.all()
    specialtyGroups=SpecialtyGroup.query.all()
    geoRegions=GeoRegions.query.all()
    Segments=Segment.query.all()
    print("--------------------------")
    print(current_user)
    customerName=Customer.query.get(current_user.customerid).name
    print("Customer Name="+customerName)
    print("--------------------------")
    return dict(customer_name=customerName,segments=Segments,professions=professions,specialtyGroups=specialtyGroups,geoRegions=geoRegions)

@app.route('/')
def root():
    return "HELLO BLUEPRINTS!"