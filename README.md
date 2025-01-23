# task_fast_print_django
Tes Programmer pada Fast Print dengan Django dan PostgreSQL

## Proyek Manajemen Produk

Proyek ini adalah aplikasi web sederhana untuk mengelola produk menggunakan Django dan PostgreSQL. Aplikasi ini memungkinkan pengguna untuk menambah, mengedit, menghapus, dan menampilkan produk. Data produk diambil dari API eksternal dan disimpan dalam database.

## Fitur

- Mengambil data produk dari API
- Menyimpan produk ke dalam database
- Menampilkan daftar produk
- Menambah, mengedit, dan menghapus produk
- Validasi form input
- Filter produk yang hanya memiliki status "bisa dijual"
- Fitur konfirmasi untuk menghapus produk

## Prerequisites

Sebelum memulai, pastikan Anda memiliki hal-hal berikut:

- Python 3.x
- PostgreSQL
- Django 3.x atau lebih tinggi
- Django REST Framework (untuk serializer dan API)
- psycopg2 (untuk PostgreSQL)

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan aplikasi ini:

1. **Clone Repository**

   Clone repository ini ke dalam direktori lokal Anda:
   
   git clone https://github.com/zidanestian/task_fast_print_django.git
   cd task_fast_print_django

2. **Konfigurasi Database**

    Konfigurasi database pada file ./task_fast_print/settings.py
    Ubah bagian your_username dengan username database anda dan your_password dengan password database anda
    
3. **Jalankan Migration atau Import Database**

    Terdapat 2 cara untuk membuat table pada database
        1. Migration
            A. buat database dengan nama db_task_fast_print
            B. jalankan pada cli 
                cd task_fast_print
                python manage.py migrate
        2. Import Database
            A. Import file db_task_fast_print.sql pada database anda (file berada pada root project)

4. **Jalankan AplikasiI**

    python manage.py runserver