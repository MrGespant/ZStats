# This script should parse given XLS file and fill the database with included data
#
#

import xlrd
import dbscripts
from resources.secrets import config
from os import listdir
from datetime import datetime

database = dbscripts.db_init()

for file in listdir(config.files_dir):
    # store import file information
    insertFileQuery = f"""INSERT INTO files (filename, date_processed) 
                          VALUES ("{file}", "{file[23:-4]}")"""
    dbscripts.db_query(database, insertFileQuery)

    sheet = xlrd.open_workbook(config.files_dir+file).sheet_by_index(0)
    if file == 'investice-TomasMeisner-2018-08-07.xls':
        for row in range(3, sheet.nrows):
            sheet.cell_value(row, 0)
            sheet.cell_value(row, 1)
            sheet.cell_value(row, 2)
            storyId = sheet.cell_value(row, 3)
            if sheet.cell_value(row, 4) != "":
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(sheet.cell_value(row, 4), 0)
                dateStart = str(year) + "-" + str(month) + "-" + str(day)
            else:
                dateStart = ""
            sheet.cell_value(row, 5)
            sheet.cell_value(row, 6)
            sheet.cell_value(row, 7)
            sheet.cell_value(row, 8)
            sheet.cell_value(row, 9)
            sheet.cell_value(row, 10)
            sheet.cell_value(row, 11)
            sheet.cell_value(row, 12)
            sheet.cell_value(row, 13)
            sheet.cell_value(row, 14)
            sheet.cell_value(row, 15)
            sheet.cell_value(row, 16)
            sheet.cell_value(row, 17)
            sheet.cell_value(row, 18)
            sheet.cell_value(row, 19)
            sheet.cell_value(row, 20)
            sheet.cell_value(row, 21)
            sheet.cell_value(row, 22)
            sheet.cell_value(row, 23)
            sheet.cell_value(row, 24)
            sheet.cell_value(row, 25)
            sheet.cell_value(row, 26)
            sheet.cell_value(row, 27)
            sheet.cell_value(row, 28)
            if sheet.cell_value(row,29) != "":
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(sheet.cell_value(row, 29), 0)
                dateNextPayment = str(year) + "-" + str(month) + "-" + str(day)
            else:
                dateNextPayment = ""
            if sheet.cell_value(row,30) != "":
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(sheet.cell_value(row, 30), 0)
                dateSecondaryBought = str(year) + "-" + str(month) + "-" + str(day)
            else:
                dateSecondaryBought= ""
            if sheet.cell_value(row,31) != "":
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(sheet.cell_value(row, 31), 0)
                dateSecondarySoldDate = str(year) + "-" + str(month) + "-" + str(day)
            else:
                dateSecondarySoldDate = ""
            insertStoryQuery = f"""INSERT INTO stories 
            (amount, date_next_payment, date_secondary_bought, date_secondary_sold_date, date_start, fee, id) 
                               VALUES ({sheet.cell_value(row, 5)}, "{dateNextPayment}", "{dateSecondaryBought}", "{dateSecondarySoldDate}", "{dateStart}", {sheet.cell_value(row, 25)}, {storyId})"""
            print(insertStoryQuery)
            dbscripts.db_query(database, insertStoryQuery)

#TODO: Insert date in proper format

database.close()


# amount, date_next_payment, date_secondary_bought, date_secondary_sold_date, date_start, fee, full_payment, installments, installments_when_bought, insurance, interest_rate, my_payment, name, postponed, rating, status, user_id