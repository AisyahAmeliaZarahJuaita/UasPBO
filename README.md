# UasPBO
UAS PBO_KELOMPOK 10_KELAS A


Impor Modul:

Random: Digunakan untuk menghasilkan karakter acak dalam password.
string: Berisi kumpulan konstanta string, seperti huruf alfabet, digit, dan tanda baca.
tkinter: Library GUI standar untuk Python.
messagebox: Modul di dalam Tkinter untuk menampilkan kotak pesan (message box).
os: Digunakan untuk melakukan operasi pada sistem operasi, seperti memeriksa keberadaan file.


Fungsi generate_password(length):
Menghasilkan password acak dengan panjang length.
Karakter-karakter yang digunakan adalah kombinasi huruf (kapital dan kecil), angka, dan tanda baca.
Memastikan bahwa password yang dihasilkan memenuhi persyaratan: memiliki setidaknya satu huruf kecil, satu huruf kapital, satu angka, dan satu tanda baca.
Mengembalikan password yang dihasilkan dalam bentuk string.

Fungsi generate_password_button():
Dipanggil saat tombol "Generate Password" ditekan.
Mendapatkan panjang password dari input pengguna.
Memanggil fungsi generate_password() untuk menghasilkan password acak.
Memasukkan password ke dalam kotak input password di GUI.

Fungsi validate_password():
Dipanggil saat tombol "Validate Password" ditekan.
Mendapatkan password dari kotak input password di GUI.
Memvalidasi password dengan memeriksa apakah memenuhi persyaratan yang sama seperti di fungsi generate_password().
Menampilkan pesan informasi jika password memenuhi persyaratan.
Memanggil fungsi save_password() untuk menyimpan password jika memenuhi persyaratan.
Menampilkan pesan peringatan jika password tidak memenuhi persyaratan.

Fungsi save_password(password):
Menerima password yang akan disimpan.
Membuka file "passwords.txt" dalam mode append.
Menyimpan password ke dalam file.
Menampilkan pesan informasi bahwa password telah disimpan.

Fungsi view_passwords():
Dipanggil saat tombol "View Passwords" ditekan.
Memeriksa keberadaan file "passwords.txt".
Jika file tersebut ada, membuka file dan membaca semua baris yang berisi password. Jika ada password yang terbaca, menghapus semua item pada listbox dan menambahkan password-password ke dalam listbox. Jika tidak ada password yang terbaca, menampilkan pesan informasi bahwa tidak ada password yang tersimpan.

Fungsi delete_password():
Dipanggil saat tombol "Delete Password" ditekan.
Mendapatkan password yang dipilih dari listbox.
Memunculkan kotak dialog konfirmasi untuk menghapus password.
Jika pengguna mengkonfirmasi penghapusan, menghapus password dari listbox dan dari file "passwords.txt".

Pembuatan Window Tkinter:
Membuat instance objek window sebagai window utama dengan menggunakan class Tk() dari modul tkinter.
Mengatur judul window menggunakan metode title() pada objek window.

Membuat Label dan Entry untuk Panjang Password:
Membuat objek length_label sebagai label untuk teks "Panjang Password" menggunakan class Label dari modul tkinter.
Menambahkan label ke dalam window menggunakan metode pack().
Membuat objek length_entry sebagai kotak input untuk panjang password menggunakan class Entry dari modul tkinter.
Menambahkan kotak input ke dalam window menggunakan metode pack().

Membuat Tombol "Generate Password":
Membuat objek generate_button sebagai tombol dengan teks "Generate Password" menggunakan class Button dari modul tkinter.
Mengatur perintah yang akan dijalankan saat tombol ditekan dengan menghubungkannya ke fungsi generate_password_button().
Menambahkan tombol ke dalam window menggunakan metode pack().

Membuat Label dan Entry untuk Menampilkan Password:
Membuat objek password_label sebagai label untuk teks "Password" menggunakan class Label dari modul tkinter.
Menambahkan label ke dalam window menggunakan metode pack().
Membuat objek password_entry sebagai kotak input untuk menampilkan password menggunakan class Entry dari modul tkinter.
Menambahkan kotak input ke dalam window menggunakan metode pack().

Membuat Tombol "Validate Password":
Membuat objek validate_button sebagai tombol dengan teks "Validate Password" menggunakan class Button dari modul tkinter.
Mengatur perintah yang akan dijalankan saat tombol ditekan dengan menghubungkannya ke fungsi validate_password().
Menambahkan tombol ke dalam window menggunakan metode pack().

Membuat Tombol "View Passwords":
Membuat objek view_button sebagai tombol dengan teks "View Passwords" menggunakan class Button dari modul tkinter.
Mengatur perintah yang akan dijalankan saat tombol ditekan dengan menghubungkannya ke fungsi view_passwords().
Menambahkan tombol ke dalam window menggunakan metode pack().

Membuat Listbox untuk Menampilkan Daftar Password:
Membuat objek listbox sebagai listbox menggunakan class Listbox dari modul tkinter.
Menambahkan listbox ke dalam window menggunakan metode pack().

Membuat Tombol "Delete Password":
Membuat objek delete_button sebagai tombol dengan teks "Delete Password" menggunakan class Button dari modul tkinter.
Mengatur perintah yang akan dijalankan saat tombol ditekan dengan menghubungkannya ke fungsi delete_password().
Menambahkan tombol ke dalam window menggunakan metode pack().

Menjalankan Aplikasi:
Menggunakan metode mainloop() pada objek window untuk menjalankan aplikasi GUI.
Metode ini akan menjaga aplikasi tetap berjalan sampai window ditutup oleh pengguna
Dalam fungsi delete_password(), setelah menghapus password dari listbox, kita membuka file "passwords.txt" dalam mode membaca ("r") untuk membaca semua baris yang berisi password.

Selanjutnya, kita membuka file "passwords.txt" dalam mode menulis ("w") untuk menulis ulang isi file. Kita menulis ulang semua baris password kecuali baris yang berisi password yang dihapus. Terakhir, kita menampilkan pesan informasi bahwa password telah dihapus menggunakan messagebox.showinfo(). Setelah semua bagian kode di atas, program akan membuat window Tkinter dengan elemen-elemen GUI seperti label, kotak input, tombol, dan listbox. Ketika tombol "Generate Password" ditekan, akan dihasilkan password acak sesuai panjang yang diinputkan. Tombol "Validate Password" akan memvalidasi password yang dimasukkan dan menampilkan pesan sesuai dengan persyaratan. Tombol "View Passwords" akan membaca file "passwords.txt" dan menampilkan daftar password yang disimpan dalam listbox. Tombol "Delete Password" akan menghapus password yang dipilih dari listbox dan file "passwords.txt".

Program ini memberikan fitur sederhana untuk menghasilkan dan menyimpan password, serta memvalidasi dan menghapus password. Namun, program ini tidak melibatkan enkripsi atau keamanan tambahan lainnya.
