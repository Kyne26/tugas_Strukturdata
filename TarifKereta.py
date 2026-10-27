from tkinter import *

# deklarasi variable
tarif_dasar = 2000   # harga untuk jarak paling dekat 
batas_dasar = 5      # jarak yang masih masuk tarif dasar 
isi_blok = 3         # jarak tambahan dihitung per 3 km, dan 3 km itu disebut 1 blok
tarif_blok = 500     # tambahan harga untuk setiap blok 
jarak_maks = 1000    # batas atas jarak yang boleh dimasukkan (km)


# logikany
def hitung_tarif(jarak):
    total = tarif_dasar
    # ini maksudnya jarak yang melebihi batas dasar
    sisa = jarak - batas_dasar

    # loop berhenti kalau sisa sudah 0 atau minus
    while sisa > 0:
        # tiap putaran = 1 blok, jadi tambah Rp 500
        total = total + tarif_blok 
        # lalu kurangi sisa jarak sebesar 3 km  
        sisa = sisa - isi_blok       

        # btw kalau sisa tinggal 1 km, loop tetap jalan 1 kali lagi ( 1 > 0)
    return total


def format_rupiah(angka):
    # ubah 3500 jadi "3.500" supaya enak dibaca dan python formatny itu (,) jadi diubah ke (.)
    # format Python memakai koma (3,500), jadi koma-nya diganti titik
    return "{:,}".format(angka).replace(",", ".")


#logika tombolny
def tombol_hitung_diklik():
    # ambil apa yang diketik user di kotak input
    teks = kotak_jarak.get()

    # kalau user mengetik huruf (misal "abc"), float() akan error harus teks pokokny
    try:
        jarak = float(teks)
    except:
        hasil.config(text="Input tidak valid", fg=warna_error)
        return

    # jarak harus lebih dari 0 dan kurang dari jarak_maks
    if not (0 < jarak < jarak_maks):
        hasil.config(text="Input tidak valid", fg=warna_error)
        return

    total = hitung_tarif(jarak)

    hasil.config(text="Rp " + format_rupiah(total), fg=warna_teks)


# CUMAN STYLE BUKAN LOGIKA MASSSSSS
warna_kertas = "#ede7d6"   
warna_tiket = "#f8f4e8"    
warna_teks = "#1f1d1a"     
warna_aksen = "#c4501b"     
warna_aksen_gelap = "#9c3d12"
warna_redup = "#7a7467"   
warna_error = "#b3261e"

font_mesin = "Courier New" 

window = Tk()
window.title("Tarif Kereta")
window.config(bg=warna_kertas)
window.resizable(False, False)

lebar, tinggi = 560, 500
x = (window.winfo_screenwidth() - lebar) // 2
y = (window.winfo_screenheight() - tinggi) // 2
window.geometry(str(lebar) + "x" + str(tinggi) + "+" + str(x) + "+" + str(y))

tiket = Frame(window, bg=warna_tiket, highlightthickness=2,
              highlightbackground=warna_teks)
tiket.pack(fill="both", expand=True, padx=28, pady=(28, 12))

Label(tiket, text="Kalkulator\nTarif Kereta", font=(font_mesin, 24, "bold"),
      bg=warna_tiket, fg=warna_teks, justify="left").pack(anchor="w", padx=24, pady=(22, 14))

Label(tiket, text="JARAK TEMPUH (KM)", font=(font_mesin, 10, "bold"),
      bg=warna_tiket, fg=warna_redup).pack(anchor="w", padx=24)

kotak_jarak = Entry(tiket, font=(font_mesin, 22, "bold"), bg=warna_kertas,
                    fg=warna_teks, relief="flat", insertbackground=warna_teks,
                    highlightthickness=2, highlightbackground=warna_teks,
                    highlightcolor=warna_aksen)
kotak_jarak.pack(fill="x", padx=24, pady=(6, 14), ipady=6)
kotak_jarak.focus()

tombol = Button(tiket, text="HITUNG TARIF", font=(font_mesin, 13, "bold"),
                bg=warna_aksen, fg=warna_tiket, relief="flat", cursor="hand2",
                activebackground=warna_aksen_gelap, activeforeground=warna_tiket,
                command=tombol_hitung_diklik)
tombol.pack(fill="x", padx=24, ipady=8)

tombol.bind("<Enter>", lambda e: tombol.config(bg=warna_aksen_gelap))
tombol.bind("<Leave>", lambda e: tombol.config(bg=warna_aksen))

window.bind("<Return>", lambda e: tombol_hitung_diklik())

Label(tiket, text="TOTAL BAYAR", font=(font_mesin, 10, "bold"),
      bg=warna_tiket, fg=warna_redup).pack(anchor="w", padx=24, pady=(26, 0))

hasil = Label(tiket, text="Rp -", font=(font_mesin, 26, "bold"),
              bg=warna_tiket, fg=warna_redup)
hasil.pack(anchor="w", padx=24, pady=(2, 18))

keterangan = (str(batas_dasar) + " km pertama: Rp " + format_rupiah(tarif_dasar) + "\n"
              + "Tiap " + str(isi_blok) + " km berikutnya: +Rp " + format_rupiah(tarif_blok)
              + " (sisa dibulatkan)")
Label(window, text=keterangan, font=(font_mesin, 9), bg=warna_kertas,
      fg=warna_redup, justify="left").pack(anchor="w", padx=30, pady=(0, 14))

window.mainloop()
