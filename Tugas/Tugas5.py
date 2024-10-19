def caesar_encrypt(plaintext, key):
    """
    Fungsi untuk mengenkripsi teks menggunakan metode Caesar Cipher
    
    Args:
        plaintext (str): Teks yang akan dienkripsi
        key (int): Jumlah pergeseran (shift)
    
    Returns:
        str: Teks terenkripsi (ciphertext)
    """
    ciphertext = ""
    
    for char in plaintext:
        # Cek apakah karakter adalah huruf
        if char.isalpha():
            # Konversi ke kode ASCII
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Hitung pergeseran
            shifted = (ord(char) - ascii_offset + key) % 26
            # Konversi kembali ke karakter
            encrypted_char = chr(shifted + ascii_offset)
            ciphertext += encrypted_char
        else:
            # Jika bukan huruf, tambahkan langsung tanpa enkripsi
            ciphertext += char
    
    return ciphertext

def caesar_decrypt(ciphertext, key):
    """
    Fungsi untuk mendekripsi teks yang dienkripsi dengan Caesar Cipher
    
    Args:
        ciphertext (str): Teks terenkripsi yang akan didekripsi
        key (int): Jumlah pergeseran (shift)
    
    Returns:
        str: Teks terdekripsi (plaintext)
    """
    # Dekripsi sama dengan enkripsi dengan kunci negatif
    return caesar_encrypt(ciphertext, -key)

# Contoh penggunaan
if __name__ == "__main__":
    # Input dari pengguna
    plaintext = input("Masukkan teks yang akan dienkripsi: ")
    key = int(input("Masukkan kunci (angka): "))
    
    # Enkripsi
    encrypted_text = caesar_encrypt(plaintext, key)
    print(f"\nTeks terenkripsi: {encrypted_text}")
    
    # Dekripsi
    decrypted_text = caesar_decrypt(encrypted_text, key)
    print(f"Teks terdekripsi: {decrypted_text}")