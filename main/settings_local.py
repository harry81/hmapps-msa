import os
import dj_database_url

try:
    from .settings import *
except:
    pass

DEBUG=True
INTERNAL_IPS = ['localhost', '127.0.0.1']
# MIDDLEWARE_CLASSES = ['debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE_CLASSES

# harry
REGION_NAME = 'ap-northeast-2'

AWS_ACCESS_KEY_ID = 'AKIAI5HM4USLX6B5RN5Q'
AWS_SECRET_ACCESS_KEY = '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'

# KaKao
SOCIAL_AUTH_KAKAO_KEY = '6901c2a574288db8a31dbe3e2ed5dae4'
SOCIAL_AUTH_KAKAO_SECRET = 'd8a1fb91acb39634edb33dfbed834609'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '221879398254081'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b0d2caec244b2844071eaebc6a252b76'

# Navere
SOCIAL_AUTH_NAVER_KEY = 'mAGsI5imdDqwwg8LwhJH'
SOCIAL_AUTH_NAVER_SECRET = '58rX8bWARl'

SESSION_COOKIE_SECURE = False

GCM_SERVER_KEY = "AIzaSyC1sfs2qJGrWiMXvYyHD5QG5AM5HoPbLo4"


DATABASES = {
    'local': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hmapps',
        'USER': 'psql_user',
        'PASSWORD': 'psql_pw',
        'HOST': 'localhost',
        'PORT': '5432'
        },
 }

# DATABASE_URL='postgis://myapps:pw-myapps@ebdb.cvwezlg0tpcz.ap-northeast-2.rds.amazonaws.com:5432/ebdb'
# DATABASES['live'] = dj_database_url.config(default=DATABASE_URL)
DATABASES['default'] = DATABASES['local']


RAVEN_CONFIG = {
    'dsn': 'https://685b68704634462ebd2b855d94f39bf6:986abe1900264a6f9649c555d562efb3@sentry.io/127326',
}

BROKER_URL = 'amqp://guest:guest@localhost:5672//'
BROKER_TRANSPORT = 'amqp'


CORS_ORIGIN_ALLOW_ALL = True

SMS_APPID = 'healworld'
SMS_APIKEY = '7bac7074dbca11e6a8a30cc47a1fcfae'

EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_HOST_USER = 'AKIAIQEFFMX2FSEGXNQQ'
EMAIL_HOST_PASSWORD = 'Aqiaws0BmIlnN6bz/kS/zRc0ZXwjsS3jowEGR27MgzhJ'

# SENDGRID
SENDGRID_API_KEY = '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'

DAUM_API_KEY = '192b2926e537f29221262d4c390b485a'
DAUM_API_KEY = '9f68e425f40e190b407745eb855619262ce0b2cc'

DATA_GO_KR_KEY1 = "auRRfe7N35QzfgB8TuK41hLH+sjwp8Vp7Q4ot8VaoRsnA0qsPHX65GonUcnkKfRzkBPdYz2h7llYNLRo19RJ2w=="
DATA_GO_KR_KEY2 = "HRcQAivxWMAZj51AONvOczzjc8EsILOHGOKF1oZpvyH5VFW2Hdj9I/HQK7SaPtkMPGS3HOlgRs6W4TBOqf+2sg=="
DATA_GO_KR_KEY3 = "Wc5emY4QVg8oFRb0xbJWUnSd4/EgCcubxTAh3ZeEc2GOJR0XJp3/IyqEVnDtQu680oKLyaTRTPhQnT4EcufhJw=="
DATA_GO_KR_KEY4 = "CLarf6LYEcbGJTHZ9zDua5StwIeVB1D2Vg4hUqmb9Ws6ohPCi2qV5OlUkx6kTz7amvkEoRj7hP8q+4FXONknvw=="
DATA_GO_KR_KEY5 = "CLarf6LYEcbGJTHZ9zDua5StwIeVB1D2Vg4hUqmb9Ws6ohPCi2qV5OlUkx6kTz7amvkEoRj7hP8q+4FXONknvw=="
DATA_GO_KR_KEY6 = "gZZSfaHHCp8tVZhjDKC/zDpFT823boO5Mx2LKOwXZkvWgxL1jdkzfW70Vn/kyJV20R7sA0q9fd6TWW6jqPQVlw=="

DATA_GO_KR_KEY = DATA_GO_KR_KEY1
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

print(DATABASES)
