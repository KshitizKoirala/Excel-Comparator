import os
import pandas as pd
# from sqlalchemy.exc import IntegrityError
# from excel_checker.extensions import db
from flask import redirect, url_for, flash, request, render_template, Blueprint

# from .user import User
from .user_form import addUserForm, input_excel
from excel_checker.excel_comparator.utils import add_as_excel, allowed_file


users = Blueprint('users', __name__)


# Code for adding and removing the users is below

# @users.route('/users')
# def get_all():
#     users_list = User.query.all()
#     return render_template('users.html', users=users_list)


# @users.route('/users/add', methods=['GET', 'POST'])
# def register():
#     form = addUserForm(request.form)
#     if request.method == 'POST' and form.validate():
#         fullname = form.fullname.data
#         branch = form.branch.data
#         boid = form.boid.data
#         phoneNumber = form.phoneNumber.data
#         ucc_code = form.ucc_code.data
#         client_code = form.client_code.data
#         user = User(fullname=fullname, branch=branch, boid=boid, phoneNumber=phoneNumber,
#                     ucc_code=ucc_code, client_code=client_code)
#         try:
#             db.session.add(user)
#             db.session.commit()
#             flash('User successfully created', 'success')
#             redirect(url_for('users.get_all'))
#             return render_template('add_user.html', form=form)
#         except IntegrityError:
#             db.session.rollback()
#             flash('User Already exists', 'danger')
#             return render_template('add_user.html', form=form)
#         finally:
#             db.session.close()
#     return render_template('add_user.html', form=form)


# For excel comparision with static DB like excel files
@users.route('/non-globals', methods=['GET', 'POST'])
def globaltononglobal():
    form = input_excel(request.form)
    if request.method == 'POST' and form.validate():
        # Get List of all the clients to be queried from
        users_list = pd.read_excel(
            f"{os.getcwd()}\\ExcelFiles\\Client List.xlsx")
        # Get List of documents lets say bankDocs
        bankDocs = request.files['BankExcel']
        # Check for variable name CLIENT UCC
        if (("CLIENT UCC" in users_list.columns) and (users_list is not None)):
            if allowed_file(bankDocs.filename) == True:
                # Creating a Dataframe using Pandas
                BankData = pd.read_excel(bankDocs, header=1)
                # Check if column exists or not in dataframe
                if ("Description" in BankData.columns):
                    matched_users = ['0']
                    unmatched_transfers = []
                    ukulele = [str(x) for x in BankData["Description"]]
                    cips = [x[5:].split()[0]
                            for x in ukulele if x[0:4] == 'CIPS']
                    # (0n2 time complexity) General procedure. Try Efficient algorithm
                    for c in cips:
                        for user in users_list["CLIENT UCC"]:
                            user = str(user)
                            if user == c:
                                matched_users.append(user)
                        if c != matched_users[-1]:
                            unmatched_transfers.append(c)

                    matched_users = [int(x) for x in matched_users]
                    # Creating a new dataframe using DATAFRAME.loc for sucessful_transfers
                    successful_transfer = users_list.loc[users_list['CLIENT UCC'].isin(
                        matched_users)]
                    # Filter rows of dataframe
                    successful_transfers = successful_transfer[[
                        'CLIENT NAME', 'CLIENT UCC', 'CLIENT CODE']]
                    # Check for fails
                    failed_bank_transfer = []
                    for fails in BankData['Description']:
                        fails = str(fails)
                        # Check for specific CIPS fails
                        if ((fails[0:4] == 'CIPS') and ((fails[5:].split()[0]) in unmatched_transfers)):
                            failed_bank_transfer.append(fails)
                     # Creating another new dataframe using DATAFRAME.loc for failed_transfers
                    failed_transfer = BankData.loc[BankData['Description'].isin(
                        failed_bank_transfer)]
                    failed_transfers = failed_transfer[[
                        'Description', 'Withdraw', 'Deposit']]
                    successful_transfers.name = bankDocs.filename
                    # Outputs the file in excel
                    add_as_excel(successful_transfers)
                    return render_template('user_results.html',  successful_table=[successful_transfers.to_html(classes='data_excel')], titles=successful_transfers.columns.values, failed_table=[failed_transfers.to_html(classes='failed_data_excel')])
                else:
                    return render_template("non-globals.html", bank_error="Invalid Excel Column Names", form=form)
            else:
                return render_template("non-globals.html", file_error="Invalid File Name", form=form)
        else:
            return render_template("non-globals.html", file_error="Please Check Client List", form=form)
    return render_template('non-globals.html', form=form)
