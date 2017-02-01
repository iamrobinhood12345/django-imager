from imagersite.settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1",
                 "54.202.162.152",
                 "ec2-54-202-162-152.us-west-2.compute.amazonaws.com",
                 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static', 'imagersite')]

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS", "")
EMAIL_HOST_USER = 'conor.clary@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
