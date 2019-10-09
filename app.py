from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Home Message')

# OUR MOCK ARRAY OF Store Products
products = [
    { 'title': 'Dragon Kite', 'description': 'Wow dragon' },
    { 'title': 'Bunny Kite', 'description': 'wow bunny' }
]

@app.route('/products')
def products_index():
    """Show all playlists."""
    return render_template('products_index.html', products=products)



if __name__ == '__main__':
    app.run(debug=True)
