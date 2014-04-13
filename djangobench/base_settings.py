ALLOWED_HOSTS = ['*']

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}

SECRET_KEY = "NOT REALLY SECRET"
