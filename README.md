1. Menentukan bilangan terbesar dari tiga bilangan yang diinputkan:
Membuat flowchart yang menunjukkan alur logika untuk menentukan bilangan terbesar di antara tiga bilangan.
Implementasi kode Python untuk mengecek bilangan terbesar dari tiga input.
2. Menentukan bilangan terbesar dari N bilangan yang diinputkan:
Flowchart untuk menentukan bilangan terbesar dari sekumpulan N bilangan, di mana proses input berhenti ketika pengguna memasukkan angka 0.
Kode Python untuk mencari nilai terbesar dari N bilangan yang diinputkan hingga pengguna memasukkan 0 sebagai tanda berhenti.

1. FLOWCHART UNTUK MENENTUKAN BILANGAN TERBESAR DARI 3 BILANGAN
Tugas ini mengharuskan kita membuat flowchart yang akan membantu dalam menentukan bilangan terbesar dari tiga bilangan yang
diinputkan. Flowchart merupakan representasi visual dari algoritma atau proses yang digunakan untuk menyelesaikan masalah ini.

• LANGKAH-LANGKAH DALAM FLOWCHART:
► Mulai dari titik awal (start).
Minta pengguna untuk memasukkan tiga bilangan (misalnya bilangan A, B, dan Cl.
► Bandingkan ketiga bilangan tersebut:
Pertama, cek apakah bilangan A lebih besar dari B dan C. Jika benar, bilangan A adalah yang terbesar.
Jika tidak, cek apakah bilangan B lebih besar dari A dan C. Jika benar, bilangan B adalah yang terbesar.
Jika tidak ada yang memenuhi, berarti bilangan C adalah yang terbesar.
Hasil dari flowchart adalah bilangan terbesar dari tiga bilangan yang diinputkan.
Akhir flowchart (stop).

PENJELASAN KODE:
meminta untuk memasukan tiga bilangan, kemudian mengecek bilangan terbesar dengan struktur kondisional (if-else). kondisi pertama mengecek apakah A adalah terbesar. jika tidak,
akan dicek apakah B adalah yang terbesar. jika kedua kondisi tersebut salah, maka C adalah bilangan terbesar.

2. FLOWCHART UNTUK MENENTUKAN BILANGAN TERBESAR DARI N BILANGAN DENGAN INPUT 0 SEBAGAI PENANDA AKHIR
Latihan ini lebih dinamis karena jumlah bilangan yang akan dibandingkan tidak ditentukan secara spesifik. akan terus memasukkan bilangan hingga memasukkan angka O sebagai tanda bahwa mereka sudah selesai. Flowchart yang dibuat harus dapat menangani input yang bervariasi ini.

LANGKAH-LANGKAH DALAM FLOWCHART:
► Mulai dari titik awal (start).
► Minta pengguna memasukkan bilangan pertama. Set bilangan tersebut sebagai bilangan terbesar untuk sementara.
► Masukkan bilangan berikutnya:
▷ Jika bilangan yang dimasukkan adalah O, hentikan proses input.
▷ Jika tidak, bandingkan bilangan ini dengan bilangan terbesar sementara.
▷ Jika bilangan baru lebih besar, gantikan bilangan terbesar sementara dengan bilangan baru ini.
► Ulangi proses di atas hingga pengguna memasukkan O.
► Setelah selesai, tampilkan bilangan terbesar yang ditemukan.
► Akhiri flowchart (stop).

PENJELASAN KODE:
memulai dengan meminta input dari pengguna, yang kemudian disimpan sebagai bilangan terbesar sementara. Selanjutnya, dalam loop while, pengguna diminta untuk memasukkan bilangan satu per satu. Jika pengguna memasukkan O, proses berhenti (break). Setiap bilangan yang dimasukkan dibandingkan dengan bilangan terbesar sementara, dan jika lebih besar, nilai terbesar sementara di-update. Setelah pengguna selesai (memasukkan O), bilangan terbesar ditampilkan.

latihan ini memberikan pemahaman tentang bagaimana menentukan nilai terbesar dalam sekumpulan bilangan, baik dalam jumlah terbatas (3 bilangan) maupun dalam jumlah tidak tetap ( N bilangan dengan penghentian input menggunakan angka 0)



