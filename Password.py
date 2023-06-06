import random
import string
import tkinter as tk
from tkinter import messagebox
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = random.choices(characters, k=length)
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return ''.join(password)

def generate_password_button():
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def validate_password():
    password = password_entry.get()
    if (any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)):
        messagebox.showinfo("Validasi Password", "Password memenuhi persyaratan!")
        save_password(password)
    else:
        messagebox.showwarning("Validasi Password", "Password tidak memenuhi persyaratan!")

def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    messagebox.showinfo("Simpan Password", "Password telah disimpan!")

def view_passwords():
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
        if passwords:
            password_list = [password.strip() for password in passwords]
            listbox.delete(0, tk.END)
            for password in password_list:
                listbox.insert(tk.END, password)
        else:
            messagebox.showinfo("Daftar Password", "Tidak ada password yang tersimpan.")
    else:
        messagebox.showinfo("Daftar Password", "Tidak ada password yang tersimpan.")

def delete_password():
    selected_password = listbox.get(tk.ACTIVE)
    if selected_password:
        confirmation = messagebox.askyesno("Hapus Password", "Apakah Anda yakin ingin menghapus password ini?")
        if confirmation:
            listbox.delete(tk.ACTIVE)
            with open("passwords.txt", "r") as file:
                passwords = file.readlines()
            with open("passwords.txt", "w") as file:
                for password in passwords:
                    if password.strip() != selected_password:
                        file.write(password)
            messagebox.showinfo("Hapus Password", "Password telah dihapus.")
    else:
        messagebox.showwarning("Hapus Password", "Tidak ada password yang dipilih.")

# Membuat window Tkinter
window = tk.Tk()
window.title("Generator & Penyimpanan Password")

# Membuat label dan entry untuk panjang password
length_label = tk.Label(window, text="Panjang Password:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Membuat tombol untuk menghasilkan password
generate_button = tk.Button(window, text="Generate Password", command=generate_password_button)
generate_button.pack()

# Membuat label dan entry untuk menampilkan password
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window)
password_entry.pack()

# Membuat tombol untuk validasi password
validate_button = tk.Button(window, text="Validate Password", command=validate_password)
validate_button.pack()

# Membuat tombol untuk melihat password yang telah disimpan
view_button = tk.Button(window, text="View Passwords", command=view_passwords)
view_button.pack()

# Membuat listbox untuk menampilkan daftar password
listbox = tk.Listbox(window)
listbox.pack()

# Membuat tombol untuk menghapus password
delete_button = tk.Button(window, text="Delete Password", command=delete_password)
delete_button.pack()

# Menjalankan aplikasi
window.mainloop()
