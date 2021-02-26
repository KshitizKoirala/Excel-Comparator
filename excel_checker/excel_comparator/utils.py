import os
import pandas as pd


ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# Check if correct file extension is provided


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Return matched documents
def non_global_as_excel(dataframe):
    return dataframe.to_excel(f"{os.getcwd()}\\ExcelFiles\\ Matched for {dataframe.name}.xlsx", index=False)


def add_as_excel(my_dataframe):
    # return my_dataframe.name
    # Set destination directory to save excel.
    xlsFilepath = f"{os.getcwd()}\\ExcelFiles\\Matched for {my_dataframe.name}.xlsx"
    # To format the columns I have used xlsxwriter
    writer = pd.ExcelWriter(xlsFilepath, engine='xlsxwriter')

    # Write excel to file using pandas to_excel
    my_dataframe.to_excel(writer, startrow=1,
                          sheet_name='Sheet1', index=False)

    # Indicate workbook and worksheet for formatting
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Iterate through each column and set the width == the max length in that column. A padding length of 2 is also added.
    for i, col in enumerate(my_dataframe.columns):
        # find length of column i
        column_len = my_dataframe[col].astype(str).str.len().max()
        # Setting the length if the column header is larger
        # than the max column value length
        column_len = max(column_len, len(col)) + 2
        # set the column length
        worksheet.set_column(i, i, column_len)
    return writer.save()
