from groentenenfruit.settings.base import *

INSTALLED_APPS = list(filter(lambda x: 'cloudinary' not in x, INSTALLED_APPS))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
