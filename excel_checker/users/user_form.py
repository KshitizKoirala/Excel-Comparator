from wtforms import Form, StringField, IntegerField, validators, FileField


# User Registration Form
class addUserForm(Form):
    fullname = StringField('FullName', [validators.Length(min=1, max=50)])
    branch = StringField('Branch Name', [validators.Length(min=1, max=50)])
    boid = IntegerField('BOID')
    phoneNumber = IntegerField('Phone Number')
    ucc_code = IntegerField('Ucc Code')
    client_code = IntegerField('Client Code')


# Excel input form
class input_excel(Form):
    BankExcel = FileField('Global to Global Bank Excel File Upload')
