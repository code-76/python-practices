DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the path of the database file
SQLALCHEMY_DATABASE = os.path.join(BASE_DIR, 'database/app.db')

HOST = "0.0.0.0"

PORT = os.environ.get("PORT", 8080)