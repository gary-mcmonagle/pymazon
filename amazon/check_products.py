from amazon.get_item_details import get_item_details
from cosmos.get_products import get_products
from email_service.send import *

def check_products(email_service, db_client):
    mails = __create_mail_dict(db_client)
    for key, value in mails.items():
        message_body = ""
        for idx, product in enumerate(value):
            message_body += "NAME: " + product["name"] + "\n"
            message_body += "PRICE: " + str(product["sale_price"]) + "\n"
            message_body += "URL: " + product["url"] + "\n"
            message_body += "\n\n\n"
        if(len(value) > 1):
            subject = "{0} Offers Available on Amazon".format(len(value))
        else:
            subject = "{0} Available At {1}".format(value[0]["name"], value[0]["sale_price"])
        send_message(email_service,
                     create_message("pymazon@gmail.com", key, subject, message_body))

def __get_live_details(db_client):
    products = get_products(db_client)
    for idx, product in enumerate(products):
        check = get_item_details(product['productId'])
        if check:
            product["sale_price"] = float(check["SALE_PRICE"][1:])
            product["url"] = check["URL"]
            product["name"] = check["NAME"]
        else:
            product["sale_price"] = None
            product["url"] = None
            product["name"] = None
    return products

def __get_deals(products):
    products = filter(lambda prod: prod["sale_price"] and prod["url"] and prod["name"], products)
    products = list(filter(lambda prod: prod["sale_price"] <= prod["target_price"], products))
    return products

def __create_mail_dict(db_client):
    mails = {}
    deals = __get_deals(__get_live_details(db_client))
    for idx, deal in enumerate(deals):
        if(not deal['recipient'] in mails):
            mails[deal['recipient']] = []
        mails[deal['recipient']].append(deal)
    return mails

