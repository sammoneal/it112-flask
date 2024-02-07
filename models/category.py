"""Defines the Category database model
"""
from . import db


class Category(db.Model):
    """Category model

    Args:
        db (_type_): Database
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
