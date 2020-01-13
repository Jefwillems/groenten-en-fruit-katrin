from groentenenfruit.settings.base import *
import django_heroku

django_heroku.settings(locals())

DEBUG = False
ALLOWED_HOSTS = ['groentenenfruit.herokuapp.com']
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
