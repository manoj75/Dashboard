import json
import requests
import adal
import re
from project import db
from flask import Blueprint,render_template, redirect,url_for,request,flash
from project.models import User ,Profession, Customer
from project.admin.forms import AddNewUserForm,NewCustomerForm
from werkzeug.security import generate_password_hash, check_password_hash

admin_blueprint =   Blueprint(
    'admin',
    __name__,
    template_folder='templates'
)

@admin_blueprint.route("/")
def Index():
    return render_template('admin/index.html')

@admin_blueprint.route("/newcustomer", methods=['GET', 'POST'])
def AddNewCustomer():
    form = NewCustomerForm()
    print(form)
    print(request.method)
    if request.method=="GET":
        return render_template('admin/AddNewCustomer.html',newCustomerForm=form)
    if request.method=="POST":
        print(form.validate_on_submit())
    if form.validate_on_submit() :
        new_customer = Customer(name=form.customername.data)
        print(new_customer)
        db.session.add(new_customer)
        db.session.commit()
        return render_template('admin/AddNewCustomer.html',newCustomerForm=form,success=True)
    else:
        print(form.errors)
    return render_template('admin/AddNewCustomer.html')

@admin_blueprint.route("/newuser", methods=['GET', 'POST'])
def AddNewUser():
    form = AddNewUserForm()
    form.customer.choices=[(customer.id, customer.name) for customer in Customer.query.all()]
    print(form)
    print(request.method)
    if request.method=="GET":
        return render_template('admin/AddNewUser.html',newUserForm=form)
    if request.method=="POST":
        print(form.validate_on_submit())
    if form.validate_on_submit() :
        # code to process form
        #print("Validated")
        #hashed_password = generate_password_hash(form.password.data, method='sha256')
        hashed_password = generate_password_hash("123", method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password,customerid=form.customer.data,firstname=form.firstname.data,lastname=form.lastname.data)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        return render_template('admin/AddNewUser.html',newUserForm=form,success=True)
    else:
        print("1111="+form.customer.data)
        print(form.errors)
    return render_template('admin/AddNewUser.html',newUserForm=form)
        

@admin_blueprint.route("/newcampaign")
def AddNewCampaign():
    return render_template('admin/AddNewCampaign.html')


@admin_blueprint.route("/resetpassword")
def ResetPassword():
    return render_template('admin/resetPassword.html')
