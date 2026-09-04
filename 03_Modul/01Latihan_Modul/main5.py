import data_toko

print("===STRUK BELANJA TOKO DIEN===\n")
print(f"Nama Pembeli :{data_toko.keranjang['Nama_Pembeli']}")

total_barang = 0
for nomor,barang in enumerate(data_toko.keranjang["Items"], start=1):
    subtotal_perproduk = barang["harga"] * barang["jumlah"]
    total_barang = total_barang + subtotal_perproduk #atau ditulis seperti ini --> total_barang += subtotal_perproduk

    print(f"{nomor}.Produk : {barang['nama_produk']}  | Harga : {barang['harga']}  | Jumlah : {barang['jumlah']}  | Total Harga : {subtotal_perproduk}")



Total_keseluruhan = data_toko.hitung_total(data_toko.keranjang["Items"])
print(f"Total Belanja Keseluruhan : {Total_keseluruhan}")


# ini memanggil fungsi barang termahal dan mencetaknya
produk_mahal = data_toko.cari_barang_termahal(data_toko.keranjang["Items"])
print(f"Barang termahal adalah : {produk_mahal}")

#ini memanggil fungsi barang termurah dan mencetaknya
produk_murah = data_toko.cari_barang_termurah(data_toko.keranjang["Items"])
print(f"Barang termurah adalah : {produk_murah}")


uang_saya = 1500000
hasil_pencarian = data_toko.cari_sesuai_budget(data_toko.keranjang["Items"], uang_saya)

print(f"\n --- BARANG DENGAN HARGA DI BAWAH Rp {uang_saya} ---")
for barang in hasil_pencarian:
    print(f"- {barang['nama_produk']} : Rp {barang['harga']}")

#ini yang menjadi pembeda dengan main4.py
hasil_jumlah_beli = data_toko.cari_barang_berdasarkan_jumlah_beli(data_toko.keranjang["Items"])
print(f"\n -- BARANG BERDASARKAN JUMLAH BELI LEBIH DARI DUA ---")
for barang in hasil_jumlah_beli:
    print(f" - {barang['nama_produk']} : {barang['jumlah']}")

print("\n===TERIMA KASIH TELAH BERBELANJA DI TOKO DIEN===")
