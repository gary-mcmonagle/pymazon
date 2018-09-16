import constants as constants
def get_db(client):
    return client.ReadDatabase("dbs/{}".format(constants.COSMOS_DB))
def get_collection(client):
    return client.ReadCollection("dbs/{}/colls/{}".format(constants.COSMOS_DB, constants.COSMOS_COLL))