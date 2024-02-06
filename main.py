import os, json
from flask import Flask, render_template, url_for, request
from utils import movie_stars

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY',
                                          'default_secret_key')

MOVIE_DATA = [{
    'title': 'Toy Story',
    'genre': 'Animation',
    'rating': 5,
}, {
    'title': 'Finding Nemo',
    'genre': 'Animation',
    'rating': 4.5,
}, {
    'title': 'Monsters, Inc.',
    'genre': 'Animation',
    'rating': 4.5,
}, {
    'title': 'Cars',
    'genre': 'Animation',
    'rating': 3,
}, {
    'title': 'Cars 2',
    'genre': 'Animation',
    'rating': 2,
}]

rated_movies = movie_stars(MOVIE_DATA)


@app.route('/')
def index():
  title = 'Jinja Home'
  return render_template('index.html', title=title)


@app.route('/about')
def about():
  title = 'About Jinja'
  return render_template('about.html', title=title)


@app.route('/hipster')
def hipster():
  title = 'Hipster Page'
  return render_template('hipster.html', title=title)


@app.route('/pirate')
def pirate():
  title = 'Pirate Page'
  return render_template('pirate.html', title=title)


@app.route('/movies')
def movies():
  payload = {
      'title': 'Pixar Movies',
      'movies': rated_movies,
  }
  return render_template('movies.html', **payload)


@app.route('/register', methods=['GET', 'POST'])
def register():
  title = "Register"
  feedback = None
  if request.method == 'POST':
    feedback = register_data(request.form)
  payload = {"title": title, "feedback": feedback}
  return render_template('register.html', **payload)


def register_data(form_data):
  feedback = []
  for key, value in form_data.items():
    if key.endswith("[]"):
      value = ', '.join(request.form.getlist(key))
      key = key[:-2]
    if key in ['First_Name', 'Last_Name', 'Address', 'City']:
      value = value.title()
    feedback.append(f"{key.replace('_',' ')}: {value}")
  return feedback


@app.route('/users')
def users():
  with open('test.json') as json_file:
    user_data = json.load(json_file)
  payload = {
      'title': 'Users',
      'users': user_data,
  }
  return render_template('users.html', **payload)


@app.route('/user/<int:id>')
def user(id):
  with open('test.json') as json_file:
    user_data = json.load(json_file)
    try:
      this_user = user_data[id]
    except IndexError:
      return 'User not found', 404
  context = {"title": "User", "user": this_user}
  return render_template("user.html", **context)


def load_user_data(user_number):
  # Read project data from JSON file
  with open('test.json') as json_file:
    users = json.load(json_file)
    for user in users:
      if user['id'] == user_number:
        return user
    return None


app.run(host='0.0.0.0', port=81)
