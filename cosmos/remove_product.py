from cosmos.get_instance import get_collection
def remove_product(client, product_id, recip):
    query = {'query': 'SELECT * FROM server s'}
    options = {}
    options['enableCrossPartitionQuery'] = True
    links = client.QueryDocuments(get_collection(client)['_self'], query, options)
    for idx, link in enumerate(links):
        print(link)
        if link['productId'] == product_id and link['recipient'] == recip:
            client.DeleteDocument(link['_self'])
