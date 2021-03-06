from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField,SelectField
from wtforms.validators import InputRequired, Email, Length

class AddNewUserForm(FlaskForm):
    #username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)],render_kw={"type":"email", "class":"form-control", "id":"inputUsername", "placeholder":"User Name"})
    #email = StringField('email', validators=[InputRequired()],render_kw={"type":"email", "class":"form-control", "id":"inputEmail", "placeholder":"Email Address"})
    #customer=SelectField('customer', choices=[],render_kw={ "class":"form-control", "id":"inputCustomer"})

    username    =   StringField('username',validators=[InputRequired(), Length(max=80)],render_kw={"type":"email", "class":"form-control", "id":"inputUsername", "placeholder":"User Name"})
    email       =   StringField('email',validators=[InputRequired()],render_kw={"type":"email", "class":"form-control", "id":"inputEmail", "placeholder":"Email Address"})
    customer    =   SelectField('customer',coerce =int, render_kw={ "class":"form-control", "id":"inputCustomer"})
    firstname   =   StringField('fname',validators=[InputRequired()],render_kw={"class":"form-control", "id":"inputFname", "placeholder":"First Name"})
    lastname    =   StringField('lname',validators=[InputRequired()],render_kw={"class":"form-control", "id":"inputLname", "placeholder":"Last Name"})


class NewCustomerForm(FlaskForm):
    customername    =   StringField('customername',validators=[InputRequired()],render_kw={"class":"form-control", "id":"inputCustomername", "placeholder":"Customer Name"})
    