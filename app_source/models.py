from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app
# Create database connection object
db = SQLAlchemy(app)


# class Content(db.Model):
#     id = db.Column(db.String(10), primary_key=True)
#     description = db.Column(db.S, nullable=False)
#     gender = db.Column(db.Enum(Gender), nullable=False)
#
#     def __init__(self, description, gender):
#         self.description = description
#         self.gender = gender
#
#
# def init_db():
#     db.drop_all()
#     db.create_all()
#     db.session.add(Content("THIS IS SPARTAAAAAAA!!!", Gender['male']))
#     db.session.add(Content("What's your favorite scary movie?", Gender['female']))
#     db.session.commit()
#     lg.warning('Database initialized!')
