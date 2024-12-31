from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ANY changes to the database, should do a migration.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    title = db.Column(db.String(140), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    image_id = db.Column(db.String(140), nullable=True)
    
    def __repr__(self):
        return f'<Message {self.id} from {self.user_name}>'
    
# FoodPrint Section
class FoodPrint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String(80), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'<FoodPrint {self.id} from {self.county}>'
    
class NightMarkets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    part = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    operating_days = db.Column(db.String(50), nullable=True)