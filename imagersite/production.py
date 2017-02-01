from settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1",
                 "54.202.162.152",
                 "ec2-54-202-162-152.us-west-2.compute.amazonaws.com",
                 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')