# Individual Assignment: Personal Portfolio Website

Website portofolio pribadi milik **Azzam Zawawi Al Rasyid**, dikembangkan menggunakan **Django** sebagai bagian dari tugas mata kuliah **Pemrograman Berbasis Platform (CSGE602022)**, Fakultas Ilmu Komputer, Universitas Indonesia.

**Nama:** Azzam Zawawi Al Rasyid  
**NPM:** 2506618723  
**Kelas:** PBP A  
**Tautan PWS:** [azzam-zawawi-myportofolio.pws.cs.ui.ac.id](https://azzam-zawawi-myportofolio.pws.cs.ui.ac.id)

---

## Deskripsi Proyek

Website ini merupakan portofolio pribadi berbasis Django yang menerapkan pola arsitektur **Model-View-Template (MVT)**. Proyek ini dibangun secara bertahap sepanjang semester, dimulai dari halaman statis HTML5/CSS3, kemudian dilanjutkan dengan integrasi database melalui Django ORM, penambahan fitur Form serta Data Delivery (JSON), penerapan Authentication, Session, Cookies, serta Authorization berbasis peran (pengunjung, pengguna biasa, Editor, dan pemilik portofolio). Pada Tutorial 07 dan Individual Assignment 6, halaman Project dan Experience menggunakan **Django REST Framework (DRF)** untuk representasi data, validasi, serta pemeriksaan hak akses API. Interaksi tetap menggunakan **Vanilla JavaScript, AJAX, dan Fetch API**, termasuk penyimpanan edit melalui PATCH dan filter kategori Experience tanpa memuat ulang (*reload*) halaman.

Tampilan portofolio mengusung desain *clean-modern* dengan palet warna biru muda yang lembut, tipografi **Space Grotesk** untuk judul, dan sistem *layout* responsif menggunakan CSS Grid dan Flexbox.

---

## Fitur Utama

- **Profile & Hero Section:** Menampilkan identitas personal (nama, NPM, program studi), foto, bio singkat, serta tautan GitHub, LinkedIn, dan Email.
- **Dynamic Experience Page (`/experience/`):**
  - Merender data riwayat kegiatan dan kepanitiaan dari database secara asinkron menggunakan AJAX.
  - Menerapkan tata letak *zigzag* (selang-seling) otomatis menggunakan CSS *conditional styling* yang dirender via JavaScript.
  - Dilengkapi **pencarian real-time (debouncing)** dan **filter kategori** yang dapat digunakan bersamaan, modal tambah, halaman edit melalui PATCH, serta penghapusan dan notifikasi *toast*.
  - Menampilkan status **Ongoing** ketika `ended_at` kosong dan **Completed** ketika tanggal selesai sudah terisi, sesuai properti model saat ini.
- **Dynamic Project Page (`/project/`):**
  - Menampilkan daftar proyek dalam bentuk **grid kartu** dengan efek *hover* (lift + zoom gambar) yang dirender secara asinkron via AJAX.
  - Setiap kartu memiliki gambar *thumbnail*, kategori, judul, deskripsi, serta tombol Edit dan Hapus.
  - Dilengkapi pencarian *real-time* (debouncing), penambahan data melalui modal *popover*, penyimpanan edit melalui PATCH, dan konfirmasi sebelum penghapusan melalui DELETE.
- **Autentikasi & Hak Akses Berbasis Peran (Tutorial 04 & Individual Assignment 4):**
  - Register, Login, dan Logout menggunakan sistem autentikasi bawaan Django. Status login (username dan tombol Login/Logout) tampil di navbar.
  - Cookie `last_login` ditampilkan di halaman profil dan dihapus saat logout.
  - Empat peran dengan pengecekan di sisi server: pengunjung (hanya membaca; diarahkan ke halaman login untuk aksi yang butuh akun), pengguna biasa (membaca dan memberi star), Editor (hak pengguna biasa + dapat mengubah Experience), dan pemilik portofolio/superuser (dapat membuat, mengubah, dan menghapus data). Aksi yang tidak diizinkan mengembalikan HTTP 403.
  - Peran Editor ditetapkan lewat Django Group bernama Editor di Django Admin, bukan lewat form registrasi. Sesuai contoh Tutorial 07, perubahan Project hanya diperbolehkan bagi pemilik, termasuk melalui halaman edit lama.
  - Tombol Tambah, Edit, dan Hapus disembunyikan di template bagi pengguna yang tidak berhak.
  - Proteksi PIN dari Individual Assignment 3 digantikan oleh sistem ini.
- **Fitur Star:**
  - Pengguna yang login dapat memberi atau membatalkan star pada Experience dan Project (maksimal satu star per pengguna), lengkap dengan jumlah total star dan status star pengguna saat ini.
- **Keamanan Aplikasi Lanjutan:**
  - Pencegahan pemalsuan permintaan melalui header **X-CSRFToken** pada request POST, PATCH, dan DELETE antarmuka AJAX yang menggunakan session login.
  - Mencegah bahaya **Cross-Site Scripting (XSS)** lewat *escaping* manual di sisi klien (`escapeHtml`) dan pembersihan tag HTML pada input teks melalui serializer DRF (`strip_tags`).
- **Responsive Design:**
  - Layout otomatis menyesuaikan pada layar kecil (mobile) melalui media query `@media (max-width: 600px)`.
- **Skeleton Template (`base.html`):**
  - Navbar dan footer konsisten di seluruh halaman melalui sistem `{% extends %}`.

---

## Progres Mingguan

### Tutorial 0

Pada Tutorial 0, saya melakukan setup awal proyek, meliputi pembuatan akun GitHub, instalasi IDE (Visual Studio Code), konfigurasi Git (`user.name` dan `user.email`), serta inisialisasi repositori lokal `myportofolio`. Saya juga mempelajari konsep *branching* dan *pull request* sebagai dasar alur kerja Git. Setelah itu, saya membuat *virtual environment*, menyusun file `requirements.txt`, serta menginisialisasi proyek Django dengan `django-admin startproject`. Proyek berhasil dijalankan di `http://localhost:8000/` dan struktur proyek awal siap untuk dilanjutkan ke tahap berikutnya.

### Tutorial 01

Pada Tutorial 01, saya mengganti halaman *default* Django dengan halaman **"About Me"** pertama. Saya membuat view `landing_page`, mendaftarkan folder `templates/` dan `static/` di `settings.py`, lalu menyusun halaman menggunakan elemen semantik HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`). Saya juga mulai menggunakan CSS3 dengan *custom properties* (`:root`), **CSS Grid** (`grid-template-areas`) untuk tata letak hero, serta **Flexbox** untuk navbar dan tombol sosial. Terakhir, saya men-*deploy* proyek ke PWS menggunakan konfigurasi `ALLOWED_HOSTS`, `WhiteNoise`, dan `.env.prod`.

### Individual Assignment 1

Pada Individual Assignment 1, saya melanjutkan proyek dari Tutorial 1 dengan menambahkan seksi **Experience** ke halaman portofolio. Saya mengisi seluruh data profil dengan data pribadi (nama, NPM, foto, bio), lalu membuat daftar pengalaman volunteering (Open House Fasilkom UI, BETIS Fasilkom UI, dan PSAF Fasilkom UI). Seksi ini menggunakan **layout zigzag** (teks-foto, foto-teks) yang dibuat menggunakan CSS Flexbox dengan `flex-direction: row-reverse` pada baris genap. Saya juga menambahkan efek *hover* (kartu terangkat, gambar membesar) serta memastikan tampilan tetap rapi di layar mobile melalui media query `@media (max-width: 600px)`.

### Tutorial 02

Pada Tutorial 02, saya mempelajari konsep **Model-View-Template (MVT)** di Django. Saya membuat aplikasi baru bernama `main` dan mendaftarkannya di `INSTALLED_APPS`. Saya merancang model `Experience` dengan field `id` (UUID), `title`, `description`, `category` (choices), `thumbnail` (URL), `started_at`, dan `ended_at`, lalu menjalankan `makemigrations` dan `migrate`. Selanjutnya, saya membuat view `show_main` dan `show_experience`, mendaftarkan routing modular di `main/urls.py`, serta menghubungkannya dengan `portofolio/urls.py` melalui `include()`. Saya juga mengubah `index.html` dan membuat `experience.html` yang menggunakan perulangan `{% for %}` dan tag `{% cycle %}` untuk menampilkan data secara dinamis.

### Individual Assignment 2

Pada Individual Assignment 2, saya **belum menambahkan tab portofolio baru** seperti yang disarankan di modul (misalnya Project). Sebagai gantinya, saya memfokuskan pengerjaan pada **perapian tampilan halaman Experience** yang sudah dibuat di Tutorial 02. Saya mengubah tata letak daftar pengalaman dari *grid card* sederhana menjadi **layout zigzag selang-seling** (teks-foto, foto-teks) menggunakan CSS Flexbox dengan `flex-direction: row-reverse` pada baris genap, dipadukan dengan tag `{% cycle '' 'reverse' %}` di template Django. Saya juga menambahkan efek *hover* (kartu terangkat, gambar membesar), garis pemisah vertikal antara teks dan gambar, serta memastikan tampilan tetap rapi di layar mobile melalui media query `@media (max-width: 600px)`.

**Refleksi:** Saya menyadari setelahnya bahwa pendekatan ini belum sepenuhnya sesuai dengan instruksi tugas yang meminta penambahan *section* baru dengan model tersendiri. Konsekuensinya, saya baru benar-benar membuat tab **Project** (beserta model, view, template, dan *routing*-nya) pada pengerjaan **Individual Assignment 3**, bersamaan dengan implementasi Form & Data Delivery.

### Tutorial 03

Pada Tutorial 03, saya mempelajari konsep **Form** dan **Data Delivery (JSON)**. Saya membuat **skeleton template** `base.html` sebagai kerangka utama, lalu me-*refactor* `index.html` dan `experience.html` agar meng-*extend* `base.html` sehingga navbar dan footer konsisten. Karena pada Tutorial 03 saya baru mempelajari cara membuat form, saya mengimplementasikan `ExperienceForm` dan view `create_experience` terlebih dahulu di halaman Experience. Saya juga menambahkan view `get_experience_json` dan `delete_experience`, lalu mendaftarkan endpoint `/api/experience/` di `urls.py`. Modal konfirmasi hapus dibuat menggunakan fitur bawaan HTML5 `popover="auto"` tanpa JavaScript.

### Individual Assignment 3

Pada Individual Assignment 3, saya baru benar-benar menambahkan **tab portofolio baru**, yaitu **Project**, yang seharusnya sudah mulai dikerjakan sejak Individual Assignment 2. Saya membuat model `Project` dengan field `id` (UUID), `title`, `description`, `category` (choices: Team/Individual), `thumbnail`, `started_at`, dan `ended_at`, serta menambahkan `class Meta: ordering = ["-started_at"]`. Setelah itu, saya membuat view `show_project`, `create_project`, `edit_project`, `delete_project`, dan `get_project_json`, template `project.html` dan `project_form.html`, serta endpoint `/api/project/` di `urls.py`.

Selain melengkapi kedua tab (Experience & Project) dengan mekanisme Form dan Data Delivery, saya juga menambahkan fitur **Update (Edit)** yang belum dicontohkan di Tutorial 03, dengan memanfaatkan parameter `instance=` pada ModelForm. Saya juga menambahkan **proteksi PIN sederhana** pada form Create/Edit dan aksi Delete sebagai langkah antisipasi sementara sebelum materi Authentication diajarkan. Proses *refactor* ke `base.html` sempat menimbulkan beberapa error (`TemplateSyntaxError`, `NoReverseMatch`, `FieldError`) yang saya telusuri satu per satu. Saat menjalankan `python manage.py test`, saya juga menemukan dan memperbaiki beberapa *test* yang gagal karena tautan navbar yang belum sinkron dan migrasi *seed* data yang ikut berjalan di database *testing*.

### Tutorial 4

Pada Tutorial 04, saya mempelajari perbedaan authentication dan authorization, serta cara kerja session, cookie, dan CSRF. Saya membuat fitur registrasi, login, dan logout menggunakan sistem autentikasi bawaan Django (`UserCreationForm`, `AuthenticationForm`, `login()`, dan `logout()`), membuat template `register.html` dan `login.html`, lalu menampilkan status login di navbar `base.html`. Saya juga menambahkan cookie `last_login` yang dibuat dengan `set_cookie()` saat login, ditampilkan di halaman profil lewat `request.COOKIES`, dan dihapus dengan `delete_cookie()` saat logout.
Pada bagian authorization, saya membatasi view yang mengubah data dengan `@login_required` dan pengecekan `is_superuser` (`PermissionDenied` menghasilkan 403), lalu menyembunyikan tombol yang tidak boleh dipakai melalui `{% if user.is_superuser %}` di template. Karena portofolio saya punya dua bagian, yaitu Project dan Experience, saya langsung menerapkan seluruh pola ini ke keduanya. Saya menambahkan ManyToManyField `starred_by` ke model Project dan Experience dengan `related_name` yang berbeda (`starred_projects` dan `starred_experiences`), membuat view `toggle_star_project` dan `toggle_star_experience`, serta komponen tombol star untuk masing-masing bagian.

### Individual Assignment 4
Karena fitur autentikasi, pembatasan hak akses superuser, dan star sudah saya terapkan pada Project dan Experience saat mengerjakan Tutorial 04, pada Individual Assignment 4 saya hanya perlu menambahkan satu peran baru, yaitu **Editor**.

Peran Editor dibuat dengan Django Group `Editor` melalui Django Admin (`/admin`), lalu akun tertentu dimasukkan ke grup tersebut oleh superuser. Alasannya, form registrasi bawaan hanya meminta username dan password sehingga tidak ada cara bagi pengguna untuk memilih perannya sendiri, dan memang tidak seharusnya begitu. Di view, keanggotaan grup diperiksa dengan `request.user.groups.filter(name="Editor").exists()`: view edit menerima superuser dan Editor, sedangkan view create dan delete tetap hanya untuk superuser. Pengunjung tanpa login diarahkan ke halaman login oleh `@login_required`, sedangkan pengguna yang sudah login tetapi tidak berhak menerima `PermissionDenied` (403). Status Editor dikirim dari view ke template sebagai variabel `is_editor`, sehingga tombol Edit ditampilkan bagi superuser dan Editor, sedangkan tombol Tambah dan Hapus hanya bagi superuser. Tombol star hanya ditampilkan bagi pengguna yang sudah login. Pengecekan di server tetap dipertahankan karena menyembunyikan tombol tidak mencegah orang membuka URL-nya langsung.
Karena hak akses sekarang ditangani oleh sistem autentikasi Django, saya juga menghapus proteksi PIN (`secret_passcode` dan `clean_secret_passcode()`) dari `forms.py` beserta pengecekannya di view.

### Tutorial 05

Pada Tutorial 05, saya mempelajari pendekatan pengambilan dan pengiriman data secara asinkron menggunakan **AJAX** dan **Fetch API** dengan fokus pengerjaan pada halaman **Project**. Saya memodifikasi fitur pencarian agar berjalan *real-time* saat pengguna mengetik, dengan menerapkan teknik **debouncing** (jeda 300ms) untuk mencegah *spam request* ke server. Selain itu, *form* penambahan proyek dipindahkan ke dalam **modal** berbasis `popover`, dan datanya dikirim menggunakan `fetch()` metode POST yang dilindungi oleh Token CSRF. Saya juga menambahkan komponen notifikasi **toast** interaktif untuk memberikan *feedback* visual (sukses/gagal) tanpa perlu me-*reload* halaman. Terakhir, untuk mengamankan situs dari potensi serangan **XSS (Cross-Site Scripting)** akibat memanipulasi `innerHTML`, saya menerapkan sanitasi HTML secara mandiri melalui fungsi `escapeHtml()` di sisi *client* dan `strip_tags()` di sisi *server*.

### Individual Assignment 5

Pada Individual Assignment 5, saya mengadaptasi dan menerapkan seluruh logika AJAX yang telah dibangun di Tutorial 05 secara mandiri ke halaman **Experience**. Proses ini mencakup perombakan *template* agar hanya memuat kerangka dasar pada awalnya, serta menambahkan implementasi status *loading*, *empty*, dan *error* pada antarmuka. Setelah itu, saya merakit kembali data portofolio dari *endpoint* JSON menjadi elemen HTML secara dinamis menggunakan JavaScript. Tantangan utama pada tugas ini adalah memastikan setiap fungsi JavaScript, penamaan variabel, *field* model (seperti penyesuaian properti `is_ongoing`), dan ID elemen DOM telah disesuaikan dengan akurat agar seluruh fitur asinkron di halaman Experience dapat beroperasi dengan lancar tanpa mengalami konflik dengan halaman Project.

---

### Tutorial 07

Pada Tutorial 07, halaman **Project** menggunakan **Django REST Framework** sebagai pengganti endpoint JSON manual. Representasi dan validasi data ditangani oleh `ProjectSerializer`, hak akses perubahan diperiksa oleh `IsPortfolioOwnerOrReadOnly`, dan API view berbasis fungsi ditempatkan pada `main/api_views.py`. Endpoint daftar, detail, dan star berada di bawah `/api/v1/projects/`. Halaman Project menggunakan endpoint tersebut untuk menampilkan, mencari, menambah, menghapus, dan memberi star pada data, dengan session serta perlindungan CSRF dari Django tetap dipakai.

### Individual Assignment 6

Pada Individual Assignment 6, saya menggunakan **Experience** sebagai bagian tugas, dengan mempertahankan model, data, dan relasi `starred_by` yang sudah ada. Audit awal menunjukkan bahwa `ExperienceSerializer`, permission, dan endpoint DRF Experience sudah tersedia. Karena itu, saya berfokus pada pemeriksaan kesesuaian implementasi dengan checklist dan penyelesaian integrasi edit yang masih menggunakan POST ke view lama.

Halaman edit Experience tetap digunakan, tetapi penyimpanannya diubah menjadi `fetch()` dengan PATCH ke API. Data dikirim sebagai JSON dengan header `X-CSRFToken`; respons sukses dan error ditampilkan melalui toast tanpa me-reload halaman edit. Tombol simpan dinonaktifkan selama request berlangsung untuk mencegah pengiriman ganda. View tambah AJAX lama juga diberi `@require_POST` agar hanya menerima method POST.

Saya kemudian memilih menerapkan penyimpanan edit melalui API juga pada **Project**. Hak aksesnya tetap mengikuti Tutorial 07: hanya pemilik yang dapat mengubah Project, sedangkan Experience dapat diubah oleh Editor maupun pemilik. View edit Project lama disesuaikan agar konsisten dengan API.

Sebagai tambahan di luar checklist minimal, saya menambahkan **filter kategori Experience**. Dropdown kategori menyatu di sisi kanan kolom pencarian agar tidak memakan baris tambahan. Pilihan diambil dari `Experience.EXPERIENCE_CHOICES`, lalu dikirim sebagai query parameter `category` ke API. Filter dapat digabung dengan pencarian judul dan tetap digunakan ketika daftar dimuat ulang setelah tambah, hapus, atau star. Fitur ini menggunakan model yang sudah ada tanpa migrasi atau dependency baru. Pengerjaan disimpan bertahap pada branch `feat/tugas-6-drf`.

---

## Pertanyaan Reflektif

### Assignment 1

**1. Penggunaan Semantic HTML5**

Ya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, dan `<footer>`. Saya juga menggunakan `<dl>`, `<dt>`, dan `<dd>` untuk menampilkan informasi seperti NPM dan program studi. Penggunaan elemen semantik ini membantu saya memisahkan setiap bagian halaman secara logis, sehingga ketika saya menambahkan seksi **Experience**, saya cukup membuat `<section id="experience">` baru tanpa mengganggu struktur yang sudah ada. Selain itu, selektor CSS menjadi lebih spesifik karena saya bisa menargetkan setiap bagian berdasarkan perannya, bukan sekadar `<div>`.

**2. Penataan Layout dan Responsive CSS**

Tantangan terbesar yang saya hadapi adalah mengatur posisi foto agar tetap proporsional di berbagai ukuran layar. Awalnya, foto saya tampil terlalu besar karena browser menampilkan gambar sesuai resolusi aslinya. Setelah mempelajari properti `max-width`, `aspect-ratio`, dan `object-fit: cover`, saya bisa membuat foto selalu berbentuk kotak 1:1 tanpa terdistorsi. Saya juga beberapa kali mengubah struktur `grid-template-areas` pada media query untuk mengatur ulang urutan elemen (identitas → foto → detail) di layar HP.

**3. Rencana Pengembangan Selanjutnya**

Karena website ini masih berupa *static web*, setiap kali saya ingin menambahkan pengalaman baru, saya harus mengedit kode HTML secara manual. Untuk pengembangan selanjutnya, saya ingin menyimpan data pengalaman menggunakan model Django dan database, sehingga konten dapat dikelola tanpa harus mengubah HTML. Saya juga ingin menambahkan fitur interaktif seperti *pop-up* detail kegiatan.

### Assignment 2

**1. Alur MVT dari Request Pengguna sampai Ditampilkan di Browser**

Ketika pengguna membuka URL `/experience/`, permintaan pertama diterima oleh `portofolio/urls.py` (routing tingkat proyek), yang kemudian mendelegasikan ke `main/urls.py` melalui `include("main.urls")`. Di `main/urls.py`, path `"experience/"` dicocokkan dan memanggil fungsi view `show_experience`. View ini memanggil fungsi internal `get_experience_json()` untuk mengambil data dari model `Experience` via ORM, lalu mengubahnya menjadi JSON dengan `serializers.serialize()`. Hasil JSON tersebut kemudian di-*deserialize* kembali menjadi objek Python di dalam `show_experience`, dimasukkan ke dalam `context`, dan dikirim ke template `experience.html` melalui `render()`. Template memproses perulangan `{% for %}` dan tag `{% cycle %}` untuk menghasilkan HTML dinamis, yang akhirnya dikirim sebagai HTTP Response ke browser.

**2. Alasan Penyimpanan Data di Model Dibanding Hardcode di Template**

Menyimpan data di model memisahkan secara tegas antara **lapisan data** dan **lapisan presentasi**. Dampaknya terhadap pemeliharaan:

- **Efisiensi:** Penambahan atau pembaruan portofolio cukup dilakukan lewat Django shell, admin, atau form, tanpa perlu menyentuh HTML.
- **Konsistensi:** Seluruh data ditampilkan lewat satu blok template yang sama, sehingga perubahan desain cukup diubah di satu tempat.
- **Skalabilitas:** Membuka peluang fitur lanjutan seperti pencarian, filter kategori, dan pengurutan otomatis.

**3. Perbedaan `makemigrations` dan `migrate`**

- `makemigrations`: Memindai `models.py` dan mengemas instruksi perubahan skema ke dalam file migrasi Python baru di `migrations/`. Belum mengubah database fisik.
- `migrate`: Mengeksekusi instruksi dari file migrasi tersebut ke database yang sesungguhnya (SQLite/PostgreSQL).

Contoh: Saat saya menambahkan field `ended_at` pada model `Experience`, saya harus menjalankan `makemigrations` untuk menghasilkan file migrasi, kemudian `migrate` agar kolom tersebut benar-benar tercipta di tabel database.

### Assignment 3

**1. ModelForm vs HTML Manual, dan Alasan `{% csrf_token %}`**

`ModelForm` dipakai karena otomatis menyalin struktur dari model (`Experience`/`Project`) menjadi form, sehingga saya tidak perlu menulis satu per satu tag `<input>` untuk setiap field. Field seperti `ended_at` otomatis menjadi *datetime picker*, dan validasi input (misalnya format URL) sudah ditangani Django. Jika ada field baru di model, saya cukup menambahkannya di `fields = [...]`.

`{% csrf_token %}` wajib ada karena form POST rawan disalahgunakan lewat serangan **CSRF (Cross-Site Request Forgery)**. Token ini berfungsi sebagai kode rahasia sekali pakai yang dibuat server; submit form hanya diterima kalau token-nya cocok, sehingga request dari situs luar otomatis ditolak.

**2. Kenapa JSON Lebih Disukai Dibanding XML**

JSON lebih ringkas karena tidak perlu menulis *closing tag* di setiap elemen, sehingga ukuran datanya lebih kecil dan lebih cepat dikirim. JSON juga lebih mudah di-*parsing* oleh JavaScript karena strukturnya memang berasal dari cara JavaScript menulis objek, sehingga data bisa langsung dipakai tanpa konversi tambahan. Ini penting untuk arsitektur web modern (REST API) yang banyak mengirim data bolak-balik antara server dan frontend.

**3. Alur View Mengembalikan Data JSON dan Alasan Serialization**

Ketika ada request ke endpoint `/api/experience/`, view `get_experience_json` mengambil data dari database (`Experience.objects.all()`). Data ini masih berbentuk objek Python/Django, bukan teks. Kemudian `serializers.serialize("json", ...)` dipanggil untuk mengubah objek tersebut menjadi teks berformat JSON. Teks JSON tersebut dibungkus menggunakan `HttpResponse` dengan `content_type="application/json"`, lalu dikirim sebagai response.

Serialization perlu dilakukan karena objek Python (seperti *instance* model Django) hanya "dikenali" oleh Python dan tidak bisa langsung dikirim lewat internet. Data yang dikirim lewat HTTP harus berbentuk teks, sehingga objek tersebut perlu "diterjemahkan" dulu menjadi teks JSON yang formatnya universal.

### Tugas 5

**1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!**
Debouncing adalah teknik pemrograman yang menunda eksekusi sebuah fungsi sampai jeda waktu tertentu berlalu sejak pemanggilan terakhirnya. Pada fitur pencarian AJAX, debouncing sangat penting karena mencegah browser mengirimkan HTTP request ke server untuk setiap huruf yang diketik. Tanpa debouncing, mengetik kata "Django" akan memicu 6 request berturut-turut, yang membebani kinerja server dan menghabiskan *bandwidth*. Dengan debouncing (misalnya jeda 300ms), request hanya dikirim setelah pengguna berhenti mengetik sejenak, membuat pencarian jauh lebih efisien dan responsif.

**2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**
Fungsi `await` digunakan di dalam `async function` untuk menjeda eksekusi baris kode tersebut sampai sebuah `Promise` (seperti yang dikembalikan oleh `fetch()`) selesai diproses dan mengembalikan hasil. Jika kita tidak menggunakan `await`, JavaScript akan langsung melanjutkan eksekusi ke baris berikutnya secara asinkron sebelum respons dari server diterima. Akibatnya, variabel penampung tidak akan berisi data balasan (seperti objek Response atau JSON), melainkan hanya berisi objek `Promise` yang masih *pending*, yang akan menyebabkan *error* saat kita mencoba membaca datanya.

**3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!**
XSS (Cross-Site Scripting) adalah kerentanan keamanan web di mana penyerang menyisipkan *script* berbahaya (seperti JavaScript) ke dalam data yang akan ditampilkan kepada pengguna lain. Data yang ditampilkan via AJAX lebih rentan karena JavaScript di sisi klien (terutama saat menggunakan `innerHTML`) akan langsung mengeksekusi tag HTML atau *script* apa pun yang ada di dalam *string* data tersebut. Sebaliknya, saat me-render data langsung lewat template Django, Django secara otomatis melakukan *auto-escaping* pada setiap variabel, mengubah karakter berbahaya seperti `<` dan `>` menjadi entitas teks aman (`&lt;` dan `&gt;`), sehingga mencegah *script* dieksekusi oleh browser.

---

### Tugas 6

**1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!**

REST (*Representational State Transfer*) adalah gaya arsitektur untuk komunikasi antara klien dan server. API disusun berdasarkan resource yang dikenali melalui URL, memakai HTTP method secara konsisten, serta bertukar representasi data. REST juga mencakup prinsip seperti pemisahan klien-server, stateless, dan antarmuka yang seragam. JSON hanya format data, sehingga respons JSON saja belum membuktikan bahwa sebuah API mengikuti prinsip REST.

Contohnya, `/api/v1/experiences/` mewakili kumpulan Experience dan `/api/v1/experiences/<uuid>/` mewakili satu Experience. GET membaca, POST membuat, dan DELETE menghapus. Implementasi proyek mengikuti pola resource dari tutorial, tetapi session yang disimpan di server dan endpoint aksi `/star/` berarti saya tidak menganggapnya sebagai penerapan seluruh prinsip REST secara ketat.

PUT digunakan ketika klien bermaksud mengganti representasi resource, sedangkan PATCH digunakan untuk perubahan sebagian. PUT cocok ketika mengirim seluruh data form Experience, termasuk judul, deskripsi, kategori, thumbnail, dan tanggal selesai. Jika hanya ingin mengganti judul, PATCH dapat mengirim `{"title": "PBP Teaching Assistant"}` tanpa menyertakan field lainnya. Pada view saya, `partial=True` digunakan untuk PATCH agar field yang tidak dikirim tidak diwajibkan dan nilainya tetap dipertahankan. PUT tetap memvalidasi field wajib; field opsional yang tidak dikirim tidak otomatis dikosongkan oleh ModelSerializer. Form edit memakai PATCH untuk memperbarui field yang dikelola form.

**2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?**

Serializer mengubah objek model menjadi tipe data sederhana yang kemudian dirender DRF menjadi JSON. Pada arah sebaliknya, serializer memvalidasi input, menghasilkan `validated_data`, dan dapat menyimpan perubahan melalui `.save()`. `ModelSerializer` membantu membentuk field dan validasi berdasarkan model, sementara `JsonResponse` sendiri hanya mengirim respons JSON.

Pada Tutorial 05, saya merakit dictionary dan informasi star secara manual di view. Dengan serializer, daftar field dapat ditulis eksplisit, validasi teks ditempatkan pada `validate_title()` dan `validate_description()`, serta informasi star dihitung melalui `SerializerMethodField` yang read-only. Di proyek ini, `strip_tags()` membersihkan tag HTML dan judul yang kosong setelah dibersihkan ditolak. View menjadi lebih ringkas karena cukup menjalankan `is_valid(raise_exception=True)`, menyimpan data yang valid, dan mengembalikan `Response`. Bentuk respons dan pesan error lebih konsisten, serta field sensitif akun tidak perlu ikut ditampilkan.

**3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?**

Autentikasi menentukan siapa pengirim request, sedangkan otorisasi menentukan tindakan apa yang boleh dilakukannya. `SessionAuthentication` mengenali pengguna melalui session login Django dan menyediakan identitasnya melalui `request.user`. Pengguna yang sudah login belum tentu berhak membuat atau menghapus data.

Pada Experience, `IsPortfolioOwnerOrEditorOrReadOnly` mengizinkan semua peran membaca, Editor dan pemilik melakukan PUT/PATCH, serta hanya pemilik membuat dan menghapus data. Endpoint star menggunakan `IsAuthenticated`, sehingga pengguna biasa juga dapat memberi star. Tombol disembunyikan untuk membantu antarmuka, tetapi pengguna tetap dapat mengirim request langsung ke URL API melalui alat lain. Permission di server memastikan tindakan yang tidak diizinkan ditolak sebelum perubahan dijalankan, terlepas dari tampilan tombol di browser.

**4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?**

Browser dapat mengirim cookie session secara otomatis sesuai aturan cookie. Karena itu, keberadaan session saja belum membuktikan bahwa pengguna memang bermaksud melakukan tindakan tersebut. Serangan CSRF mencoba memanfaatkan session korban untuk mengirim perubahan yang tidak dikehendaki. Saat memakai `SessionAuthentication`, request perubahan dari pengguna yang terautentikasi melalui session tetap diperiksa token CSRF-nya. Script halaman membaca cookie `csrftoken` melalui `getCookie()` dan mengirim nilainya dalam header `X-CSRFToken` saat POST, PATCH, atau DELETE.

`force_authenticate()` memilih pengguna secara langsung untuk memudahkan pengujian permission. Cara tersebut tidak menjalankan alur autentikasi session yang sesungguhnya, sehingga tidak cukup untuk membuktikan pemeriksaan CSRF. Pengujian CSRF perlu memakai `APIClient(enforce_csrf_checks=True)` dan `.login()` untuk membuat session, kemudian mengirim request perubahan tanpa token. Request tersebut seharusnya mendapat 403 dan tidak mengubah database. Request dengan token yang benar dapat digunakan sebagai pembanding. Pola pengujian session dan CSRF ini sudah tersedia pada `main/tests_api.py` proyek.

---

## AI Disclosure

### Tutorial 0 & Tutorial 01

Pada tahap awal ini, saya menggunakan **Gemini** sebagai alat bantu untuk memahami dasar-dasar HTML5 dan CSS3 yang masih terasa asing bagi saya. Saya banyak meminta penjelasan mengenai fungsi setiap tag dan properti CSS yang muncul di modul, seperti cara kerja `grid-template-areas`, `clamp()`, dan *custom properties*.

**Bagian yang Dibantu AI:**
- Menjelaskan fungsi setiap tag HTML dan properti CSS yang muncul di Tutorial 01.
- Membantu memahami cara kerja CSS Grid (`grid-template-areas`) untuk tata letak hero section.
- Membantu memahami cara mengatur foto agar proporsional menggunakan `aspect-ratio` dan `object-fit`.

**Bagian yang Saya Kerjakan dan Putuskan Sendiri:**
- Mengisi seluruh data profil dengan data pribadi (nama, NPM, foto, bio).
- Menentukan kombinasi warna dan struktur halaman portofolio.
- Menjalankan perintah Git (`add`, `commit`, `push`) dan proses *deployment* ke PWS secara mandiri.

#### AI Chat / Prompting Log

1. **Membedah struktur HTML dan CSS template bawaan**

   > *"Aku kan baru belajar HTML dan CSS, dan ini masih pakai template bawaan. Bisa tolong bedah dan jelasin ke aku struktur kode HTML dan CSS ini secara menyeluruh beserta fungsi dari masing-masing tag dan atributnya?"*

   **Konteks & Tujuan:** Digunakan saat mengawali proyek untuk memahami peran setiap tag semantik HTML5 dan atribut bawaan template sebelum mulai memodifikasinya menjadi halaman portofolio pribadi.

2. **Memahami aturan penulisan properti `padding` dan `margin`**

   > *"Bisa jelasin rumus dan aturan nilai pada padding dan margin di CSS? Kapan kita pakai 1, 2, atau 4 nilai, dan apa bedanya pengaruh ke tata letak elemen?"*

   **Konteks & Tujuan:** Ditanyakan ketika mengatur jarak antar-elemen agar tata letak tombol navigasi dan kartu tidak saling menumpuk.

3. **Mengatasi perubahan CSS yang tidak langsung muncul**

   > *"Aku udah edit file CSS-nya, tapi kok pas browser di-refresh tampilannya sama sekali gak berubah ya? Gimana cara refresh atau preview perubahan terbarunya?"*

   **Konteks & Tujuan:** Digunakan saat proses *styling* terhambat oleh *caching* browser, guna memahami solusi pembersihan *cache* dan penggunaan kombinasi tombol *hard reload* (`Ctrl + F5`).

4. **Membuat animasi hover pada tombol**

   > *"Bagian kode CSS mana yang dipakai buat bikin tombol berubah warna waktu kursor diarahkan ke situ? Tolong contohin cara bikin transisinya biar animasinya halus."*

   **Konteks & Tujuan:** Ditanyakan untuk menerapkan *pseudo-class* `:hover` dan properti `transition` pada tautan media sosial di Hero Section.

#### Keterbatasan AI dan Pemahaman Saya

AI tidak dapat melihat tampilan browser saya secara langsung, sehingga setiap kali ada masalah visual, saya perlu mendeskripsikan sendiri apa yang saya lihat. Pada tahap ini, saya juga menyadari bahwa saya masih sangat bergantung pada penjelasan AI untuk memahami dasar-dasar HTML dan CSS. Saya belum bisa menulis kode dari nol tanpa contoh, dan sebagian besar pemahaman saya terbentuk dari proses *copy-paste* lalu meminta penjelasan. Ke depannya, saya perlu melatih diri untuk menulis kode sendiri terlebih dahulu sebelum bertanya, agar pemahaman saya tidak hanya bersifat pasif.

---

### Individual Assignment 1

Pada tahap ini, saya kembali dibantu Gemini untuk mengembangkan seksi **Experience** yang baru. Karena materi CSS Grid/Flexbox masih baru, saya banyak meminta penjelasan mengenai cara membuat *layout zigzag* dan efek *hover* yang interaktif.

**Bagian yang Dibantu AI:**
- Menjelaskan cara kerja `flex-direction: row-reverse` yang dipadukan dengan `{% cycle %}`.
- Membantu memahami properti `overflow: hidden` dan `transform: scale()` untuk efek *zoom* gambar.
- Membantu memahami cara membuat modal *pop-up* konfirmasi hapus berbasis CSS.

**Bagian yang Saya Kerjakan dan Putuskan Sendiri:**
- Menentukan kurasi data pengalaman volunteering yang ingin ditampilkan (Open House, BETIS, PSAF) beserta deskripsi dan foto dokumentasi.
- Menentukan kategori dan status pengalaman (Ongoing/Completed).
- Mengecek tampilan di browser dan perangkat mobile secara berkala.

#### AI Chat / Prompting Log

1. **Membuat tata letak zigzag (selang-seling) untuk daftar pengalaman**

   > *"Gimana cara bikin layout daftar pengalaman yang selang-seling (baris 1: teks kiri foto kanan, baris 2: foto kiri teks kanan) pakai Flexbox/Grid, terus di antara foto dan teksnya mau aku kasih garis pemisah vertikal?"*

   **Konteks & Tujuan:** Digunakan saat menyusun seksi *Experience* agar visual halaman lebih dinamis dan tidak monoton.

2. **Mengisolasi efek hover agar tidak memicu seluruh kartu**

   > *"Waktu aku kasih efek hover di satu item pengalaman, kok semua kartu di bawahnya ikut gerak/kena efeknya ya? Gimana caranya biar efek hover-nya cuma aktif di kartu yang lagi disentuh kursor?"*

   **Konteks & Tujuan:** Ditanyakan untuk memisahkan struktur blok kartu menggunakan tag semantik `<article>` terpisah agar *scope* animasi tetap independen.

3. **Memperbaiki border gambar yang terpotong saat membesar (zoom)**

   > *"Pas gambar aku kasih efek scale/zoom waktu di-hover, kok garis border di sekeliling fotonya malah hilang atau kepotong? Gimana cara perbaikinya?"*

   **Konteks & Tujuan:** Digunakan untuk memahami perilaku `overflow: hidden` pada elemen induk pembungkus gambar agar *border-radius* dan garis batas tetap terlihat utuh saat transformasi aktif.

4. **Memahami variasi nilai properti CSS `display`**

   > *"Tolong jelasin perbedaan mendasar antara display block, inline, inline-block, flex, grid, dan none di CSS beserta contoh situasi penggunaannya masing-masing."*

   **Konteks & Tujuan:** Ditanyakan guna memperdalam pemahaman dasar seputar alur render dokumen HTML dan penataan komponen halaman.

#### Keterbatasan AI dan Pemahaman Saya

AI tetap tidak dapat melihat hasil akhir tampilan, sehingga saya harus berulang kali mengecek sendiri di browser dan menjelaskan kondisinya ke AI. Saya juga menyadari bahwa solusi yang diberikan AI kadang tidak langsung cocok, dan saya perlu menyesuaikannya kembali dengan struktur proyek saya. Pada tahap ini, saya mulai belajar untuk tidak langsung menerima kode dari AI, tetapi mencoba memahami logikanya terlebih dahulu. Meskipun demikian, saya masih kesulitan untuk menuliskan solusi alternatif sendiri tanpa arahan dari AI, terutama untuk properti seperti `overflow` dan `transform` yang belum saya kuasai sepenuhnya.

---

### Tutorial 02 & Individual Assignment 2

Pada tahap ini, saya mulai mempelajari konsep **MVT (Model-View-Template)** yang benar-benar baru bagi saya. Saya menggunakan Gemini untuk memahami bagaimana `urls.py`, `view`, `model`, dan `template` saling terhubung sebelum mulai menulis kode.

**Bagian yang Dibantu AI:**
- Menjelaskan alur MVT dari *request* pengguna sampai data tampil di browser.
- Membantu memahami cara kerja `makemigrations` dan `migrate`.
- Membantu menyusun strategi pengisian data awal di server PWS menggunakan Django Fixtures.
- Membantu menulis *unit test* untuk memvalidasi akses URL, penggunaan template, dan render data.

**Bagian yang Saya Kerjakan dan Putuskan Sendiri:**
- Menentukan pendekatan visual untuk merapikan halaman Experience menjadi layout zigzag selang-seling.
- Menentukan kurasi pengalaman volunteering yang ditampilkan, beserta deskripsi dan foto dokumentasinya.
- Menjalankan migrasi, *testing*, dan *deployment* ke PWS secara mandiri.

**Catatan:** Pada tahap ini saya belum menambahkan tab Project seperti yang diminta di instruksi tugas, sehingga baru saya kerjakan pada Individual Assignment 3.

#### AI Chat / Prompting Log

1. **Memahami alur data pada arsitektur MVT Django**

   > *"Bisa jelaskan alur kerja MVT di Django dari awal user mengetikkan URL di browser sampai halaman dirender? Aku masih bingung membedakan peran dan hubungan antara urls.py, views.py, models.py, dan file HTML template."*

   **Konteks & Tujuan:** Digunakan sebagai dasar konseptual sebelum memecah kode monolitik menjadi aplikasi modular (`main`) dan membuat *database model*.

2. **Mendiagnosis data database lokal yang tidak tampil di PWS**

   > *"Di server lokal (localhost) data pengalaman dan proyekku udah muncul lengkap, tapi kenapa pas di-deploy ke PWS halamannya malah kosong? Apakah file db.sqlite3 lokal gak otomatis ikut ke-deploy ke server produksi?"*

   **Konteks & Tujuan:** Ditanyakan saat menyadari adanya disparitas database antara environment *development* dan *production*, yang kemudian diarahkan pada solusi penggunaan Django Fixtures.

3. **Menangani error path dumpdata di PowerShell**

   > *"Waktu aku jalankan perintah python manage.py dumpdata di terminal PowerShell, muncul error: 'Out-File : Could not find a part of the path .../main/fixtures/experiences.json'. Gimana cara export data fixture yang benar di Windows?"*

   **Konteks & Tujuan:** Digunakan saat menyiapkan file *seed data* JSON agar tidak terhambat oleh sintaks *redirection* terminal Windows.

4. **Mengatasi urutan data yang tidak konsisten**

   > *"Kenapa urutan data Experience di localhost beda sama urutan data yang tampil di web PWS, padahal datanya sama persis? Gimana cara bikin urutannya paten dan konsisten?"*

   **Konteks & Tujuan:** Ditanyakan untuk memahami pentingnya penetapan `ordering` pada `class Meta` model Django atau pada query `order_by()`.

5. **Menambahkan thumbnail gambar pada kartu Project**

   > *"Gimana cara nambahin kolom URL gambar di model Project, dan gimana sintaks di templatenya biar kalau gambarnya gak ada, dia otomatis nampilin placeholder gambar default?"*

   **Konteks & Tujuan:** Digunakan untuk memperkaya tampilan kartu proyek dengan aset visual eksternal dan menangani kondisi *fallback* (*empty state*).

#### Keterbatasan AI dan Pemahaman Saya

Pada tahap ini, saya mulai menyadari bahwa MVT bukan sekadar urutan kode, tetapi pola pikir tentang pemisahan tanggung jawab. Saya masih kesulitan memahami bagaimana satu `view` bisa memanggil `view` lain (seperti `show_experience` yang memanggil `get_experience_json`), dan butuh beberapa kali penjelasan ulang dari AI untuk benar-benar paham. Saya juga sempat salah kaprah tentang peran `fixtures` dan sempat berpikir bahwa file JSON itu adalah database-nya, padahal hanya media perantara.

Selain itu, saya juga kurang teliti dalam membaca instruksi Individual Assignment 2, sehingga saya **belum menambahkan tab portofolio baru** seperti yang diminta, dan hanya berfokus pada perapian tampilan Experience. Akibatnya, pengerjaan tab Project baru saya lakukan pada Individual Assignment 3. Ini menjadi pelajaran bagi saya untuk membaca ulang *checklist* tugas secara menyeluruh sebelum mulai mengerjakan.

---

### Tutorial 03 & Individual Assignment 3

Pada tahap ini, saya menggunakan Gemini terutama untuk membantu *debugging*, karena banyak error yang muncul dari proses *refactor* kode lama (Tutorial 02) ke struktur baru dengan `base.html`, bukan dari materi baru itu sendiri.

**Bagian yang Dibantu AI:**
- Menjelaskan penyebab error `TemplateSyntaxError`, `NoReverseMatch`, `FieldError`, dan `CSRF verification failed`.
- Membantu menulis `ExperienceForm`, `ProjectForm`, view CRUD untuk kedua model, dan endpoint JSON.
- Membantu memahami cara membuat modal konfirmasi hapus berbasis `popover` tanpa JavaScript.
- Membantu menelusuri langkah-langkah perbaikan setelah *test* gagal.

**Bagian yang Saya Kerjakan dan Putuskan Sendiri:**
- Memutuskan untuk menambahkan tab **Project** yang sebelumnya belum dibuat di Individual Assignment 2.
- Menentukan untuk menambahkan fitur Edit yang tidak dicontohkan di Tutorial 03.
- Menentukan untuk menambahkan proteksi PIN sederhana sebelum materi Authentication diajarkan.
- Memeriksa sendiri setiap berkas (`views.py`, `urls.py`, `forms.py`, template) setelah mendapat penjelasan dari AI.
- Menjalankan `python manage.py test` dan `python manage.py runserver` untuk memverifikasi setiap perbaikan.

#### AI Chat / Prompting Log

1. **Menelusuri error setelah refactoring ke template inheritance (`base.html`)**

   > *"Setelah aku pecah template jadi base.html dan pakai {% extends %}, di terminal dan browser muncul error kayak TemplateSyntaxError dan NoReverseMatch. Ini log error lengkapnya: [paste log error]. Bagian mana dari tag block atau routing url yang salah sambung?"*

   **Konteks & Tujuan:** Digunakan sebagai prompt *troubleshooting* untuk melacak kegagalan render template akibat nama blok atau parameter URL yang belum sinkron pasca-refaktorisasi.

2. **Memahami perbedaan perintah `makemigrations` dan `migrate`**

   > *"Tolong jelaskan secara konkret perbedaan fungsi antara python manage.py makemigrations dan python manage.py migrate. Kapan waktu yang tepat menjalankan masing-masing perintah tersebut?"*

   **Konteks & Tujuan:** Ditanyakan untuk memantapkan alur pembaruan skema database ketika menambahkan *field-field* baru ke dalam model.

3. **Mengimplementasikan form Edit (Update) data**

   > *"Di materi tutorial kan baru ada Create dan Delete. Gimana cara bikin form dan view untuk Edit/Update data Experience yang sudah ada, dan gimana caranya biar form-nya otomatis terisi sama data lama yang mau diubah?"*

   **Konteks & Tujuan:** Digunakan untuk melengkapi siklus CRUD secara mandiri dengan memanfaatkan parameter `instance=` pada Django `ModelForm`.

4. **Membuat proteksi validasi PIN/Passcode sederhana**

   > *"Karena belum ada materi user login/authentication, gimana cara paling simpel untuk ngasih proteksi PIN rahasia di form Tambah/Edit dan tombol Hapus, supaya orang lain gak bisa sembarangan memodifikasi data portofolioku?"*

   **Konteks & Tujuan:** Ditanyakan untuk mengimplementasikan pengamanan sementara di level form (`clean_secret_passcode`) dan *conditional check* di *view* sebelum materi sesi autentikasi resmi diajarkan.

5. **Mendiagnosis kegagalan unit test (`test_completed_experience`)**

   > *"Waktu aku jalankan perintah 'python manage.py test', ada satu test yang gagal (test_completed_experience). Ini pesan failure trace-nya: [paste trace error]. Kira-kira apa yang bikin test ini gagal padahal di browser fiturnya berfungsi normal?"*

   **Konteks & Tujuan:** Digunakan saat mencari akar penyebab *assertion error*, yang ternyata dipicu oleh adanya migrasi data otomatis (*seed data*) yang ikut terpasang di database *isolated testing*.

6. **Mengevaluasi celah keamanan endpoint tanpa autentikasi**

   > *"Kalau form dan endpoint API delete/update ini gak pakai sistem login akun, apakah artinya siapa saja yang tahu URL-nya bisa nembak request lewat Postman atau browser? Apa best practice standar untuk mencegah hal ini ke depannya?"*

   **Konteks & Tujuan:** Digunakan sebagai bentuk refleksi teknis untuk memahami pentingnya middleware autentikasi, pembatasan hak akses (*permissions*), dan proteksi CSRF pada aplikasi web skala produksi.

7. **Menambahkan tab Project yang tertunda dari Individual Assignment 2**

   > *"Di tugas 2 seharusnya aku nambah tab baru tapi aku belum sempat, baru ngerjain perapian tampilan Experience. Sekarang aku mau bikin tab Project dari nol, mulai dari model, view, template, sampai form dan JSON delivery-nya. Bisa tuntun aku step-by-step mirip kayak Experience?"*

   **Konteks & Tujuan:** Digunakan untuk mengejar ketertinggalan dari Individual Assignment 2 dengan memanfaatkan pola yang sudah terbentuk di Experience, lalu diterapkan ke model `Project` baru.

#### Keterbatasan AI dan Pemahaman Saya

Pada tahap ini, saya menyadari bahwa proses *refactor* kode lama ternyata lebih rawan menimbulkan error dibanding menulis kode baru dari nol, karena ada banyak bagian yang mudah terlewat, seperti berkas HTML yang belum ikut di-*extend*, migrasi yang saling bergantung, atau referensi ke model yang sudah dihapus namun masih tertinggal di berkas lain. AI membantu saya menelusuri error tersebut satu per satu, tetapi saya tetap perlu memeriksa kembali setiap berkas secara manual untuk memastikan tidak ada bagian lain yang tertinggal.

Saya juga menyadari bahwa proteksi PIN yang saya tambahkan bukan solusi keamanan yang sesungguhnya, karena PIN-nya masih *hardcoded* di `forms.py` dan tidak terhubung dengan sistem autentikasi Django. Saya perlu mempelajari konsep Authentication, Session, dan Cookies lebih lanjut di tutorial-tutorial berikutnya untuk benar-benar membatasi akses ke fitur Create, Update, dan Delete pada portofolio saya.

### Tutorial 04 & Individual Assignment 4
Pada tahap ini, saya menggunakan Gemini untuk memahami cara menerapkan pola star dan hak akses dari tutorial ke dua bagian portofolio saya (Experience dan Project), serta untuk memahami cara menentukan peran Editor.

**Bagian yang Dibantu AI:**
- Menjelaskan cara mengadaptasi fitur star dari Project ke Experience (model, view, URL, dan komponen template).
- Menjelaskan cara membuat superuser dengan `createsuperuser`.
- Membantu memahami cara menentukan peran Editor tanpa mengubah form registrasi.

**Bagian yang Saya Kerjakan dan Putuskan Sendiri:**
- Memutuskan untuk menerapkan seluruh pola Tutorial 04 langsung ke kedua bagian (Experience dan Project), bukan hanya Project.
- Menulis dan menghubungkan model, view, URL, dan template untuk kedua bagian, lalu menjalankan migrasi.
- Menghapus proteksi PIN dari form dan view karena sudah digantikan oleh autentikasi.
- Membuat akun superuser, grup Editor, dan akun uji untuk setiap peran, lalu mencoba sendiri tiap peran di browser.
- Memperbaiki sendiri error-error kecil yang muncul (misalnya import yang kurang, tipe parameter URL, dan typo nama URL).

**AI Chat / Prompting Log**
1. **Menerapkan fitur star ke dua bagian portofolio**
  > *"Di tutorial ada fitur star, tapi contohnya cuma untuk Project. Sedangkan portofolioku punya section Project dan Experience, dan di Langkah 4 aku sudah nulis field starred_by di kedua model. Jadi gimana cara mengerjakan Langkah 5 (view, URL, dan template tombol star) untuk kedua section itu?"*

  **Konteks & Tujuan:** Digunakan untuk memahami bahwa pola pada tutorial bisa dipakai ulang untuk model lain dengan mengganti nama model dan `related_name`, sehingga saya membuat `toggle_star_project` dan `toggle_star_experience` beserta komponen tombol masing-masing.

2. **Membuat akun superuser**
  > *"Aku belum punya superuser. Gimana cara membuatnya, dan apa bedanya dengan akun yang dibuat lewat form register?"*

  **Konteks & Tujuan**: Digunakan untuk membuat akun pemilik portofolio dengan `python manage.py createsuperuser`, yang diperlukan untuk menguji hak akses create dan delete serta untuk mengakses Django Admin.

3. **Menentukan akun mana yang menjadi Editor**
  >  *"Gimana cara kita memilih akun yang Editor atau bukan? Kan saat register cuma masukin username dan password, nggak ada yang menentukan Editor atau bukan."*

  **Konteks & Tujuan**: Ditanyakan saat merancang peran Editor. Kesimpulannya, peran tidak boleh dipilih sendiri oleh pengguna saat registrasi. Peran ditetapkan oleh superuser melalui grup Editor di Django Admin, lalu diperiksa di view dan template.

**Keterbatasan AI dan Pemahaman Saya**
AI tidak bisa melihat kode proyek saya, sehingga jawabannya sering berupa contoh umum yang harus saya sesuaikan sendiri dengan struktur proyek, misalnya tipe ID model (UUID) dan nama parameter di urls.py. Saya juga perlu teliti saat menyalin pola dari satu model ke model lain, misalnya `related_name` yang harus dibedakan. Selain itu, saya menyadari bahwa menyembunyikan tombol di template tidak cukup untuk mengamankan aplikasi, sehingga pengecekan hak akses di sisi server (`@login_required`, `PermissionDenied`, dan pengecekan grup) tetap harus ada. Saya juga masih perlu memahami lebih dalam perbedaan pemeriksaan grup dengan pemeriksaan permission per model, karena saya baru memakai pemeriksaan grup yang paling sederhana.

### Tutorial 05 & Individual Assignment 5

Pada tahap ini, saya menggunakan AI (Gemini) untuk mendukung transisi proyek portofolio saya dari *rendering* sisi server menuju pendekatan *client-side* asinkron menggunakan AJAX dan Fetch API.

**Bagian yang Dibantu AI:**
- Membantu menelusuri penyebab *Internal Server Error (500)* saat mengambil data JSON akibat ketidaksesuaian *field* model pada respons API.
- Membantu merevisi logika penanggalan pada properti `is_ongoing` di model `Experience` agar membandingkan waktu secara aktual menggunakan `timezone.now()`.
- Memberikan penjelasan mengenai urgensi teknik *debouncing* untuk optimasi *request* asinkron.
- Memberikan gambaran alur kerja (*workflow*) yang sistematis tentang cara mengadaptasi mekanisme JavaScript/AJAX dari bagian Project agar dapat diimplementasikan pada halaman Experience.

**Bagian yang Saya Kerjakan dan Putuskan Sendiri:**
- Menerapkan fungsi AJAX dan `fetch()` pada halaman portofolio secara mandiri mengikuti instruksi tutorial, mulai dari perakitan modal, notifikasi *toast*, hingga inisialisasi pencarian dinamis.
- Menganalisis *traceback error* dari *Network DevTools* secara mandiri untuk memberikan konteks yang tepat kepada AI.
- Secara aktif mengevaluasi hasil akhir fitur (seperti masalah validasi tanggal) dan secara proaktif mengarahkan AI untuk memperbaiki logika yang tidak sesuai dengan nalar aplikasi kehidupan nyata.

#### AI Chat / Prompting Log

1. **Mendiagnosis Kegagalan Endpoint AJAX (*Internal Server Error*)**
   > *"Saat saya melakukan fetch() ke endpoint API JSON portofolio, saya mendapatkan pesan Internal Server Error (500) dan traceback menunjukkan `AttributeError`. Bagaimana cara menelusuri ketidaksesuaian atribut ini saat merakit dictionary JSON secara manual di views.py?"*
   
   **Konteks & Tujuan:** Digunakan untuk melacak penyebab *crash* pada fungsi serialisasi, yang dipicu oleh sisa atribut peninggalan entitas lain yang tidak dikenali oleh model target.

2. **Memperbaiki Logika Bisnis (*Business Logic*) Penentuan Status**
   > *"Status data pengalaman saya selalu dirender sebagai 'Completed' oleh AJAX padahal tanggal selesainya masih di masa depan. Bagaimana cara memperbarui logika properti di model Django agar membandingkan parameter tanggal dengan waktu aktual saat ini?"*
   
   **Konteks & Tujuan:** Ditanyakan ketika saya menyadari bahwa evaluasi bawaan hanya memeriksa terisi atau tidaknya sebuah kolom. Permintaan ini ditujukan agar AI memberikan solusi komparasi waktu menggunakan pustaka bawaan Django.

3. **Memahami Urgensi *Debouncing* pada Pencarian**
   > *"Mengapa kita harus menerapkan teknik debouncing (seperti penggunaan `setTimeout` dan `clearTimeout`) pada kolom pencarian yang menggunakan AJAX? Apa dampaknya terhadap kinerja aplikasi web?"*
   
   **Konteks & Tujuan:** Digunakan untuk memperdalam pemahaman teoretis mengenai optimasi kinerja *client-side* dan langkah pencegahan *request* berlebih (*spamming*) ke server.

4. **Mengadaptasi Implementasi AJAX pada Halaman Experience**
   > *"Di tutorial, seluruh logika AJAX (seperti form modal, *debouncing*, dan manipulasi DOM) dicontohkan pada bagian Project. Bagaimana alur berpikir (*workflow*) yang tepat untuk mengadaptasi seluruh mekanisme asinkron tersebut agar dapat diterapkan dengan lancar ke halaman Experience?"*
   
   **Konteks & Tujuan:** Ditanyakan sebagai langkah persiapan sebelum mengimplementasikan instruksi tugas mandiri. Tujuannya adalah untuk memahami gambaran besar dan penyesuaian kode yang diperlukan (seperti perbedaan id DOM, penamaan variabel, dan *field* model) saat menduplikasi pendekatan *client-side* tersebut ke entitas portofolio yang berbeda.

#### Keterbatasan AI dan Pemahaman Saya

Dalam proses pengerjaan, AI cenderung memberikan solusi yang bersifat teoretis atau menebak-nebak jika tidak diberikan konteks kode yang mutlak. Misalnya, saat menangani kegagalan pengambilan data AJAX, AI awalnya mencurigai kesalahan sederhana pada rute URL. Saya harus melakukan pengecekan di tab *Network* pada *DevTools* secara mandiri, lalu menyertakan *traceback error* yang spesifik (`AttributeError`) agar AI dapat menemukan akar permasalahannya.

Selain itu, AI tidak memiliki pemahaman intrinsik mengenai kelogisan fungsi waktu (*common sense*). Pada kasus penentuan status penyelesaian (*Ongoing/Completed*), AI awalnya menganggap algoritma sudah valid karena variabel *datetime* sudah terisi di form, tanpa menyadari bahwa secara nalar, tanggal di masa depan belum dapat dianggap selesai. Hal ini menuntut saya untuk proaktif membantah hasil yang diberikan dan mengarahkan AI untuk menggunakan modul komparasi waktu nyata (`timezone.now()`). Pengalaman ini semakin menyadarkan saya bahwa kemampuan berpikir kritis dan validasi fungsional tetap menjadi tanggung jawab utama pengembang perangkat lunak, sementara AI lebih ideal diposisikan sebagai asisten penyusun sintaksis.

**Catatan kesesuaian dengan kode terbaru:** Pembahasan `timezone.now()` di bagian Tugas 5 di atas merupakan catatan pendekatan yang dibahas pada tahap tersebut. Pada versi kode saat ini, properti `Experience.is_ongoing` mengembalikan `ended_at is None`. Karena itu, tanggal selesai yang terisi dianggap Completed, termasuk jika tanggalnya masih di masa depan. Ringkasan Fitur Utama mengikuti perilaku model saat ini.

### Individual Assignment 6 & Pengembangan Filter Kategori

Pada tahap ini, saya menggunakan **ChatGPT** untuk membantu audit kode, integrasi edit melalui API, penambahan filter kategori, dan penyusunan dokumentasi. Saya memberikan dokumen Tutorial 07, Tugas 6, serta konteks proyek agar pembahasan tetap mengikuti materi yang diminta. Strategi prompting yang saya gunakan adalah membagi pengerjaan per tahap, meminta penjelasan sebelum perubahan, dan mempertahankan implementasi yang sudah sesuai.

**Bagian yang Dibantu AI:**

- Membantu memahami pembagian tanggung jawab model, serializer, permission, dan API view, serta mencocokkan alurnya dengan implementasi Experience yang sudah tersedia.
- Membantu menyusun logika penyimpanan edit melalui PATCH, mulai dari pengambilan nilai form, penyusunan payload JSON, pengiriman CSRF, hingga penanganan respons melalui toast, beserta perubahan kode yang diperlukan.
- Memberikan penjelasan mengenai perbedaan hak akses Project dan Experience agar pembatasan pada halaman edit tetap konsisten dengan permission API.
- Membantu menyusun logika penggabungan pencarian judul dan filter kategori melalui query parameter, termasuk mempertahankan kategori aktif saat daftar dimuat ulang setelah operasi AJAX.
- Memberikan alternatif penataan dropdown dan membantu menyesuaikan implementasinya agar lebih ringkas serta menyatu dengan kolom pencarian.

**Bagian yang Saya Kerjakan dan Putuskan Sendiri:**

- Menentukan urutan pengerjaan dan menjadikan Tutorial 07 serta checklist Tugas 6 sebagai acuan untuk menilai perubahan yang diperlukan.
- Meminta penjelasan tentang bagian kode yang sudah sesuai dan alasan penyesuaian, terutama perbedaan integrasi edit pada contoh tutorial dan bagian tugas.
- Memilih untuk mempertahankan halaman edit yang sudah ada dan menerapkan penyimpanan melalui API juga pada Project.
- Mengevaluasi alternatif tampilan filter dan mengarahkan revisinya: tetap menggunakan dropdown, mengurangi ruang yang dipakai, dan menempatkannya di sisi kanan pencarian.
- Menentukan penggunaan branch `feat/tugas-6-drf` dan menyimpan perubahan melalui commit bertahap setelah penjelasan perubahan tersedia.

#### AI Chat / Prompting Log

Contoh pertanyaan berikut dirangkum dari topik pengerjaan, bukan transkrip verbatim percakapan.

1. **Menyesuaikan serializer untuk model Experience**

   > *"Di Tutorial 07 contohnya pakai ProjectSerializer. Kalau diterapkan ke Experience, field apa saja yang perlu dimasukkan dan bagaimana supaya jumlah star serta status star pengguna tidak bisa diubah dari input API?"*

   **Konteks & Tujuan:** Digunakan untuk memahami penyesuaian `ModelSerializer` terhadap model Experience, penulisan field secara eksplisit, validasi teks dengan `strip_tags`, serta penggunaan `SerializerMethodField` untuk informasi star yang bersifat read-only.

2. **Menerapkan permission empat peran pada API**

   > *"Bagaimana cara membuat permission supaya pengunjung hanya bisa membaca, pengguna biasa bisa memberi star, Editor bisa mengedit Experience, tetapi hanya pemilik yang boleh menambah dan menghapus? Apa view lama juga perlu disesuaikan?"*

   **Konteks & Tujuan:** Digunakan untuk mencocokkan `IsPortfolioOwnerOrEditorOrReadOnly` dengan aturan Tugas 6 dan memastikan view lama tidak memberikan izin yang lebih luas. Endpoint star tetap memakai `IsAuthenticated` dan mengambil akun dari `request.user`.

3. **Mengubah penyimpanan form edit menjadi PATCH melalui fetch**

   > *"Halaman edit Experience saya masih submit POST ke view lama. Bagaimana cara mempertahankan form itu, tetapi menyimpan perubahan lewat PATCH ke API tanpa reload? Token CSRF dan pesan error 400 atau 403 ditangani di bagian mana?"*

   **Konteks & Tujuan:** Digunakan untuk menghubungkan halaman edit dengan endpoint detail DRF melalui payload JSON dan header `X-CSRFToken`, menampilkan respons lewat toast, serta mencegah pengiriman ganda selama request. Pola edit tersebut kemudian diterapkan juga pada Project dengan hak akses sesuai Tutorial 07.

4. **Menggabungkan filter kategori dengan pencarian AJAX**

   > *"Saya ingin menambahkan filter kategori Experience yang bisa dipakai bersamaan dengan pencarian judul. Bagaimana mengirim kedua query parameter ke API dan mempertahankan filter setelah memberi star atau menambah data? Dropdown-nya juga ingin dibuat kecil dan menyatu dengan kolom pencarian."*

   **Konteks & Tujuan:** Digunakan untuk mengembangkan filtering melalui `request.query_params` dan Django ORM tanpa membuat model baru. `fetchExperiences()` membaca kategori aktif setiap kali memuat daftar, sedangkan dropdown mengambil pilihan dari model dan ditempatkan di sisi kanan pencarian agar tampilannya tetap ringkas.

#### Keterbatasan AI dan Pemahaman Saya

Penjelasan dan susunan logika dari AI tetap perlu dicocokkan dengan struktur proyek. Pola Project tidak dapat diterapkan begitu saja ke Experience karena field dan hak aksesnya berbeda. Contohnya, Editor boleh melakukan PUT/PATCH pada Experience, sedangkan perubahan Project tetap dibatasi kepada pemilik. Dari pembahasan ini, saya memahami bahwa kesamaan alur request tidak berarti seluruh aturan kedua bagian harus disamakan.

Pada filter kategori, perubahan tidak cukup dilakukan pada dropdown saja. Nilainya harus diteruskan ke query parameter dan dibaca kembali setiap kali daftar dimuat ulang. Saya memahami bahwa jika kategori hanya dikirim saat dropdown berubah, hasil daftar setelah memberi star atau menambah data dapat kembali mengabaikan filter. Karena itu, logika kategori ditempatkan pada fungsi pemuatan daftar yang digunakan bersama oleh interaksi tersebut.

AI juga memberikan beberapa alternatif tampilan yang belum langsung sesuai dengan kebutuhan saya. Saya mengarahkan revisi agar pilihan tetap berbentuk dropdown dan tidak menambah baris kategori. Hal ini membantu saya membedakan logika yang sudah berfungsi dengan antarmuka yang nyaman digunakan. Pemeriksaan terbaru pada 9 November 2026 menghasilkan Django check tanpa masalah dan 25 test bawaan lulus. Filter kategori juga sudah diperiksa melalui browser desktop dan mobile. Hasil tersebut menjadi bukti untuk bagian yang telah diperiksa; seluruh interaksi edit per peran dan deployment akhir belum diperiksa ulang melalui browser. Dokumentasi dan jawaban reflektif yang dibantu AI tetap perlu saya baca ulang serta cocokkan dengan implementasi.
