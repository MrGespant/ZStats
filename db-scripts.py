# initial DB setup

import sqlite3
from sqlite3.dbapi2 import Connection
from resources.secrets import config


insert = """INSERT INTO stories (
    id, user_id, name, status, date_start, date_next_payment, date_secondary_bought, date_secondary_sold_date, amount, full_payment, my_payment, installments, installments_when_bought, insurance, postponed, interest_rate, fee, rating
) VALUES (
    1,2,'try','start',NULL,'2018-05-13', NULL, NULL, 10000, 2300, 13.5, 5, NULL, 1, 0, 5.86, 2, 'A++'  
)"""


def db_init():
    # initialize the connection to DB
    try:
        db: Connection = sqlite3.connect(config.db_database_location)
        # TODO ukladat databazi na Drive
    except Exception as e:
        print("DB not connected")
        raise e

    print("DB connection established")
    return db


def db_script_open(query):
    try:
        fd = open(query, 'r')
        sqlFile = fd.read()
        fd.close()
    except Exception as e:
        print("Script " + query + " not loaded")
        raise e

    print("Script " + query + " loaded")
    return sqlFile


def db_query(db, script):

    sqlCommands = script.split(';')

    for command in sqlCommands:
        try:
            db.cursor().execute(command)
        except Exception as e:
            raise e

    print("Script executed")
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        print("Script rollbacked")
        raise e


database = db_init()
db_query(database, db_script_open(config.db_create_script))
db_query(database, insert)
database.close()

