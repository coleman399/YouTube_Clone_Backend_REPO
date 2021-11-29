# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t(^s@5=x81_-=x($p$8k%7+4mgk-=mz1rx-!z8z!x*f*=e9fhf'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_project_database',
        'USER': 'root',
        'PASSWORD': 'army4280',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}