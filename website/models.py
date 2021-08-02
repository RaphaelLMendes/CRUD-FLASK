from . import db
from sqlalchemy.sql import func

# creating model to interact with DB
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

