"""Defines the Recipe database model
"""
from . import db

class Recipe(db.Model):
    """Recipe model

    Args:
        db (_type_): Database
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    description = db.Column(db.String(200))
    ingredients = db.Column(db.Text)
    instructions = db.Column(db.Text)
    rating = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('recipes', lazy=True))


