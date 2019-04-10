from flask_migrate import Migrate
from LeagueOfLogsWebServer.py import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
