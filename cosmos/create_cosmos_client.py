import pydocumentdb.document_client as document_client
import os
import constants as constants

def create_cosmos_client():
    config = __get_config()
    return document_client.DocumentClient(config['ENDPOINT'], {'masterKey': config['MASTERKEY']})

def __get_config():
    return {
        'ENDPOINT': os.environ['cosmos_endpoint'],
        'MASTERKEY': os.environ['cosmos_key']
    }
