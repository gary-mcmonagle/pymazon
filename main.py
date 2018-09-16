from email_service.create_service import create_service
from amazon.check_products import check_products
from email_service.analyse_inbox import analyse_inbox
from cosmos.create_cosmos_client import create_cosmos_client
from cosmos.db_init import db_init
from cosmos.get_instance import *

db_client = create_cosmos_client()
try:
    get_db(db_client)
except:
    db_init(db_client)


email_service = create_service()
analyse_inbox(email_service, db_client)
check_products(email_service, db_client)

