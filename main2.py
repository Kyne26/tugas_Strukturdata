# Kalkulator Tarif Kereta (versi CLI)

# ====== ATURAN TARIF ======
tarif_dasar = 2000   # harga untuk jarak paling dekat
batas_dasar = 5      # jarak (km) yang masih masuk tarif dasar
isi_blok = 3         # tiap 3 km tambahan dihitung 1 blok
tarif_blok = 500     # tambahan harga untuk setiap blok
jarak_maks = 1000    # batas atas jarak yang boleh dimasukkan (km)


# ====== FUNGSI HITUNG TARIF ======
def hitung_tarif(jarak):
    total = tarif_dasar
    sisa = jarak - batas_dasar   # jarak yang melebihi batas dasar

    # selama masih ada sisa jarak, tambah 1 blok
    while sisa > 0:
        total = total + tarif_blok
        sisa = sisa - isi_blok   # sisa 1 km pun tetap dihitung 1 blok

    return total


# ubah 3500 jadi "3.500" supaya enak dibaca
def format_rupiah(angka):
    return "{:,}".format(angka).replace(",", ".")


# ====== PROGRAM UTAMA ======
print("=== KALKULATOR TARIF KERETA ===")
print(str(batas_dasar) + " km pertama: Rp " + format_rupiah(tarif_dasar))
print("Tiap " + str(isi_blok) + " km berikutnya: +Rp " + format_rupiah(tarif_blok)
      + " (sisa dibulatkan)")
print()

teks = input("Masukkan jarak tempuh (km): ")

# kalau user mengetik huruf (misal "abc"), float() akan error
try:
    jarak = float(teks)
except ValueError:
    print("Input tidak valid")
    exit()

# jarak harus lebih dari 0 dan kurang dari jarak_maks
if not (0 < jarak < jarak_maks):
    print("Input tidak valid")
    exit()

total = hitung_tarif(jarak)
print("Total bayar: Rp " + format_rupiah(total))