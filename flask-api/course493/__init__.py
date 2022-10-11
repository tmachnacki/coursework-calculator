"""Insta485 package initializer."""
import flask
# from flask_cors import CORS





# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# cors = CORS(app, resources={r"/api": {"origins": "http://localhost:8080"}})


# Read settings from config module (insta485/config.py)
app.config.from_object('course493.config')
app.config['CORS_HEADERS'] = 'Content-Type'


# Overlay settings read from a Python file whose path is set in the environment
# variable INSTA485_SETTINGS. Setting this environment variable is optional.
# Docs: http://flask.pocoo.org/docs/latest/config/
#
# EXAMPLE:
# $ export INSTA485_SETTINGS=secret_key_config.py
app.config.from_envvar('COURSE493_SETTINGS', silent=True)

# Tell our app about api and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.


import course493.api  # noqa: E402  pylint: disable=wrong-import-position
import course493.model  # noqa: E402  pylint: disable=wrong-import-position
