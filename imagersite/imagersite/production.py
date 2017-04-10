from imagersite.settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1",
                 "54.245.7.225", "54.202.162.152",
                 "ec2-54-202-162-152.us-west-2.compute.amazonaws.com",
                 'localhost', "ec2-54-245-7-225.us-west-2.compute.amazonaws.com"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'imagersite', 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'MEDIA')
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_PASSWORD = 'somestupidwordpass'
EMAIL_HOST_USER = 'codefellowsdjango401imager@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = 'codefellowsdjango401imager@gmail.com'
DEFAULT_FROM_EMAIL = 'SOURCE SHOT IMAGER SITE BRO. TROLLPY'
