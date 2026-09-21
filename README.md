# Individual Assignment: Personal Portfolio Website

Website portofolio pribadi milik **Azzam Zawawi Al Rasyid**, dikembangkan menggunakan **Django** sebagai bagian dari tugas mata kuliah **Pemrograman Berbasis Platform (CSGE602022)**, Fakultas Ilmu Komputer, Universitas Indonesia.

**Nama:** Azzam Zawawi Al Rasyid  
**NPM:** 2506618723  
**Kelas:** PBP A  
**Tautan PWS:** [azzam-zawawi-myportofolio.pws.cs.ui.ac.id](https://azzam-zawawi-myportofolio.pws.cs.ui.ac.id)

---

## Deskripsi Proyek

Website ini merupakan portofolio pribadi berbasis Django yang menerapkan pola arsitektur **Model-View-Template (MVT)**. Proyek ini dibangun secara bertahap sepanjang semester, dimulai dari halaman statis HTML5/CSS3, kemudian dilanjutkan dengan integrasi database melalui Django ORM, dan terakhir penambahan fitur Form serta Data Delivery (JSON).

Tampilan portofolio mengusung desain *clean-modern* dengan palet warna biru muda yang lembut, tipografi **Space Grotesk** untuk judul, dan sistem *layout* responsif menggunakan CSS Grid dan Flexbox.

---

## Fitur Utama

- **Profile & Hero Section:** Menampilkan identitas personal (nama, NPM, program studi), foto, bio singkat, serta tautan GitHub, LinkedIn, dan Email.
- **Dynamic Experience Page (`/experience/`):**
  - Merender data riwayat kegiatan dan kepanitiaan dari database.
  - Menerapkan tata letak *zigzag* (selang-seling) otomatis menggunakan tag Django `{% cycle '' 'reverse' %}` yang dipadukan dengan CSS `flex-direction: row-reverse`.
  - Dilengkapi fitur **pencarian** berdasarkan judul, tombol **Tambah**, **Edit**, dan **Hapus** dengan modal konfirmasi.
  - Menampilkan status **Ongoing** / **Completed** secara otomatis berdasarkan `ended_at`.
- **Dynamic Project Page (`/project/`):**
  - Menampilkan daftar proyek dalam bentuk **grid kartu** dengan efek *hover* (lift + zoom gambar).
  - Setiap kartu memiliki gambar *thumbnail*, kategori, judul, deskripsi, serta tombol Edit dan Hapus.
  - Dilengkapi fitur pencarian, form tambah, dan modal konfirmasi hapus.
- **JSON Data Delivery:**
  - Endpoint `/api/experience/` dan `/api/project/` mengembalikan data mentah berformat JSON.
  - Mendukung filter berdasarkan judul melalui query parameter `?title=`.
- **Proteksi PIN Sederhana:**
  - Form Create/Edit dan aksi Delete dilindungi oleh kolom **PIN rahasia** yang divalidasi di sisi server melalui `clean_secret_passcode()` pada `forms.py` dan pengecekan di `views.py`.
- **Responsive Design:**
  - Layout otomatis menyesuaikan pada layar kecil (mobile) melalui media query `@media (max-width: 600px)`.
- **Skeleton Template (`base.html`):**
  - Navbar dan footer konsisten di seluruh halaman melalui sistem `{% extends %}`.

---

## Teknologi yang Digunakan

- **Backend:** Django 5.2, Python
- **Database:** SQLite (development), PostgreSQL (production di PWS)
- **Frontend:** HTML5, CSS3 (Grid, Flexbox, Custom Properties), Django Template Language
- **Deployment:** Pacil Web Service (PWS)
- **Version Control:** Git & GitHub

---

## Cara Menjalankan Proyek Secara Lokal

1. **Clone repositori:**
   ```bash
   git clone https://github.com/AzzamZR/myportofolio.git
   cd myportofolio
   ```

2. **Buat dan aktifkan virtual environment:**
   ```bash
   python -m venv env
   # Windows:
   .\env\Scripts\Activate.ps1
   # macOS/Linux:
   source env/bin/activate
   ```

3. **Pasang dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Terapkan migrasi database:**
   ```bash
   python manage.py migrate
   ```

5. **Jalankan server pengembangan:**
   ```bash
   python manage.py runserver
   ```

6. **Buka browser** dan akses `http://localhost:8000/`.

---

## Struktur Folder

```
myportofolio/
├── env/
├── .git/
├── .gitignore
├── requirements.txt
├── db.sqlite3
├── manage.py
├── main/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py          # ExperienceForm & ProjectForm
│   ├── models.py         # Model Experience & Project
│   ├── tests.py
│   ├── urls.py           # Routing aplikasi main
│   └── views.py          # Seluruh logika view
├── portofolio/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       └── Foto.JPG
└── templates/
    ├── base.html
    ├── index.html
    ├── experience.html
    ├── experience_form.html
    ├── project.html
    ├── project_form.html
    └── components/
        ├── experience_delete_modal.html
        └── project_delete_modal.html
```

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
