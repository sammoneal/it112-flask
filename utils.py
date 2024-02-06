import json


def add_stars(rating, max=5):
  full = round(rating)
  half = False
  if 0.75 > rating % 1 > 0.25:
    half = True
    full -= 1
  result = []
  for i in range(full):
    result.append('<span class="fa fa-star checked"></span>')
  if half:
    result.append('<span class="fa fa-star-half checked"></span>')
  while len(result) < max:
    result.append('<span class="fa fa-star unchecked"></span>')
  return "".join(result)


def movie_stars(movie_dict):
  for item in movie_dict:
    item['stars'] = add_stars(item['rating'])
  return movie_dict


def load_user_data(user_number):
  # Read project data from JSON file
  with open('test.json') as json_file:
    for user in json.load(json_file):
      if user['id'] == user_number:
        return user
    return None
