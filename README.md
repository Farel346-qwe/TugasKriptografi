Implementasi Algoritma RC4 (Stream Cipher) - Python

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![Topic](https://img.shields.io/badge/topic-Cryptography-orange)

Proyek ini berisi implementasi algoritma kriptografi **RC4 (Rivest Cipher 4)** dari nol (*from scratch*) menggunakan bahasa pemrograman Python. Dibuat untuk memenuhi tugas mata kuliah **Keamanan Data dan Informasi**.

📌 Tentang RC4
RC4 adalah algoritma *symmetric key stream cipher* yang dirancang oleh Ron Rivest pada tahun 1987. Algoritma ini memproses data byte demi byte (stream) dan dikenal karena kesederhanaan serta kecepatannya dalam enkripsi/dekripsi.

> Catatan: RC4 saat ini sudah dianggap tidak aman untuk standar industri modern (RFC 7465), namun sangat relevan untuk dipelajari sebagai dasar pemahaman mekanisme *stream cipher*.

⚙️ Cara Kerja Algoritma
Implementasi ini mencakup tiga komponen utama sesuai dengan standar algoritma RC4:

1.  KSA (Key Scheduling Algorithm): Menginisialisasi dan melakukan permutasi pada S-Box (array 256 byte) berdasarkan kunci rahasia yang diberikan.
2.  PRGA (Pseudo-Random Generation Algorithm): Menghasilkan aliran kunci (keystream) secara dinamis dengan terus melakukan swap pada elemen S-Box.
3.  XOR Operation: Melakukan substitusi antara plaintext dan keystream menggunakan operator bitwise XOR (^).



🚀 Fitur Kode
- Murni Tanpa Library: Tidak menggunakan library kriptografi eksternal (menggunakan logika matematika dasar).
- Simetris: Menggunakan fungsi yang sama untuk proses Enkripsi dan Dekripsi.
- Output Hexadecimal: Menampilkan hasil enkripsi dalam format Hex agar mudah dibaca.

 💻 Cara Penggunaan
Pastikan Anda sudah menginstal Python di sistem Anda, kemudian jalankan perintah berikut:
