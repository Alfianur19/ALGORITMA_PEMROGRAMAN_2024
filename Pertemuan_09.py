# Minta input pengeluaran dari pengguna
nominal = float(input("Masukkan nominal pengeluaran: "))

# Tentukan kategori pengeluaran
if nominal <= 500:
    kategori = "Rendah"
elif nominal <= 1500:
    kategori = "Sedang"
else:
    kategori = "Tinggi"

# Tampilkan kategori pengeluaran
print(f"Kategori pengeluaran: {kategori}")
