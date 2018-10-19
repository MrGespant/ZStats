# This script should parse given XLS file and fill the database with included data
#
#

import xlrd
import dbscripts
from resources.secrets import config
from os import listdir

database = dbscripts.db_init()

for file in listdir(config.files_dir):
    # store import file information
    insertFileQuery = f"""INSERT INTO files (filename, date_processed) 
                          VALUES ("{file}", "{file[23:-4]}")"""
    dbscripts.db_query(database, insertFileQuery)

    sheet = xlrd.open_workbook(config.files_dir+file).sheet_by_index(0)
    if file == 'investice-TomasMeisner-2018-08-07.xls':
        for row in range(3, sheet.nrows):
            insertStoryQuery = f"""INSERT INTO stories 
            (amount, date_next_payment, date_secondary_bought, date_secondary_sold_date, date_start, fee) 
                               VALUES ({sheet.cell_value(row, 5)}, "{sheet.cell_value(row, 29)}", "{sheet.cell_value(row, 29)}", "{sheet.cell_value(row, 29)}", "{sheet.cell_value(row, 29)}", {sheet.cell_value(row, 25)})"""
            print(insertStoryQuery)
            dbscripts.db_query(database, insertStoryQuery)

#TODO: Insert date in proper format

database.close()


# amount, date_next_payment, date_secondary_bought, date_secondary_sold_date, date_start, fee, full_payment, installments, installments_when_bought, insurance, interest_rate, my_payment, name, postponed, rating, status, user_id