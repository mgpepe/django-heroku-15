Blank Django Project on Heroku in 15m
=====================================

> 1. OSX only
> 2. If you have better/faster ways, let me know

Files Setup
-----------

Change to where your project will be

    cd ~

Fork this repository `https://github.com/mgpepe/django-heroku-15`

    git clone YOUR_FORKED_REPOSITORY

You may rename the 'django-heroku-15' folder to anything you like:

    mv django-heroku-15 YOUR_PROJECT_NAME

Database Prerequisites
--------------------------------

Just before we continue, we will install postgres.app. Grab and install from: http://postgresapp.com/


Virtual Environment
-----------------------

If you don’t have virtualenv, you need to get it. It will allow you to have separate installations of software for each project:

    pip install virtualenv
    
Then we start the fun:

    cd django-heroku-15
    virtualenv venv
    source venv/bin/activate
    PATH=/Applications/Postgres.app/Contents/MacOS/bin/:$PATH

Now install all we need:

    pip install -r requirements.txt

And test that we have Django:

    python -c "import django; print(django.get_version())"

Database
--------

    createdb YOUR_DATABASE_NAME --owner=YOUR_OSX_USERNAME
    
Change in your `settings.py` the database part tool something like that:
    
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

Change the `SECRET_KEY` variable while you are there.

In terminal run this command to create databases and setup your admin user:

    python manage.py syncdb

Heroku Multiple Accounts & SSH Keys
-----------------------------------

[ OPTIONAL ] To create a new ssh KEY:

    ssh-keygen -t rsa
    
When asked for name, write the full path and name as shown. then type your password or leave blank.

[ END OPTIONAL ]

Even if you never have to have multiple heroku accounts, it is an easy way to setup and use it even for one account. So on we go:

    cd ~
    heroku plugins:install git://github.com/ddollar/heroku-accounts.git
    
the add a heroku account with:

1. `heroku accounts:add personal`
2. Type in your Heroku login email
3. Type in your Herokku login password

Then it says it and you should add the following to your `~/.ssh/config`:

    Host heroku.personal
        HostName heroku.com
        IdentityFile /PATH/TO/PRIVATE/KEY
        IdentitiesOnly yes

Go to your project folder with (if you did rename your project folder, use your name here):

    cd ~/django-heroku-15
    
and then set the new account as:

    heroku accounts:set personal

Finally add the keys both to your OSX and heroku:

    heroku keys:add  ~/.ssh/YOUR_KEY_NAME.pub
    ssh-add ~/.ssh/YOUR_KEY_NAME

Deploy to Heroku
----------------

Now that everything is in order, you should be able to see all your Heroku Apps:

    heroku apps
    
To create one for your project:

    heroku apps:create YOUR_APP_NAME

To deploy files to Heroku:

    git push heroku master
    
And then create the database and admin user with:

    heroku run python manage.py syncdb
    
Now if you go to `YOUR_APP_NAME.herokuapp.com` to see your site. You are all set!
