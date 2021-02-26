from wtforms import Form, FileField

# Add your custom file upload field with custom messages


# Upload Excel Form
class addExcelFile(Form):
    BankExcel = FileField('Global to Global Bank Excel File Upload')
    TmsExcel = FileField('TMS Global to Global File Upload')


# Upload Excel Form
class ExcelFile(Form):
    BankExcel = FileField('Non Global Bank Excel File Upload')
    TmsExcel = FileField('TMS Non Global File Upload')
