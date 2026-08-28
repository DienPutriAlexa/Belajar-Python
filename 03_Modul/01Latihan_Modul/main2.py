import data_toko

print("===STRUK BELANJA TOKO DIEN===\n")
print(f"Nama Pembeli :{data_toko.keranjang['Nama_Pembeli']}")

total_barang = 0
for nomor,barang in enumerate(data_toko.keranjang["Items"], start=1):
    subtotal_perproduk = barang["harga"] * barang["jumlah"]
    total_barang = total_barang + subtotal_perproduk #atau ditulis seperti ini --> total_barang += subtotal_perproduk

    print(f"{nomor}.Produk : {barang['nama_produk']}  | Harga : {barang['harga']}  | Jumlah : {barang['jumlah']}  | Total Harga : {subtotal_perproduk}")


# ini yang menjadi pembeda dengan latihan pada file main.py
#memanggil fungsi pada modul
Total_keseluruhan = data_toko.hitung_total(data_toko.keranjang["Items"])
print(f"Total Belanja Keseluruhan : {Total_keseluruhan}")