# initial DB setup

import sqlite3
from sqlite3.dbapi2 import Connection
from resources.secrets import config


def zstats_db_init():
    try:
        db: Connection = sqlite3.connect(config.db_database_location)
        # TODO ukladat databazi na Drive
    except Exception as e:
        raise e

    print("DB connection established")
    cursor = db.cursor()

    try:
        fd = open(config.db_create_script, 'r')
        sqlFile = fd.read()
        fd.close()
    except Exception as e:
        raise e

    print("Create script loaded")
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except Exception as e:
            raise e

    print("Create script executed")
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        print("Create script rollbacked")
        raise e
    finally:
        db.close()


zstats_db_init()