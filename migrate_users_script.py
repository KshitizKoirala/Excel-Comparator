# SCRIPT TO MIGRATE A LIST OF USERS i.e. EXCEL FILES TO DATABASE COLUMNS

# import os
# import pandas as pd
# from excel_checker.users.user import User

# from excel_checker.extensions import db

# CREATING A DATAFRAME
# users_docs = pd.read_excel('excel_checker/ExcelFiles/Client List.xlsx')
# # print(users_docs.values[1])


# ADDING USERS TO DATABASE
# def add_users_to_db(dataframe):
#     try:
#         for row in dataframe.values:
#             with app.app_context():
#                 records = User(**{
#                     'fullname': row[3],
#                     'branch': row[8],
#                     'boid': row[6],
#                     'ucc_code': row[5],
#                     'client_code': row[4]
#                 })

#                 db.session.add(records)
#                 db.session.commit()
#     except:
#         db.session.rollback()
#     finally:
#         db.session.close()

#     print(records)

# # objects = [
# #     User(name="u1"),
# #     User(name="u2"),
# #     User(name="u3")
# # ]
# # s.bulk_save_objects(objects)

#     # try:
#     #     db.session.add()
#     #     db.session.commit()
#     # except ImportError:
#     #     db.session.rollback(

# INITIALIZE THE FUNCTION WITH DATAFRAME FROM PANDAS
# add_users_to_db(users_docs)
