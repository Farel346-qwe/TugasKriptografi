def rc4_ksa(key):
    """
    #Tahap 1: Key Scheduling Algorithm (KSA)
    Tujuan: Melakukan PERMUTASI pada array S berdasarkan kunci rahasia.
    """
    key_length = len(key)
    # Inisialisasi array S dengan angka 0-255
    S = list(range(256)) 
    
    j = 0
    for i in range(256):
        # Rumus pengacakan posisi (Permutasi)
        j = (j + S[i] + key[i % key_length]) % 256
        # Tukar posisi (Swap)
        S[i], S[j] = S[j], S[i]
        
    return S

def rc4_prga(S):
    """
    Tahap 2: Pseudo-Random Generation Algorithm (PRGA)
    Tujuan: Menghasilkan aliran kunci (Keystream) secara terus-menerus.
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        # Tukar posisi lagi agar S-Box terus berubah (Dinamis)
        S[i], S[j] = S[j], S[i]
        
        # Ambil nilai substitusi dari S-Box
        t = (S[i] + S[j]) % 256
        k = S[t]
        yield k # Mengembalikan 1 byte keystream

def rc4_process(data, key):
    """
    Tahap 3: Enkripsi/Dekripsi
    Tujuan: Menggabungkan data dengan keystream menggunakan XOR.
    """
    # Ubah kunci dan data menjadi angka (byte)
    key_bytes = [ord(c) for c in key]
    data_bytes = [ord(c) for c in data]
    
    # Jalankan KSA
    S = rc4_ksa(key_bytes)
    
    # Jalankan PRGA
    keystream = rc4_prga(S)
    
    res = []
    for char_byte in data_bytes:
        # Lakukan SUBSTUSI dengan operasi XOR (Plaintext XOR Keystream)
        # next(keystream) mengambil 1 byte angka acak berikutnya
        processed_byte = char_byte ^ next(keystream)
        res.append(processed_byte)
        
    return res

# --- DEMO PENGGUNAAN ---
if __name__ == "__main__":
    plaintext = "HALO TEKNIK"
    key_secret = "KOPI"

    print(f"Pesan Asli: {plaintext}")
    print(f"Kunci: {key_secret}\n")

    # --- PROSES ENKRIPSI ---
    cipher_bytes = rc4_process(plaintext, key_secret)
    # Ubah ke format Hex agar mudah dibaca (karena ciphertext biasanya karakter aneh)
    hex_cipher = ''.join([f'{b:02x}' for b in cipher_bytes])
    print(f"Hasil Enkripsi (Hex): {hex_cipher}")

    # --- PROSES DEKRIPSI ---
    # Ubah kembali bytes hasil dekripsi menjadi karakter string
    # Kita kirim cipher_bytes (hasil enkripsi) ke fungsi yang sama
    decrypted_bytes = rc4_process(''.join([chr(b) for b in cipher_bytes]), key_secret)
    decrypted_text = ''.join([chr(b) for b in decrypted_bytes])
    print(f"Hasil Dekripsi: {decrypted_text}")