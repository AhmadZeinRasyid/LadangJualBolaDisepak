ahmad-zein41-ladangjualbelibola.pbp.cs.ui.ac.id

- Membuat dan mengaitkan github repo dengan local repo
- Membuat virtual environment, menyesuaikan requirements.txt dan .env, .env.prod
- Me-run command 'django-admin startproject LadangJualBola' untuk membuat projek django
- membuat aplikasi 'main' dengan `python manage.py startapp main` pada directory 'LADANGJUALBOLADISEPAK'
- membuat ../main/models.py dan menyesuaikan dengan atribut yg cocok dari models.Model
- migrate models yg baru dengan me-run `python manage.py makemigrations`dan `python manage.py migrate`
- membuat ../main/views.py dan membuat fungsi show_main(request) yang mengembalikan tampilan yg sesuai
- konfigurasi urls pada ../main/urls.py dan ../ladang_jual_bola/urls.py untuk routing dengan aplikasi 'main'
- `git push pws master`

------------------  if url exist  ---------------- url '', show_main -----------------------------------------
|  HTTPS request | -------------> | main/urls.py | ------------------| show_main,                            |
------------------  on urls.py    ----------------                   | render(request, 'main.html', context),|
        |           ladang_jual_bola                                 -----------------------------------------
        |
        |  if not      ------------
        -------------> | 404 page |
                       ------------

settings.py adalah settings utama untuk projek Django. file ini menyimpan detail database connection, list installed app, konfigurasi middleware, dan set path untuk berbagai files. 

membuat perubahan pada ../models.py dan meng-commit tidak akan berubah, justru, kita harus me-run `python manage.py makemigrations` dan `python manage.py migrate` agar modelnya dapat secara benar ter-update

kita menggunakan Django karna menggunakan python yg sudah dipelajari di matkul sebelumnya

no komen, gacor weh
