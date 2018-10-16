# initial DB setup

import sqlite3
from sqlite3.dbapi2 import Connection
import config

try:
    db: Connection = sqlite3.connect("./resources/data.db")
    # TODO ukladat databazi na Drive
except Exception as e:
    raise e

cursor = db.cursor()

try:
    fd = open(config.db_create_filename, 'r')
    sqlFile = fd.read()
    fd.close()
except Exception as e:
    raise e

sqlCommands = sqlFile.split(';')

for command in sqlCommands:
    try:
        cursor.execute(command)
    except Exception as e:
        raise e

try:
    db.commit()
except Exception as e:
    db.rollback()
    raise e
finally:
    db.close()
