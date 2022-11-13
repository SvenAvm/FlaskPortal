from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
    db.init_app(app)
    return app


class Product(db.Model):
    product_id = db.Column(db.Integer(), nullable=False, unique=True, primary_key=True)
    product_name = db.Column(db.String(length=30), nullable=False, unique=True)
    product_price = db.Column(db.Float(), nullable=False)
    product_barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    product_description = db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


# Pages


@app.route("/market")
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template("market.html", items=items)


@app.route('/about/<username>')
def about_page(username):
    return f"<h1>This is the about page of {username}</h1>"


@app.route("/ukraine")
def ukraine_page():
    return render_template("ukraine.html")
    pass


@app.route("/jira")
def jira_page():
    return render_template("jira.html")
    pass


@app.route("/stocks")
def stocks_page():
    return render_template("stocks.html")
    pass


@app.route("/crypto")
def crypto_page():
    return render_template("crypto.html")
    pass
