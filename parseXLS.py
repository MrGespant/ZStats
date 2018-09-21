# This script should parse given XLS file and fill the database with included data
#
#

import xlrd
import sqlite3

path = "./files/investice-TomasMeisner-2018-09-21.xls"
# TODO soubor jako vstupni parametr

sheet = xlrd.open_workbook(path).sheet_by_index(0)
# TODO projit soubor a ulozit data jednotlivych pribehu

try:
    db = sqlite3.connect("./data.db")
    # TODO ukladat databazi na Drive
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS stories(id INTEGER PRIMARY KEY,sum INTEGER)''')
    db.commit()

    cursor.execute('''INSERT INTO stories(sum) VALUES(?)''', sheet.nrows)
    db.commit()

except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()
