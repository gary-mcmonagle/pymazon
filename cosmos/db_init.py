import constants as Constants
def db_init(client):
    db = client.CreateDatabase({'id': Constants.COSMOS_DB})
    options = {
        'offerEnableRUPerMinuteThroughput': True,
        'offerVersion': "V2",
        'offerThroughput': 400
    }
    client.CreateCollection(db['_self'], {'id': Constants.COSMOS_COLL}, options)
