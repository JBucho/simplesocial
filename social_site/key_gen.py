import os
from django.core.management.utils import get_random_secret_key

SECRET_KEY = '3e7#nuv5uj+$)e07m(8%+hy0w_sl0=o4@w+kdacu+m+j$a3th#'
SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))

def generate_secret_key():
    with open(os.path.join(SETTINGS_DIR, '.secret_key.'), 'w') as kf:
        kf.write('\'' + SECRET_KEY + '\'')
