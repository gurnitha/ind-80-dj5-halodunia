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

