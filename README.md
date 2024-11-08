# ind-80-dj5-halodunia
Membuat setup proyek Django versi 5 dengan menampilkan HALO DUNIA!
Gighub: https://github.com/gurnitha/ind-80-dj5-halodunia


## 1. SETUP

#### 1. Membuat lingkungan virtual

#### 2. Mengaktifkan venv312512

#### 3. Menginstal Django 

#### 4. Memverifikasi hasil

#### 5. Mengningkatkan versi pip

#### 6. Menjelajahi perintah django-admin


## 2. PROYEK DJANGO

#### 1. Membuat proyek Django

        modified:   .gitignore
        modified:   README.md
        new file:   config/config/__init__.py
        new file:   config/config/asgi.py
        new file:   config/config/settings.py
        new file:   config/config/urls.py
        new file:   config/config/wsgi.py
        new file:   config/manage.py

#### 2. Menjalankan server pengembangan Django

#### 3. Struktur proyek Django

#### 4. Memodifikasi struktur proyek

        modified:   README.md
        renamed:    config/config/__init__.py -> config/__init__.py
        renamed:    config/config/asgi.py -> config/asgi.py
        renamed:    config/config/settings.py -> config/settings.py
        renamed:    config/config/urls.py -> config/urls.py
        renamed:    config/config/wsgi.py -> config/wsgi.py
        renamed:    config/manage.py -> manage.py

#### 5. Membuat file requirements.txt

        modified:   README.md
        new file:   requirements.txt


## 3. MENSETING PROYEK

#### 1. Menseting bahasa dan waktu

        # Menseting bahasa
        LANGUAGE_CODE = 'id'
        # Menseting waktu
        TIME_ZONE = 'Asia/Jakarta'

        modified:   README.md
        modified:   config/settings.py

#### 2. Menseting path untuk templates

        ...
        import os
        ...
        # Menseting absolut path untuk templates
        TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

        # print(__file__)
        # print(os.path.dirname(__file__))
        # print(os.path.dirname(os.path.dirname(__file__)))

        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [TEMPLATE_DIR, ],
                ...
        ]
        ....

        # testing
        (venv312512) λ python manage.py check
        C:\Users\ING\Desktop\workspace\ind-80-dj5-halodunia\src\config\settings.py
        C:\Users\ING\Desktop\workspace\ind-80-dj5-halodunia\src\config
        C:\Users\ING\Desktop\workspace\ind-80-dj5-halodunia\src
        System check identified no issues (0 silenced).

        (venv312512) λ mkdir templates

        modified:   README.md
        modified:   config/settings.py

#### 3. Menseting path untuk file statis

        # Menseting absolute path untuk file statis
        STATIC_DIR = os.path.join(BASE_DIR, 'static')
        STATICFILES_DIRS = [STATIC_DIR, ]
        STATIC_URL = 'static/'

        modified:   README.md
        modified:   config/settings.py

#### 4. Menseting path untuk file media

        # Menseting absolute path untuk file media
        MEDIA_DIR = os.path.join(BASE_DIR, 'media')
        MEDIA_ROOT = MEDIA_DIR
        MEDIA_URL = '/media/'

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py


## 4. DATABASE

#### 1. Membuat MySQL database

        # 1. Create database
        λ mysql -u root
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 9
        Server version: 8.0.30 MySQL Community Server - GPL

        Copyright (c) 2000, 2022, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql>
        mysql> CREATE DATABASE ind_80_dj5_halodunia;
        Query OK, 1 row affected (0.14 sec)

        # 2. Connect the project with database

        # MySQL Database
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ind_80_dj5_halodunia',
            'USER': 'root',
            'PASSWORD': '',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }

        # 3. Check
        (venv312512) λ python manage.py check
        Traceback (most recent call last):
          File "C:\Users\ING\Desktop\workspace\ind-80-dj5-halodunia\venv312512\Lib\site-packages\django\db\backends\mysql\base.py", line 16, in <module>
            import MySQLdb as Database
        ModuleNotFoundError: No module named 'MySQLdb'

        ...
        raise ImproperlyConfigured(
        django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
        Did you install mysqlclient?

        # 4. Install mysqlclient
        (venv312512) λ pip install mysqlclient
        Collecting mysqlclient
          Downloading mysqlclient-2.2.5-cp312-cp312-win_amd64.whl.metadata (4.8 kB)
        Downloading mysqlclient-2.2.5-cp312-cp312-win_amd64.whl (207 kB)
        Installing collected packages: mysqlclient
        Successfully installed mysqlclient-2.2.5

        # 5. Check

        (venv312512) λ python manage.py check
        System check identified no issues (0 silenced).

#### 2. Melindungi file penting

        # 1. Membuat file .env dan .env.example
        (venv312512) λ touch .env .env.example

        # 2. Setup db kredensial pada .env
        DEBUG=True
        SECRET_KEY=django-insecure-%5hrvtl+3hx7&6@-bfgr^ry$z(%liuh6(tet8brhr7n)=3w75c
        DATABASE_NAME=ind_80_dj5_halodunia
        DATABASE_USER=root
        DATABASE_PASSWORD=
        DATABASE_HOST=localhost
        DATABASE_PORT=3306

        # 3. Mengimplementasikan environ

        # 3.1. / 1. Impor environ
        import environ

        # 3.2. / 2. Create environ
        env = environ.Env(
            # set casting, default value
            DEBUG=(bool, False)
        )

        ...

        # 3.3. / 3. Set the project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 3.4. / 4. Take environment variables from .env file
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

        # Quick-start development settings - unsuitable for production
        # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

        # SECURITY WARNING: keep the secret key used in production secret!
        # SECRET_KEY = 'django-insecure-%5hrvtl+3hx7&6@-bfgr^ry$z(%liuh6(tet8brhr7n)=3w75c'

        # 3.5. / 5. Raises Django's ImproperlyConfigured
        # exception if SECRET_KEY not in os.environ
        SECRET_KEY = env('SECRET_KEY')

        # SECURITY WARNING: don't run with debug turned on in production!
        # DEBUG = True
        # 3.6. / 6. False if not in os.environ because of casting above
        DEBUG = env('DEBUG')

        ...
        # 3.7. / 7. Set db
        DATABASES = {
            'default': {
                'ENGINE': os.environ.get('MYSQL_ENGINE'),
                'NAME': os.environ.get('DATABASE_NAME'),
                'USER': os.environ.get('DATABASE_USER'),
                'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
            }
        }

        # 4. Check
        (venv312512) λ python manage.py check
        File "C:\Users\ING\Desktop\workspace\ind-80-dj5-halodunia\src\config\settings.py", line 13, in <module>
            import environ
        ModuleNotFoundError: No module named 'environ'

        # 5. Instal django-environ
        (venv312512) λ pip install django-environ
        Collecting django-environ
          Using cached django_environ-0.11.2-py2.py3-none-any.whl.metadata (11 kB)
        Using cached django_environ-0.11.2-py2.py3-none-any.whl (19 kB)
        Installing collected packages: django-environ
        Successfully installed django-environ-0.11.2

        # 6. Check
        (venv312512) λ python manage.py check
        System check identified no issues (0 silenced).

        # 7. Setup .env.example
        DEBUG=True
        SECRET_KEY=
        DATABASE_NAME=
        DATABASE_USER=
        DATABASE_PASSWORD=
        DATABASE_HOST=
        DATABASE_PORT=

        new file:   .env.example
        modified:   README.md
        modified:   config/settings.py

#### 3. Mengganti MySQL database dengan PostgreSQL database 

        # 1. Login ke server
        λ psql -U postgres
        psql (16.2)
        WARNING: Console code page (437) differs from Windows code page (1252)
                 8-bit characters might not work correctly. See psql reference
                 page "Notes for Windows users" for details.
        Type "help" for help.

        postgres=#

        # 2. Membuat database
        postgres=# CREATE DATABASE ind_80_dj5_halodunia;
        CREATE DATABASE

        # 3. Konek proyek dengan database
        # 7. (3.1) Set db
        DATABASES = {
            'default': {
                # 'ENGINE': os.environ.get('MYSQL_ENGINE'),
                'ENGINE': os.environ.get('PSQL_ENGINE'),
                'NAME': os.environ.get('DATABASE_NAME'),
                'USER': os.environ.get('DATABASE_USER'),
                'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
            }
        }
        
        # 4. Check
        (venv312512) λ python manage.py check
        Traceback (most recent call last):
          File "C:\Users\ING\Desktop\workspace\ind-80-dj5-halodunia\venv312512\Lib\site-packages\django\db\backends\postgresql\base.py", line 25, in <module>
            import psycopg as Database
        ModuleNotFoundError: No module named 'psycopg'
        ...
        File "C:\Users\ING\Desktop\workspace\ind-80-dj5-halodunia\venv312512\Lib\site-packages\django\db\backends\postgresql\base.py", line 29, in <module>
            raise ImproperlyConfigured("Error loading psycopg2 or psycopg module")
        django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 or psycopg module

        # 5. Instal psycopg2
        (venv312512) λ pip install psycopg2
        Collecting psycopg2
          Downloading psycopg2-2.9.10-cp312-cp312-win_amd64.whl.metadata (5.0 kB)
        Downloading psycopg2-2.9.10-cp312-cp312-win_amd64.whl (1.2 MB)
           ---------------------------------------- 1.2/1.2 MB 6.4 MB/s eta 0:00:00
        Installing collected packages: psycopg2
        Successfully installed psycopg2-2.9.10

        # 6. Check
        (venv312512) λ python manage.py check
        System check identified no issues (0 silenced).

        # 7. Update requirements.txt
        (venv312512) λ pip freeze > requirements.txt
        
        modified:   README.md
        modified:   config/settings.py
        modified:   requirements.txt


## 5. APLIKASI DJANGO
