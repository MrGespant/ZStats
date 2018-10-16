# This script should parse given XLS file and fill the database with included data
#
#
from sqlite3.dbapi2 import Connection

import xlrd
import sqlite3
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# you have to get client_secrets.json file from Google API Console and save it in root
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt'})
file1.SetContentString('Hello')
file1.Upload()

path = "./files/investice-TomasMeisner-2018-09-21.xls"
# TODO soubor jako vstupni parametr

sheet = xlrd.open_workbook(path).sheet_by_index(0)
# TODO projit soubor a ulozit data jednotlivych pribehu

