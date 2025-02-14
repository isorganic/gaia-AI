import requests
import random
import time

# Warna teks untuk terminal
MERAH = '\033[91m'
KUNING = '\033[93m'
RESET = '\033[0m'  # Reset warna

# Endpoint API
API_URL = "https://0xa31f3831xxxxxxxxxxxxxxx.gaia.domains/v1/chat/completions"

# Headers untuk permintaan
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Fungsi untuk membaca daftar pertanyaan dari file
def baca_pertanyaan(file_path):
    try:
        with open(file_path, "r") as file:
            pertanyaan = file.readlines()
        return [p.strip() for p in pertanyaan if p.strip()]  # Hapus baris kosong
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        return []

# Fungsi untuk mengirim pertanyaan ke API dan menampilkan jawaban
def kirim_pertanyaan(pertanyaan):
    payload = {
        "model": "gpt-3.5-turbo",  # Model yang digunakan (sesuaikan jika berbeda)
        "messages": [
            {"role": "user", "content": pertanyaan}
        ],
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 1
    }
    try:
        print(f"{MERAH}Mengirim pertanyaan: {pertanyaan}{RESET}")
        response = requests.post(API_URL, json=payload, headers=HEADERS)

        if response.status_code == 200:
            # Menampilkan respons dari API
            json_response = response.json()
            jawaban = json_response['choices'][0]['message']['content']
            print(f"{KUNING}Jawaban dari Chat AI:{RESET}")
            print(f"{KUNING}{jawaban}{RESET}")
        else:
            print(f"Error saat mengirim pertanyaan (Status: {response.status_code})")
            print(response.text)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi utama
def main():
    # Baca daftar pertanyaan dari file
    file_path = "tanya.txt"
    pertanyaan_list = baca_pertanyaan(file_path)

    if not pertanyaan_list:
        print("Daftar pertanyaan kosong. Pastikan file tanya.txt memiliki pertanyaan.")
        return

    print("Mulai mengirim pertanyaan secara otomatis...")
    while True:
        # Pilih pertanyaan secara acak
        pertanyaan = random.choice(pertanyaan_list)

        # Kirim pertanyaan dan tampilkan jawaban
        kirim_pertanyaan(pertanyaan)

        # Tunggu selama 1 menit sebelum mengirim pertanyaan berikutnya
        time.sleep(60)

# Jalankan script
if __name__ == "__main__":
    main()
