import random

def substitusi(teks, kunci):
    hasil = ""
    
    # Mengimplementasikan Caesar cipher, sebuah teknik kriptografi substitusi sederhana
    '''
    Untuk setiap karakter dalam teks input :
- Jika karakter adalah huruf, geser sesuai dengan nilai kunci
- Jika huruf besar, gunakan ASCII 65-90 (A-Z)
- Jika huruf kecil, gunakan ASCII 97-122 (a-z)

    Rumus (ord(karakter) - base + kunci) % 26 + base digunakan untuk
    menggeser karakter, di mana base adalah 65 untuk huruf besar dan 97 untuk
    huruf kecil
    '''
    for karakter in teks:
        if karakter.isalpha():
            if karakter.isupper():
                hasil += chr((ord(karakter) - 65 + kunci) % 26 + 65) 
            else:
                hasil += chr((ord(karakter) - 97 + kunci) % 26 + 97)
        else:
            hasil += karakter
    return hasil

def blocking(teks, ukuran_blok):
    # Membagi teks menjadi blok-blok dengan ukuran tertentu
    # Menggunakan list comprehension untuk membuat daftar blok-blok teks
    return [teks[i:i+ukuran_blok] for i in range(0, len(teks), ukuran_blok)]

def permutasi(teks):
    # Memisahkan teks menjadi kata-kata
    kata_kata = teks.split()
    
    # Fungsi untuk membalikkan huruf dalam sebuah kata
    def balik_kata(kata):
        return kata[::-1]
    
    # Membalikkan setiap kata
    kata_kata_terbalik = [balik_kata(kata) for kata in kata_kata]
    
    # Menggabungkan kembali kata-kata menjadi teks
    teks_terbalik = ' '.join(kata_kata_terbalik)
    
    return teks_terbalik

def main():
    print("Program Kriptografi Sederhana")
    print("1. Substitusi")
    print("2. Blocking")
    print("3. Permutasi")
    
    pilihan = input("Pilih teknik kriptografi (1/2/3): ")
    
    if pilihan == "1":
        teks = input("Masukkan teks: ")
        kunci = int(input("Masukkan kunci (angka): "))
        hasil = substitusi(teks, kunci)
        print(f"Hasil enkripsi: {hasil}")
    
    elif pilihan == "2":
        teks = input("Masukkan teks: ")
        ukuran_blok = int(input("Masukkan ukuran blok: "))
        hasil = blocking(teks, ukuran_blok)
        print(f"Hasil blocking: {hasil}")
    
    elif pilihan == "3":
        teks = input("Masukkan teks: ")
        hasil = permutasi(teks)
        print(f"Hasil permutasi: {hasil}")
    
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()