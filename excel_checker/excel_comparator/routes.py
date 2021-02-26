import os
import pandas as pd
from flask import request, render_template, Blueprint
from .excel_form import addExcelFile, ExcelFile
from .utils import allowed_file, add_as_excel


# Initialize the Blueprint and getting in excel_comparation __init__ module
excel = Blueprint('excel', __name__)


@excel.route('/', methods=['GET', 'POST'])
def globaltoglobal():
    # global tmsDocs
    form = addExcelFile(request.form)
    if request.method == 'POST' and form.validate():
        bankDocs = request.files['BankExcel']
        tmsDocs = request.files['TmsExcel']
        if (allowed_file(bankDocs.filename) and allowed_file(tmsDocs.filename)) == True:
            # reading uploaded files and creating a DATAFRAME
            TmsData = pd.read_excel(tmsDocs)
            BankData = pd.read_excel(bankDocs, header=1)
            # CHECK if COLUMN exists
            if (("Description" in BankData.columns) and "TMS TRANSACTION ID" in TmsData.columns):
                matched_data = []
                matched_bank_data = []
                bankDescription = [str(x) for x in BankData["Description"]]
                bankTmsNumberList = [x[-7:-4] for x in bankDescription]
                # (0n2 time complexity) General procedure. Try Efficient algorithm
                for bank_tms_number in bankTmsNumberList:
                    for tms_data in TmsData["TMS TRANSACTION ID"]:
                        if str(bank_tms_number) == str(tms_data)[:3]:
                            matched_data.append(tms_data)
                            matched_bank_data.append(bank_tms_number)

                # Check for Unmatched failed_transfers
                failed_transfers = TmsData.loc[~TmsData['TMS TRANSACTION ID'].isin(
                    matched_data)]
                # Creating a new dataframe using DATAFRAME.loc for sucessful_transfers
                successful_transfer = TmsData.loc[TmsData['TMS TRANSACTION ID'].isin(
                    matched_data)]
                # Filter rows of dataframe
                successful_transfers = successful_transfer[[
                    'STATUS', 'CLIENT', 'AMOUNT (NPR)', 'TRANSFER TYPE']]
                failed_transfers = failed_transfers[[
                    'STATUS', 'CLIENT', 'AMOUNT (NPR)', 'TRANSFER TYPE']]
                successful_transfers.name = tmsDocs.filename
                # Outputs the file in excel
                add_as_excel(successful_transfers)
                return render_template('get_excel.html',  successful_table=[successful_transfers.to_html(classes='data_excel')], titles=successful_transfers.columns.values,
                                       failed_table=[failed_transfers.to_html(classes='failed_data_excel')])
            else:
                return render_template("excel.html", bank_error="Invalid Excel Column Names", form=form)
        else:
            return render_template("excel.html", file_error="Invalid File Name", form=form)
    return render_template('excel.html', form=form)


# BOID COLUMN NAME Comparision Excel to Excel
@excel.route('/boid', methods=['GET', 'POST'])
def nonglobal():
    # global tmsDocs
    form = ExcelFile(request.form)
    if request.method == 'POST' and form.validate():
        bankDocs = request.files['BankExcel']
        tmsDocs = request.files['TmsExcel']
        if (allowed_file(bankDocs.filename) and allowed_file(tmsDocs.filename)) == True:
           # reading uploaded files and creating a DATAFRAME
            TmsData = pd.read_excel(tmsDocs)
            BankData = pd.read_excel(bankDocs, header=1)
            # CHECK if COLUMN exists
            if (("Description" in BankData.columns) and "BATCH ID" in TmsData.columns):
                matched_data = []
                bankDescription = [str(x) for x in BankData["Description"]]
                bankTmsNumberList = [x[5:].split()[0]
                                     for x in bankDescription if x[0:4] == 'CIPS']
                # (0n2 time complexity) General procedure. Try Efficient algorithm
                for bank_tms_number in bankTmsNumberList:
                    for tms_data in TmsData["BATCH ID"]:
                        if str(bank_tms_number) == str(tms_data):
                            matched_data.append(tms_data)

                # Check for Unmatched failed_transfers
                failed_transfers = TmsData.loc[~TmsData['BATCH ID'].isin(
                    matched_data)]
                successful_transfer = TmsData.loc[TmsData['BATCH ID'].isin(
                    matched_data)]
                successful_transfers = successful_transfer[[
                    'STATUS', 'CLIENT', 'AMOUNT (NPR)', 'TRANSFER TYPE']]
                failed_transfers = failed_transfers[[
                    'STATUS', 'CLIENT', 'AMOUNT (NPR)', 'TRANSFER TYPE']]
                successful_transfers.name = tmsDocs.filename
                # Outputs the file in excel
                add_as_excel(successful_transfers)
                return render_template('get_excel.html',  successful_table=[successful_transfers.to_html(classes='data_excel')], titles=successful_transfers.columns.values,
                                       failed_table=[failed_transfers.to_html(classes='failed_data_excel')])
            else:
                return render_template("excel.html", bank_error="Invalid Excel Column Names", form=form)
        else:
            return render_template("excel.html", file_error="Invalid File Name", form=form)
    return render_template('excel.html', form=form)
