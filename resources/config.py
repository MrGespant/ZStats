# konfiguracni soubor
import logging

FILES_DIR                   = './files/'
DB_CREATE_SCRIPT            = './resources/db-create.sql'
DB_DATABASE_LOCATION        = './resources/secrets/data.db'


logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('ZStats')
