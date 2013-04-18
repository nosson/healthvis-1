
import os
from secret_keys import CSRF_SECRET_KEY, SESSION_KEY

DEBUG_MODE = False

# Auto-set debug mode based on App Engine dev environ
if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    DEBUG_MODE = True

DEBUG = DEBUG_MODE

# Set secret keys for CSRF protection
SECRET_KEY = CSRF_SECRET_KEY
CSRF_SESSION_KEY = SESSION_KEY
CSRF_ENABLED = True

# app configuration goes here
supported_types = ['accuracy_table', 'survival', 'icon_array', 'heatmap', 'paired','dist','cor']
