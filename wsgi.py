# PythonAnywhere WSGI configuration
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/Animepahe-API-main'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import the FastAPI app
from main import app

# ASGI application
application = app
