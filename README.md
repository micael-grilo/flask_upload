## Run app with

> `python app.py`

## Run tests with

> `pytest --verbose `

## 2
 - First we would add a database, storing image path and name, so we don't need to try different formats to get the image.
 - Second we would need a fast webserver like Gunicorn running this flask application.
 - Third we could add Jinja cache to speedup templates generation ( altghought in this case the templates are minimal)
 - Last we could use a CDN to destribute images faster

## 3
 - We should create a settings file where we specifiy three classes, one with base settings, other with QA settings and another with Production settings, both QA and Prod settings would by child classes of base class, then we specify correct settings for each enviromnent.

## 4
 - Low traffic scenario: Just add a count +1 in the flask route endpoint that increments the counter in the database.
 - High traffic scenario: Run this counter in a background proccess / new thread.