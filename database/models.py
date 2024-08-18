from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    content = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    image_id = db.Column(db.String(140), nullable=True)
    
    def __repr__(self):
        return f'<Message {self.id} from {self.user_name}>'
    
