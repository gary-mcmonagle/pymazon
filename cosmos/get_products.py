from cosmos.get_instance import get_collection
def get_products(client):
    query = {'query': 'SELECT * FROM server s'}
    options = {}
    options['enableCrossPartitionQuery'] = True
    result_iterable = client.QueryDocuments(get_collection(client)['_self'], query, options)
    return list(result_iterable);