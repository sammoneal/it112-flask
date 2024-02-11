import os, json
from flask import Flask, render_template, url_for, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Recipe, Category
from utils import movie_stars
from default_data import create_default_data

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "default_secret_key")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"
db.init_app(app)

MOVIE_DATA = [
    {
        "title": "Toy Story",
        "genre": "Animation",
        "rating": 5,
    },
    {
        "title": "Finding Nemo",
        "genre": "Animation",
        "rating": 4.5,
    },
    {
        "title": "Monsters, Inc.",
        "genre": "Animation",
        "rating": 4.5,
    },
    {
        "title": "Cars",
        "genre": "Animation",
        "rating": 3,
    },
    {
        "title": "Cars 2",
        "genre": "Animation",
        "rating": 2,
    },
]

rated_movies = movie_stars(MOVIE_DATA)


@app.route("/")
def index():
    title = "Jinja Home"
    return render_template("index.html", title=title)


@app.route("/about")
def about():
    title = "About Jinja"
    return render_template("about.html", title=title)


@app.route("/hipster")
def hipster():
    title = "Hipster Page"
    return render_template("hipster.html", title=title)


@app.route("/pirate")
def pirate():
    title = "Pirate Page"
    return render_template("pirate.html", title=title)


@app.route("/movies")
def movies():
    payload = {
        "title": "Pixar Movies",
        "movies": rated_movies,
    }
    return render_template("movies.html", **payload)


@app.route("/register", methods=["GET", "POST"])
def register():
    title = "Register"
    feedback = None
    if request.method == "POST":
        feedback = register_data(request.form)
    payload = {"title": title, "feedback": feedback}
    return render_template("register.html", **payload)


def register_data(form_data):
    feedback = []
    for key, value in form_data.items():
        if key.endswith("[]"):
            value = ", ".join(request.form.getlist(key))
            key = key[:-2]
        if key in ["First_Name", "Last_Name", "Address", "City"]:
            value = value.title()
        feedback.append(f"{key.replace('_',' ')}: {value}")
    return feedback


@app.route("/users")
def users():
    with open("test.json") as json_file:
        user_data = json.load(json_file)
    payload = {
        "title": "Users",
        "users": user_data,
    }
    return render_template("users.html", **payload)


@app.route("/user/<int:user_id>")
def user(user_id):
    with open("test.json") as json_file:
        user_data = json.load(json_file)
        try:
            id = user_id - 1
            this_user = user_data[id]
        except IndexError:
            return render_template("404.html", title="404")
    context = {"title": "User", "user": this_user}
    return render_template("user.html", **context)


@app.route("/recipes")
def recipes():
    all_recipes = Recipe.query.all()
    title = "Recipes"
    context = {"title": title, "recipes": all_recipes}
    return render_template("recipes.html", **context)


@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    this_recipe = Recipe.query.get(recipe_id)
    context = {"title": "Recipe", "recipe": this_recipe}
    if this_recipe:
        return render_template("recipe.html", **context)
    else:
        return render_template("404.html", title="404")


with app.app_context():
    db.create_all()
    create_default_data(db, Recipe, Category)

class RecipeView(ModelView):
  column_searchable_list = ['name', 'author']

admin = Admin(app)
admin.url = '/admin/' #would not work on repl w/o this!
admin.add_view(RecipeView(Recipe, db.session))
admin.add_view(ModelView(Category, db.session))



app.run(host="0.0.0.0", port=81, debug=True)
