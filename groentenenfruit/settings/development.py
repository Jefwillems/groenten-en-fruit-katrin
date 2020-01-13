from groentenenfruit.settings.base import *

INSTALLED_APPS = list(filter(lambda x: 'cloudinary' not in x, INSTALLED_APPS))

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
