from imagersite.settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1",
                 "54.202.162.152",
                 "ec2-54-202-162-152.us-west-2.compute.amazonaws.com",
                 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/imagersite/static/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST_USER = 'conor.clary@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS", "")