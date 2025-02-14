# Panduan Instalasi dan Penggunaan Gaia-AI

## Pendahuluan
Gaia-AI adalah proyek open-source yang memungkinkan interaksi dengan model AI melalui API. Repositori ini berisi skrip yang dapat digunakan untuk mengajukan pertanyaan secara otomatis dan mendapatkan respons AI.

## Persyaratan
Sebelum menginstal dan menjalankan Gaia-AI, pastikan Anda memiliki:
- Sistem operasi Linux atau macOS (Windows bisa menggunakan WSL)
- Python 3.x terinstal
- Git terinstal

## Instalasi
1. **Clone repositori**
   ```sh
   git clone https://github.com/isorganic/gaia-AI.git
   ```
2. **Masuk ke direktori proyek**
   ```sh
   cd gaia-AI
   ```
3. **Instal dependensi**
 
## Konfigurasi Endpoint
Secara default, Gaia-AI menggunakan endpoint tertentu untuk berkomunikasi dengan model AI. Anda dapat menggantinya sesuai dengan endpoint (Alamat chat AI sesuai node masing-masing) node Anda sendiri.

1. **Buka file konfigurasi atau skrip yang berisi endpoint**
   ```sh
   nano main.py
   ```
2. **Temukan baris yang berisi endpoint API, misalnya:**
   ```python
   API_URL = "https://0xa31f3831dcad635c9e1db81b6ee868715dcce1e0.gaia.domains/v1/chat/completions"
   ```
3. **Ganti dengan endpoint Anda sendiri, misalnya:**
   ```python
   API_URL = "https://0xa31f3831dcad635c9e1db81b6ee868715dcce1e0.gaia.domains/v1/chat/completions"
   ```
4. **Simpan perubahan dan keluar dari editor** (jika menggunakan nano, tekan `CTRL+X`, lalu `Y`, lalu `Enter`).

## Menjalankan Skrip
Setelah konfigurasi selesai, jalankan Gaia-AI dengan perintah berikut:
```sh
python3 main.py
```
Jika Anda menggunakan virtual environment, pastikan telah mengaktifkannya sebelum menjalankan skrip.

## Troubleshooting
Jika mengalami masalah saat menjalankan Gaia-AI:
- Pastikan koneksi internet stabil
- Periksa apakah endpoint API yang digunakan aktif dan benar
- Pastikan dependensi sudah terinstal dengan benar


Semoga bermanfaat! 🚀

