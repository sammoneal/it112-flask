from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .recipe import Recipe
from .category import Category
