from pymongo import MongoClient
from bson.objectid import ObjectId

product_1 = {
    'title': 'Bird Kite',
    'price': 27.99,
    'description': "Flying beautifully in the sky.",
    'image': "/static/birdkite.jpg"
}

product_2 = {
    'title': 'Butterfly Kite',
    'price': 18.99,
    'description': "So beauitful yet so fragile.",
    'image': "/static/butterkite2.jpg"
}

product_3 = {
    'title': 'Rainbow Kite',
    'price': 19.99,
    'description': "For all your colorful wants and needs.",
    'image': "/static/lgbtkite.jpg"
}

product_4 = {
    'title': 'Snake Kite',
    'price': 14.95,
    'description': "Slithering through the night sky.",
    'image': "/static/snakekite.jpg"
}

product_5 = {
    'title': 'Dragon Kite',
    'price': 61.95,
    'description': "A dragon, what else could you ask for.",
    'image': "/static/dragonkite.jpg"
}

product_list = [product_1, product_2, product_3, product_4, product_5]

class createProducts():
    def __init__(self, products):
        self.products = products

    def create_database(self):
        #Clearing and then adding database
        self.products.delete_many({})
        self.products.insert_many(product_list)
