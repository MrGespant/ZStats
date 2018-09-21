# This script should parse given XLS file and fill the database with included data
#
#

import xlrd

path = "./files/investice-TomasMeisner-2018-09-21.xls"
#TODO soubor jako vstupni parametr

sheet = xlrd.open_workbook(path).sheet_by_index(0)
#TODO projit soubor a ulozit data jednotlivych pribehu

print(sheet.nrows)
