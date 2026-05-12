import tkinter as tk
from tkinter import messagebox
import os

kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"
buyuk_harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakamlar = "0123456789"
semboller = "!@#$%&*?"

def parola_uret():
    try:
        uzunluk = int(uzunluk_giris.get())
    except:
        messagebox.showerror("Hata", "Sayı gir")
        return

    if uzunluk < 4:
        messagebox.showerror("Hata", "En az 4 olmalı")
        return

    tum_karakterler = ""
    parola = ""

    if kucuk_var.get():
        tum_karakterler += kucuk_harfler
        parola += kucuk_harfler[os.urandom(1)[0] % len(kucuk_harfler)]

    if buyuk_var.get():
        tum_karakterler += buyuk_harfler
        parola += buyuk_harfler[os.urandom(1)[0] % len(buyuk_harfler)]

    if rakam_var.get():
        tum_karakterler += rakamlar
        parola += rakamlar[os.urandom(1)[0] % len(rakamlar)]

    if sembol_var.get():
        tum_karakterler += semboller
        parola += semboller[os.urandom(1)[0] % len(semboller)]

    if tum_karakterler == "":
        messagebox.showerror("Hata", "Seçim yap")
        return

    while len(parola) < uzunluk:
        parola += tum_karakterler[os.urandom(1)[0] % len(tum_karakterler)]

    sonuc.delete(0, tk.END)
    sonuc.insert(0, parola)


pencere = tk.Tk()
pencere.title("Parola Üretici")
pencere.geometry("400x350")

tk.Label(pencere, text="Parola uzunluğu").pack()
uzunluk_giris = tk.Entry(pencere)
uzunluk_giris.pack()
uzunluk_giris.insert(0, "12")

kucuk_var = tk.BooleanVar(value=True)
buyuk_var = tk.BooleanVar(value=True)
rakam_var = tk.BooleanVar(value=True)
sembol_var = tk.BooleanVar(value=True)

tk.Checkbutton(pencere, text="Küçük harf", variable=kucuk_var).pack()
tk.Checkbutton(pencere, text="Büyük harf", variable=buyuk_var).pack()
tk.Checkbutton(pencere, text="Rakam", variable=rakam_var).pack()
tk.Checkbutton(pencere, text="Sembol", variable=sembol_var).pack()

tk.Button(pencere, text="Üret", command=parola_uret).pack(pady=10)

sonuc = tk.Entry(pencere, width=30)
sonuc.pack()

pencere.mainloop()