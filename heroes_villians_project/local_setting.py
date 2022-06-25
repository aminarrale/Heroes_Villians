# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_mhbfq&w5-#&71zme!i^39(bwfq@w#!3hf5$jx-!f1kjsq&z#w'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroesvillians_database',
        'HOST' : 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}
