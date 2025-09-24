## Tugas 2

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

## Tugas 3

1. _data delivery_ adalah aksi mengirim data. Dalam konteks web development, _data delivery_ merujuk pada pengiriman dan penerimaan data dari klien ke server dan sebaliknya. 

2. Json dan xml sama-sama merupakan format yang umum digunakan dalam _data delivery_. Perbedaan yang paling mencolok adalah kemudahan dibacanya file json dibandingkan xml, dengan json menyimpan data dalam struktur key-value pairs, sementara xml menggunakan struktur tag-based. _parsing_ json lebih cepat, sementara xml dapat di-extend dan dikembangkan sesuai kebutuhan. menurut saya, JSON lebih populer karna kemudahan bacanya, yang dengan sekilas dapat diinferensi apa saja data yang terdapat. saya ingin bilang bagus-tidaknya berdasarkan setiap kasus pengaplikasian, namun umumnya lebih baik menggunakan json.

3. is_valid() method dari class django.form yang mengembalikan true ketika syarat form terpenuhi, seperti textfield terisi, positiveintegerfield berisi angka positif, atau ketentuan sendiri yang bisa kita buat di forms.py, etc. kita membutuhkan is_valid() untuk memastikan ketika user men-submit form, form yang disubmit valid dan sesuai ekspektasi kita

4. csrf_token, atau cross-site request forgery token, adalah nilai yang di-generate oleh server dan disimpan oleh client. ketika client men-submit apapun kepada server, token tersebut dibawa dan dibandingkan dengan token yang dimiliki server. token ini digunakan untuk mencegah kelemahan dimana compromised-user mensubmit form yang berbahaya, untuk server maupun untuk user. tidak menggunakannya memberikan kelemahan yang sangat mudah di exploit

5. 
- xml, json, xml_by_id, dan json_by_id mereturn data json dan xml dari model object, karna model object sendiri tidak memiliki atribut atau pun method untuk mereturn data tersebut, saya menggunakan serialize yang men-parse dan mengubah data mereka menjadi bentuk yang sesuai, HttpResponse self-explanatory
- routing saya kerjakan seperti tutorial sebelumnya, saya import setiap method ke dalam urls.py, menyimpan objek urlpatterns dengan path dan menyesuaikan untuk setiap method. 
- agar user ter-direct ke link yang sesuai, kita gunakan <a></a> elemen dengan href, atau hyperlink reference ke link yang sesuai, kita rangkum elemen <button></button> agar ter-anchor pada element button. sesuaikan href dengan yang sudah ada di urls.py dan voila
- form disini sebelumnya kita buat elemen yang dapat muncul/diubah ketika inisialisasi pada models.py, mungkin ingin menambahkan ketentuan tertentu, tapi disini saya tidak, kemudian menyambungkan dengan .html yang sesuai, ProductForm terpass sebagai context dan kita gunakan django {{ }} syntax untuk mengambil forms.as_table. kita gunakan <tr> dan <td> agar anchor element setelahnya ter-render dengan sesuai.
- serupa dengan tutorial 3, kita pass object model yg sesuai sebagai context, dan merender pada html menggunakan {{ }} django syntax

