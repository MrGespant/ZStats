# This script should parse given XLS file and fill the database with included data
#
#

import xlrd
import dbscripts
from resources.secrets import config
from os import listdir

database = dbscripts.db_init()
processedFiles = dbscripts.db_query(database, "SELECT filename FROM files")
processedStories = dbscripts.db_query(database, "SELECT id FROM stories")


for file in listdir(config.files_dir):
    # check if the file is not processed already
    if [item for item in processedFiles if file in item]:
        print(file + " already there")
        continue
    print("processing file " + file)

    # mark that this file was processed
    insertFileQuery = f"""INSERT INTO files (filename, date_processed) 
                          VALUES ("{file}", "{file[23:-4]}")"""
    dbscripts.db_query(database, insertFileQuery)
    print(file + " marked as processed")

    # process file
    sheet = xlrd.open_workbook(config.files_dir+file).sheet_by_index(0)
    for row in range(3, sheet.nrows):
        userID = sheet.cell_value(row, 0)
        name = sheet.cell_value(row, 1).replace('"', '')
        status = sheet.cell_value(row, 2)
        storyId = sheet.cell_value(row, 3)
        if sheet.cell_value(row, 4) != "":
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(sheet.cell_value(row, 4), 0)
            dateStart = str(year) + "-" + str(month) + "-" + str(day)
        else:
            dateStart = ""
        amount = sheet.cell_value(row, 5)
        fullPayment = sheet.cell_value(row, 6)
        myPayment = sheet.cell_value(row, 7)
        remainingInstallments = sheet.cell_value(row, 8)
        if sheet.cell_value(row, 9) == "Ne":
            insurance = 0
        else:
            insurance = 1
        if sheet.cell_value(row, 10) == "Ne":
            postponed = 0
        else:
            postponed = 1
        originalInvestment = sheet.cell_value(row, 11)
        principalInvestment = sheet.cell_value(row, 12)
        principalPaid = sheet.cell_value(row, 13)
        principalRemaining = sheet.cell_value(row, 14)
        principalSold = sheet.cell_value(row, 15) or 0
        principalSellFee = sheet.cell_value(row, 16) or 0
        principalLate = sheet.cell_value(row, 17)
        interestExpected = sheet.cell_value(row, 18)
        interestPaid = sheet.cell_value(row, 19)
        interestRemaining = sheet.cell_value(row, 20)
        interestLate = sheet.cell_value(row, 21)
        penalty = sheet.cell_value(row, 22)
        interestRate = sheet.cell_value(row, 23)
        rating = sheet.cell_value(row, 24)
        fee = sheet.cell_value(row, 25)
        currentInstallments = sheet.cell_value(row, 26)
        originalInstallments = sheet.cell_value(row, 27)
        installmentsWhenBought = sheet.cell_value(row, 28) or 0
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

        # check if the story is already in database
        if not [item for item in processedStories if storyId in item]:
            insertStoryQuery = f"""INSERT INTO stories 
        (id, user_id, name, date_start, date_secondary_bought, date_secondary_sold_date, amount, full_payment, my_payment, original_installments, installments_when_bought, insurance, interest_rate, fee, rating) 
        VALUES ({storyId}, "{userID}", "{name}", "{dateStart}", "{dateSecondaryBought}", "{dateSecondarySoldDate}", {amount}, {fullPayment}, {myPayment}, {originalInstallments}, {installmentsWhenBought},{insurance},{interestRate},{fee}, "{rating}")"""
            dbscripts.db_query(database, insertStoryQuery)
            print("Adding story " + str(storyId))
        else:
            print("Skipping story " + str(storyId))

        insertHistoryQuery = f"""INSERT INTO history 
        (story_id, status, date_transaction, date_next_payment, remaining_installments, current_installments, original_investment, principal_investment, principal_paid, principal_remaining, principal_sold, principal_late, principal_sell_fee, interest_expected, interest_paid, interest_remaining, interest_late, postponed, penalty ) 
        VALUES ({storyId},"{status}", "{file[23:-4]}", "{dateNextPayment}", {remainingInstallments}, {currentInstallments}, {originalInvestment}, {principalInvestment}, {principalPaid}, {principalRemaining}, {principalSold},{principalLate},{principalSellFee},{interestExpected}, {interestPaid}, {interestRemaining}, {interestLate}, {postponed}, {penalty})"""
        dbscripts.db_query(database, insertHistoryQuery)
        print("Adding history for story " + str(storyId))

database.close()


