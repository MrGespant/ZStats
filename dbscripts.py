# initial DB setup

import sqlite3
from sqlite3.dbapi2 import Connection
from resources.secrets import config

def db_init():
    #
    # initialize the connection to DB
    # returns the DB connector
    #

    try:
        db: Connection = sqlite3.connect(config.db_database_location)
    except Exception as e:
        print("DB not connected")
        raise e

    print("DB connection established")
    return db


def db_script_open(script_file):
    #
    # opens the SQL "script_file"
    # returns the full "script" from file
    #

    try:
        fd = open(script_file, 'r')
        script = fd.read()
        fd.close()
    except Exception as e:
        print("Script from file " + script_file + " not loaded")
        raise e

    print("Script from file " + script_file + " loaded")
    return script


def db_query(db, script):
    #
    # runs the queries in "script" on database "db"
    #

    commands = script.split(';')

    for command in commands:
        try:
            results = db.cursor().execute(command).fetchall()
        except Exception as e:
            raise e

    print("Script executed")
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        print("Script rolled back")
        raise e
    return results

def db_create():
    database = db_init()
    db_query(database, db_script_open(config.db_create_script))
    database.close()
