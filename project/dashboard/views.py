import json
import requests
import adal
import re
from project.models import User ,Profession
from flask import Blueprint,render_template, redirect,url_for,request,flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

dashboard_blueprint =   Blueprint(
    'dashboard',
    __name__,
    template_folder='templates'
)

@dashboard_blueprint.route("/")
def Index():
    resource_url = 'https://analysis.windows.net/powerbi/api'
    username='*****'
    password='****'

    client_id='4e4bf593-32b5-4d99-a860-bb26cdb0e2f7'
    AuthContext= adal.AuthenticationContext("https://login.windows.net/common")
    token=AuthContext.acquire_token_with_username_password(resource_url,username,password,client_id)
    #create_row_data = {'id': '1235','name':'Joel','created_on':'27/01/2018','modified_on':'27/01/2018','desc':'This is Joel!!'}
    #create_row_data={'grant_type': 'password','resource': 'https://analysis.windows.net/powerbi/api','client_id': '4e4bf593-32b5-4d99-a860-bb26cdb0e2f7','username': 'Bill.Reinstein@HCPdigitalinsights.com','password': 'Bilso1520'}
    #print(AuthContext)
    #print(token["accessToken"])
    accessToken=token["accessToken"]
    #print("======================================================")
    #print(accessToken)
    #print("======================================================")
    url="https://api.powerbi.com/v1.0/myorg/groups/42b9d168-fefb-4b3c-aa2d-af24fb08f4d8/reports"
    headers = {'Authorization': 'Bearer ' + accessToken,'Content-type': 'application/json', 'Accept': 'application/json'}
    response=requests.get(url, headers=headers)
    #print("-----------------------------------------")
    reportId=response.json()["value"][0]['id']
    #print(reportId)
    #print("-----------------------------------------")
    reportUrl=response.json()["value"][0]["webUrl"]+"/GenerateToken"
    #reportUrl="https://api.powerbi.com/v1.0/myorg/reports/"+response.json()["value"][0]['id']+"/GenerateToken"
    reportUrl="https://api.powerbi.com/v1.0/myorg/groups/42b9d168-fefb-4b3c-aa2d-af24fb08f4d8/reports/f01e98f3-abb9-4f51-bca3-a9eb419ee97e/GenerateToken"
    #print("reportUrl="+reportUrl)

    #headers = {'Authorization': 'Bearer ' + accessToken,'Content-type': 'application/json', 'Accept': 'application/json'}
    data1= {'allowSaveAs': 'false'}
    responseEmbedToken=requests.post(reportUrl,data=json.dumps(data1),headers=headers)
    #print("+++++++++++++++++++++++++++++++++++++++++")
    #print(responseEmbedToken.text)
    #print response.
    #print(responseEmbedToken.url)
    #print(responseEmbedToken.json()["token"])
    #print("++++++++++++++++++++++++++++++++++++++++++")
    embedurl="https://app.powerbi.com/reportEmbed?reportId="+reportId+"&groupId=42b9d168-fefb-4b3c-aa2d-af24fb08f4d8"
    configObj={'token':responseEmbedToken.json()["token"],'embedurl':embedurl,'reportid':reportId}
    #print(responseEmbedToken.json())
    #print(response.json()["value"][0].webUrl)
    #r = requests.post(url=api_url, json=create_row_data)
    #print(r.status_code, r.reason, r.text)
    profession=Profession.query.all()
    return render_template('dashboard/index.html',configObj=json.dumps(configObj))

@dashboard_blueprint.route("/campaign/<id>")
def Campaign(id):
    campaignId=id
    resource_url = 'https://analysis.windows.net/powerbi/api'
    username='***'
    password='***'
    print(current_user)
    profession=Profession.query.all()
    client_id='4e4bf593-32b5-4d99-a860-bb26cdb0e2f7'
    AuthContext= adal.AuthenticationContext("https://login.windows.net/common")
    token=AuthContext.acquire_token_with_username_password(resource_url,username,password,client_id)
    accessToken=token["accessToken"]
    url="https://api.powerbi.com/v1.0/myorg/groups/42b9d168-fefb-4b3c-aa2d-af24fb08f4d8/reports"
    headers = {'Authorization': 'Bearer ' + accessToken,'Content-type': 'application/json', 'Accept': 'application/json'}
    response=requests.get(url, headers=headers)
    reportId=response.json()["value"][0]['id']
    reportUrl=response.json()["value"][0]["webUrl"]+"/GenerateToken"
    #reportUrl="https://api.powerbi.com/v1.0/myorg/reports/"+response.json()["value"][0]['id']+"/GenerateToken"
    reportId="f01e98f3-abb9-4f51-bca3-a9eb419ee97e"
    reportId="187ffc03-1c8e-4cb8-a19c-d182c2b01b16"
    reportUrl="https://api.powerbi.com/v1.0/myorg/groups/42b9d168-fefb-4b3c-aa2d-af24fb08f4d8/reports/"+reportId+"/GenerateToken"
    data1= {
            'allowSaveAs'   : 'false',
            "accessLevel"   : "view",
            "identities"    : [
                                {
                                    "username":campaignId,
                                    "roles":["Campaign"],
                                    "datasets":["80529fbe-4cae-49aa-a27c-2106c3d8aad7"]
                                }
                              ]
            }

    responseEmbedToken=requests.post(reportUrl,data=json.dumps(data1),headers=headers)
    embedurl="https://app.powerbi.com/reportEmbed?reportId="+reportId+"&groupId=42b9d168-fefb-4b3c-aa2d-af24fb08f4d8"
    configObj={'token':responseEmbedToken.json()["token"],'embedurl':embedurl,'reportid':reportId}
    return render_template('dashboard/Pbi.html',profession=profession,configObj=json.dumps(configObj))


@dashboard_blueprint.route("/ProfessionalInsights")
def ProfessionalInsights():
    return render_template('dashboard/index.html')

@dashboard_blueprint.route("/ContentInsights")
def ContentInsights():
    return render_template('dashboard/ContentInsights.html')

@dashboard_blueprint.route("/DeviceTypes")
def DeviceTypes():
    return render_template('dashboard/DeviceType.html')
