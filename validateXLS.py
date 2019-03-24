import xlrd
from resources import config

def validate(file):
    #
    # validates "file"
    # returns True or False base on validation result
    #

    sheet = xlrd.open_workbook(config.FILES_DIR + file).sheet_by_index(0)
    if sheet.cell_value(1, 0) != 'ID klienta':
        config.logger.error("'ID klienta' not valid against " + sheet.cell_value(1, 0))
        return False
    if sheet.cell_value(1, 1) != 'Název':
        config.logger.error("'Název' not valid against " + sheet.cell_value(1, 1))
        return False
    if sheet.cell_value(1, 1) != 'Stav':
        config.logger.error("'Stav' not valid against " + sheet.cell_value(1, 2))
        return False
    if sheet.cell_value(1, 1) != 'ID příběhu':
        config.logger.error("'ID příběhu' not valid against " + sheet.cell_value(1, 3))
        return False
    if sheet.cell_value(1, 1) != 'Datum zafinancování':
        config.logger.error("'Datum zafinancování' not valid against " + sheet.cell_value(1, 4))
        return False

    config.logger.info(file + " is valid")
    return False
