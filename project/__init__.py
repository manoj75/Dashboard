from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_migrate import Migrate
import pyodbc
import urllib.parse 

app = Flask(__name__)
modus = Modus(app)
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=hcpdigitalinsights.database.windows.net;DATABASE=hcpdigitalinsights;UID=hcpdigital;PWD=Hcp123digital")
#conn_uri="mssql+pymssql://hcpdigital:Hcp123digital@hcpdigitalinsights.database.windows.net/hcpdigitalinsights"
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "THIS SHOULD BE HIDDEN!"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import a blueprint that we will create
from project.users.views import users_blueprint
from project.dashboard.views import dashboard_blueprint
from project.models import Profession,SpecialtyGroup,GeoRegions

# register our blueprints with the application
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

@app.context_processor
def filters():
    print("(((((((((((((((((((( HERE ))))))))))))))))")
    professions=Profession.query.all()
    specialtyGroups=SpecialtyGroup.query.all()
    geoRegions=GeoRegions.query.all()
    return dict(professions=professions,specialtyGroups=specialtyGroups,geoRegions=geoRegions)

@app.route('/')
def root():
    return "HELLO BLUEPRINTS!"