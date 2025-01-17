from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from create_products import createProducts
from static import *
import os


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
products = db.products
reviews = db.reviews
wish_list = db.wish_list

#Clears Database and Adds Static Objects
kites = createProducts(products)
kites.create_database()

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html')

@app.route('/products')
def products_index():
    """Show all products."""
    return render_template('products_index.html', products=products.find())

@app.route('/products/new')
def products_new():
    """Create a new product."""
    return render_template('products_new.html', product={}, title='New Product')

@app.route('/products', methods=['POST'])
def products_submit():
    """Submit a new product."""
    product = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'images': request.form.get('images').split(),
        'price': request.form.get('price')
    }
    product_id = products.insert_one(product).inserted_id
    return redirect(url_for('products_show', product_id=product_id))

@app.route('/products/<product_id>')
def products_show(product_id):
    """Show a single product."""
    product = products.find_one({'_id': ObjectId(product_id)})
    product_reviews = reviews.find({'product_id': ObjectId(product_id)})
    return render_template('products_show.html', product=product, reviews=product_reviews)

@app.route('/products/<product_id>/edit')
def products_edit(product_id):
    """Show the edit form for a product."""
    product = products.find_one({'_id': ObjectId(product_id)})
    return render_template('products_edit.html', product=product, title='Edit Product')

@app.route('/products/<product_id>', methods=['POST'])
def products_update(product_id):
    """Submit an edited product."""
    updated_product = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'images': request.form.get('images').split(),
        'price': request.form.get('price')
    }
    products.update_one(
        {'_id': ObjectId(product_id)},
        {'$set': updated_product})
    return redirect(url_for('products_show', product_id=product_id))

@app.route('/products/<product_id>/delete', methods=['POST'])
def products_delete(product_id):
    """Delete one product."""
    products.delete_one({'_id': ObjectId(product_id)})
    return redirect(url_for('products_index'))

@app.route('/products/reviews', methods=['POST'])
def reviews_new():
    """Submit a new review."""
    review = {
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'product_id': ObjectId(request.form.get('product_id'))
    }
    review_id = reviews.insert_one(review).inserted_id
    return redirect(url_for('products_show', product_id=request.form.get('product_id')))

@app.route('/products/reviews/<review_id>', methods=['POST'])
def reviews_delete(review_id):
    """Action to delete a review."""
    review = reviews.find_one({'_id': ObjectId(review_id)})
    reviews.delete_one({'_id': ObjectId(review_id)})
    return redirect(url_for('products_show', product_id=review.get('product_id')))

@app.route('/wishlist')
def wish_list_index():
    """Show Wish List."""
    return render_template('wish_list.html', wish_list=wish_list.find())

@app.route('/products/<product_id>/wish', methods=['POST'])
def wish_list_add(product_id):
    """Adds wish to wishlist."""
    add_wish = {
        'product_id': product_id,
        'name': products.find_one({'_id': ObjectId(product_id)})['title'],
        'description': products.find_one({'_id': ObjectId(product_id)})['description'],
        'price': products.find_one({'_id': ObjectId(product_id)})['price']
    }
    wish_list.insert_one(add_wish)
    return redirect(url_for('products_show', product_id=product_id))

@app.route('/products/<product_id>/wish/delete', methods=['POST'])
def wish_delete(product_id):
    """Deletes wish from wishlist."""
    wish_list.delete_one({'_id': ObjectId(product_id)})
    return render_template('wish_list.html', wish_list=wish_list.find())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
