django-heroku-15
================

ALL FILES
cd ~

fork my repository https://github.com/mgpepe/django-heroku-15

git clone YOUR_FORKED_REPOSITORY

rename the 'django-heroku-15' folder to anything you like:

mv django-heroku-15 YOUR_PROJECT_NAME

DATABASE
cd YOUR_PROJECT_NAME
virtualenv venv
source venv/bin/activate
PATH=/Applications/Postgres.app/Contents/MacOS/bin/:$PATH

INSTALLATIONS
pip install -r requirements.txt

python -c "import django; print(django.get_version())"

DATABASE
createdb YOUR_DATABASE_NAME --owner=YOUR_OSX_USERNAME

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOUR_DATABASE_NAME',
        'USER': 'YOUR_OSX_USERNAME',
        'PASSWORD': 'YOUR_DATABASE_PASSWORD', #might be empty string ''
        'HOST': '127.0.0.1',
        # 'PORT': '5432',
    }
}

SECRET KEY change.

MULTIPLE HEROKU ACCOUNTS & KEYS all instructions

python manage.py syncdb
