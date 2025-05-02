from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    lot = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    buy_price = db.Column(db.Float)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    lot = db.Column(db.String(50))
    quantity_sold = db.Column(db.Float)
    sell_price = db.Column(db.Float)
    profit = db.Column(db.Float)

def init_db(app):
    with app.app_context():
        db.create_all()
        if not User.query.first():
            admin = User(username='admin', password='admin123')
            db.session.add(admin)
            db.session.commit()
