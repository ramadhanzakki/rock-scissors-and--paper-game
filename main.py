import random
import os
import time

# --- Konstanta untuk mempermudah ---
# Dictionary untuk mengubah input singkat menjadi kata lengkap
PILIHAN = {
    "r": "Batu 🗿",
    "p": "Kertas 📄",
    "s": "Gunting ✂️"
}
# Skor kemenangan yang harus dicapai
SKOR_MENANG = 3

# --- Fungsi-fungsi Bantuan ---

def bersihkan_layar():
    """Membersihkan layar terminal agar tampilan lebih rapi."""
    # 'nt' adalah untuk Windows, selain itu (Linux/Mac) menggunakan 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def dapatkan_pilihan_pemain(nama_pemain):
    """Meminta input dari pemain dan memvalidasinya."""
    while True:
        pilihan = input(f"{nama_pemain}, masukkan pilihanmu (r/p/s): ").lower()
        if pilihan in PILIHAN:
            return pilihan
        else:
            print("Input tidak valid! Harap masukkan 'r' untuk Batu, 'p' untuk Kertas, atau 's' untuk Gunting.")

def tentukan_pemenang(pilihan1, pilihan2):
    """Menentukan pemenang ronde berdasarkan dua pilihan. Mengembalikan 'pemain1', 'pemain2', atau 'seri'."""
    if pilihan1 == pilihan2:
        return "seri"
    
    # Kombinasi kemenangan untuk pemain 1
    kombinasi_menang = [("r", "s"), ("s", "p"), ("p", "r")]
    
    if (pilihan1, pilihan2) in kombinasi_menang:
        return "pemain1"
    else:
        return "pemain2"

def tampilkan_hasil_ronde(pemenang, nama1, pilihan1, nama2, pilihan2, skor1, skor2):
    """Menampilkan hasil dari satu ronde permainan."""
    print("\n--- Hasil Ronde ---")
    print(f"{nama1} memilih: {PILIHAN[pilihan1]}")
    print(f"{nama2} memilih: {PILIHAN[pilihan2]}")
    
    if pemenang == "seri":
        print("Hasilnya SERI! 🤝")
    elif pemenang == "pemain1":
        print(f"{nama1} MENANG ronde ini! 🎉")
    else:
        print(f"{nama2} MENANG ronde ini! 🎉")
        
    print(f"Skor Saat Ini -> {nama1}: {skor1} | {nama2}: {skor2}")
    print("-------------------\n")
    time.sleep(2) # Beri jeda 2 detik agar pemain bisa membaca hasil

# --- Mode Permainan Utama ---

def mainkan_lawan_komputer():
    """Logika utama untuk permainan melawan komputer."""
    skor_pemain = 0
    skor_komputer = 0
    
    while skor_pemain < SKOR_MENANG and skor_komputer < SKOR_MENANG:
        bersihkan_layar()
        print("=== ⚔️ ANDA vs KOMPUTER 🤖 ===")
        print(f"Skor: Anda {skor_pemain} - {skor_komputer} Komputer")
        
        pilihan_pemain = dapatkan_pilihan_pemain("Anda")
        pilihan_komputer = random.choice(list(PILIHAN.keys()))
        
        pemenang = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
        
        if pemenang == "pemain1":
            skor_pemain += 1
        elif pemenang == "pemain2":
            skor_komputer += 1
            
        tampilkan_hasil_ronde(pemenang, "Anda", pilihan_pemain, "Komputer", pilihan_komputer, skor_pemain, skor_komputer)
        
    bersihkan_layar()
    if skor_pemain > skor_komputer:
        print("🏆 SELAMAT, ANDA MEMENANGKAN PERTANDINGAN! 🏆")
    else:
        print("😭 YAH, ANDA KALAH. COBA LAGI! 😭")
    print(f"Skor Akhir: Anda {skor_pemain} - {skor_komputer} Komputer\n")

def mainkan_dua_pemain():
    """Logika utama untuk permainan dua pemain."""
    skor_pemain1 = 0
    skor_pemain2 = 0
    
    while skor_pemain1 < SKOR_MENANG and skor_pemain2 < SKOR_MENANG:
        bersihkan_layar()
        print("=== 🧑 PEMAIN 1 vs PEMAIN 2 🧑 ===")
        print(f"Skor: Pemain 1 [{skor_pemain1}] - [{skor_pemain2}] Pemain 2")

        pilihan_pemain1 = dapatkan_pilihan_pemain("Pemain 1")
        
        # Bersihkan layar agar pemain 2 tidak melihat pilihan pemain 1
        bersihkan_layar()
        print("=== 🧑 PEMAIN 1 vs PEMAIN 2 🧑 ===")
        print(f"Skor: Pemain 1 [{skor_pemain1}] - [{skor_pemain2}] Pemain 2")
        print("Pemain 1 sudah memilih. Sekarang giliran Pemain 2!")
        
        pilihan_pemain2 = dapatkan_pilihan_pemain("Pemain 2")
        
        pemenang = tentukan_pemenang(pilihan_pemain1, pilihan_pemain2)
        
        if pemenang == "pemain1":
            skor_pemain1 += 1
        elif pemenang == "pemain2":
            skor_pemain2 += 1
            
        tampilkan_hasil_ronde(pemenang, "Pemain 1", pilihan_pemain1, "Pemain 2", pilihan_pemain2, skor_pemain1, skor_pemain2)
        
    bersihkan_layar()
    if skor_pemain1 > skor_pemain2:
        print("🏆 SELAMAT, PEMAIN 1 MEMENANGKAN PERTANDINGAN! 🏆")
    else:
        print("🏆 SELAMAT, PEMAIN 2 MEMENANGKAN PERTANDINGAN! 🏆")
    print(f"Skor Akhir: Pemain 1 [{skor_pemain1}] - [{skor_pemain2}] Pemain 2\n")

# --- Program Utama ---

def main():
    """Fungsi utama untuk menjalankan seluruh program."""
    while True:
        bersihkan_layar()
        print("=========================================")
        print("   SELAMAT DATANG DI GAME BATU GUNTING KERTAS   ")
        print("=========================================")
        print("Pilih mode permainan:")
        print("1. Lawan Komputer (c)")
        print("2. Dua Pemain (f)")
        
        mode = input("Pilihanmu (c/f): ").lower()
        
        if mode == 'c':
            mainkan_lawan_komputer()
        elif mode == 'f':
            mainkan_dua_pemain()
        else:
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(1)
            continue
            
        main_lagi = input("Apakah kamu ingin bermain lagi? (y/n): ").lower()
        if main_lagi != 'y':
            print("\nTerima kasih sudah bermain! Sampai jumpa lagi! 👋")
            break

# Jalankan program utama
if __name__ == "__main__":
    main()