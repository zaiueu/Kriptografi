def prepare_text(text):
    # Menghapus spasi berlebih dan konversi ke uppercase
    return ''.join(text.upper().split())

def create_blocks(text, block_size=4):
    # Membagi teks menjadi blok-blok
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

def encrypt_block(block):
    # Enkripsi satu blok dengan metode transposisi
    if len(block) < 4:
        block = block + 'X' * (4 - len(block))  # Padding dengan X
    return block[2] + block[3] + block[0] + block[1]

def decrypt_block(block):
    # Dekripsi satu blok dengan metode transposisi
    if len(block) < 4:
        return block  # Return as is if less than 4 characters
    return block[2] + block[3] + block[0] + block[1]

def encrypt(plaintext):
    # Proses enkripsi lengkap
    clean_text = prepare_text(plaintext)
    blocks = create_blocks(clean_text)
    encrypted_blocks = [encrypt_block(block) for block in blocks]
    return ' '.join(encrypted_blocks)

def decrypt(ciphertext):
    # Proses dekripsi lengkap
    blocks = ciphertext.split()
    decrypted_blocks = [decrypt_block(block) for block in blocks]
    return ''.join(decrypted_blocks)

# Testing dengan plaintext yang diberikan
plaintext = 'UNIVERSITAS ESA UNGGUL MERAIH AKREDITASI UNGGUL'
print("Plaintext:", plaintext)

# Enkripsi
encrypted = encrypt(plaintext)
print("\nHasil Enkripsi:", encrypted)

# Dekripsi
decrypted = decrypt(encrypted)
print("\nHasil Dekripsi:", decrypted)