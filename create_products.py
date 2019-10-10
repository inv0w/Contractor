from pymongo import MongoClient
from bson.objectid import ObjectId

product_1 = {
    'name': 'Standard Hawaii Sock',
    'price': 27.99,
    'description': "Your go-to sock when travelling to the tropics",
    'images': "/static/birdkite1.jpg"
}

product_2 = {
    'name': 'Standard Hawaii Sock',
    'price': 18.99,
    'description': "Your go-to sock when travelling to the tropics",
    'images': "/static/butterkite1.jpg"
}

product_3 = {
    'name': 'Standard Hawaii Sock',
    'price': 19.99,
    'description': "Your go-to sock when travelling to the tropics",
    'images': "/static/lgbtkite.jpg"
}

product_4 = {
    'name': 'Standard Hawaii Sock',
    'price': 14.95,
    'description': "Your go-to sock when travelling to the tropics",
    'images': "/static/snakekite.jpg"
}

product_5 = {
    'name': 'Standard Hawaii Sock',
    'price': 21.95,
    'description': "Your go-to sock when travelling to the tropics",
    'images': "/static/butterkite3.jpg"
}

product_list = [product_1, product_2, product_3, product_4, product_5]

class createProducts():
    def __init__(self, products):
        self.products = products

    def create_database(self):
        #Clearing and then adding database
        self.products.delete_many({})
        self.products.insert_many(product_list)
