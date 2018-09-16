from cosmos.get_instance import get_collection
def add_product(client, product_id, recipient, target_price):
    client.CreateDocument(get_collection(client)['_self'],
                         {
                             'productId': product_id,
                             'recipient':recipient,
                             'target_price':target_price
                         })
