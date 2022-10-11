"""Course493 development configuration."""

import pathlib

# root for application
APPLICATION_ROOT = '/'

# project directory
COURSE493_ROOT = pathlib.Path(__file__).resolve().parent.parent

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# db file path
DATABASE_FILENAME = COURSE493_ROOT/'var'/'db.sqlite3'