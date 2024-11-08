### Langkah-langkah Mensetup Starter Proyek 'Halo Dunia!'


#### Langkah 1: Prasyarat

        1. Telah menginstal Python versi 3.10 atau yang lebih tinggi.

        2. Telah menginstal MySQL atau PostgreSQL database.

        3. Telah menginstal editor text.

        4. Tentukan lokasi proyek pada komputer anda.


#### Langkah 2: Klon starter proyek

        1. Klon starter proyek halo dunia sebagai dari Github
        Gighub: https://github.com/gurnitha/ind-80-dj5-halodunia


#### Langkah 3: Setup database dan .env

        1. Buat MySQL database atau PostgreSQL database

        2. Buat file .env di dalam folder src

        3. Buka file .env.example, copy semua isinya dan paste hasil kopian pada file .env

        4. Hasil langkah 3 pada file .env:

        DEBUG=True
        SECRET_KEY=
        DATABASE_NAME=
        DATABASE_USER=
        DATABASE_PASSWORD=
        DATABASE_HOST=
        DATABASE_PORT=

        5. Setelah dilengkapi semua variabelnya dengan secret_key dan database kredensial, file .env akan menjadi:

        #MySQL
        DEBUG=True
        PSQL_ENGINE=django.db.backends.mysql
        SECRET_KEY=secret_key
        DATABASE_NAME=my_db_name
        DATABASE_USER=db_user
        DATABASE_PASSWORD=password
        DATABASE_HOST=localhost
        DATABASE_PORT=3306

        # PostgreSQL
        DEBUG=True
        PSQL_ENGINE=django.db.backends.postgresql_psycopg2
        SECRET_KEY=secret_key
        DATABASE_NAME=my_db_name
        DATABASE_USER=db_user
        DATABASE_PASSWORD=password
        DATABASE_HOST=localhost
        DATABASE_PORT=5432

        6. Tips untuk membuat secret_key: 

        1. Buat proyek django baru;
        2. Buka file settings.py, ambil secret_keynya untuk .env; dan
        3. Hapus proyek tersebut.


#### Langkah 4: Setup database kredensial pada settings.py

        # MySQL
        DATABASES = {
            'default': {
                'ENGINE': os.environ.get('PSQL_ENGINE'),
                'NAME': os.environ.get('DATABASE_NAME'),
                'USER': os.environ.get('DATABASE_USER'),
                'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
            }
        }

        # PostgreSQL
        DATABASES = {
            'default': {
                'ENGINE': os.environ.get('PSQL_ENGINE'),
                'NAME': os.environ.get('DATABASE_NAME'),
                'USER': os.environ.get('DATABASE_USER'),
                'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
            }
        }


#### Langkah 5: Menginstal requirements.txt

        1. Buat lingkungan virtual (python -m venv nama_env)

        2. Aktifkan lingkungan virtual (nama_env\Scripts\activate)

        3. Instal requirements.txt (pip install -r requirements.txt)


#### Langkah 6: Menghapus file dan folder

        1. Buka folder ind-80-dj5-halodunia di File Explorer, hapus folder .git

        2. Anda dapat menghapus file .gitignore dan/atau README.md jika tidak diperlukan


#### Langkah 7: Menganti nama root direktori ind-80-dj5-halodunia

        1. Anda dapat mengganti nama root direktori.
           Jika ingin menami root direktori, misal src gunakan perintah: mv ind-80-dj5-halodunia src
        2. Anda dapa menghapus file .gitignore dan/atau README.md jika tidak diperlukan


#### Langkah 8: Menjalankan server dan menampilkan 'Halo Dunia!'

        1. Simpan file. Jalankan server pengembangan Django: (python manage.py runserver)

        2. Buka browser dan gunakan url: http://127.0.0.1:8000/halodunia/ untuk mengakses Halo Dunia!


#### Langkah 9: Membuat folder

        1. Buat folder 'static' dan 'templates' di dalam folder src. Gunakan perintah ini:
           mkdir static
           mkdir templates


#### Designed by ING and developed with Love by Skill_Sets Training