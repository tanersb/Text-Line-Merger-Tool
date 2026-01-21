import tkinter as tk
from tkinter import messagebox

def birlestir():
    ham_metin = girdi_kutusu.get("1.0", tk.END)
    satirlar = [satir.strip() for satir in ham_metin.splitlines() if satir.strip()]
    duz_metin = " ".join(satirlar)
    sonuc_kutusu.delete("1.0", tk.END)
    sonuc_kutusu.insert(tk.END, duz_metin)

def kopyala():
    metin = sonuc_kutusu.get("1.0", tk.END).strip()
    if metin:
        pencere.clipboard_clear()
        pencere.clipboard_append(metin)
        pencere.update()
        kopyala_buton.config(text="Kopyalandı! ✔", bg="#d4edda")
        pencere.after(2000, buton_reset)
    else:
        messagebox.showwarning("Uyarı", "Kopyalanacak metin yok!")

def buton_reset():
    kopyala_buton.config(text="SONUCU KOPYALA", bg="#f0f0f0")

def temizle():
    girdi_kutusu.delete("1.0", tk.END)
    sonuc_kutusu.delete("1.0", tk.END)

pencere = tk.Tk()
pencere.title("Metin Satır Birleştirici")
pencere.geometry("500x600")

lbl_girdi = tk.Label(pencere, text="Alt alta olan metni buraya yapıştır:", font=("Arial", 10, "bold"))
lbl_girdi.pack(pady=(10, 5))

girdi_kutusu = tk.Text(pencere, height=10, width=50)
girdi_kutusu.pack(padx=10, pady=5)

frame_butonlar = tk.Frame(pencere)
frame_butonlar.pack(pady=10)

btn_cevir = tk.Button(frame_butonlar, text="DÜZ METNE ÇEVİR ⬇", command=birlestir, bg="#007bff", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
btn_cevir.pack(side=tk.LEFT, padx=5)

btn_temizle = tk.Button(frame_butonlar, text="Temizle", command=temizle, padx=10, pady=5)
btn_temizle.pack(side=tk.LEFT, padx=5)

lbl_sonuc = tk.Label(pencere, text="Sonuç (Tek Satır):", font=("Arial", 10, "bold"))
lbl_sonuc.pack(pady=(10, 5))

sonuc_kutusu = tk.Text(pencere, height=10, width=50)
sonuc_kutusu.pack(padx=10, pady=5)

kopyala_buton = tk.Button(pencere, text="SONUCU KOPYALA", command=kopyala, font=("Arial", 11), pady=10, width=40)
kopyala_buton.pack(pady=10)

pencere.mainloop()
