import data_toko #untuk melakukan teknik modul ini atau memanggil data_toko.py harus di ctrl + S dulu untuk kedua fil nya agar bisa dijalankan

print("===STRUK BELANJA TOKO DIEN===\n")
print(f"Nama Pembeli : {data_toko.keranjang['Nama_Pembeli']}") #jangan lupa untuk memanggilnya seperti ini, karena keranjang itu ada di datatoko.py jadi harus memanggilnya dulu dengan data_toko.keranjang['Nama_Pembeli']

total_barang = 0 #supaya komputer ga bingung, kita inisialisasi dulu nilai awal nya 0 , supaya nanti di perulangannya jadi tidak berantakan
for nomor, barang in enumerate(data_toko.keranjang["Items"], start=1): #enumerate disini untuk menampilkan urutan angka di depan
    subtotal_perproduk = barang["harga"] * barang["jumlah"] 
    total_barang = total_barang + subtotal_perproduk
    
    print(f"{nomor}. Produk: {barang['nama_produk']} |  Harga satuan : {barang['harga']}  | Jumlah Beli : {barang['jumlah']}  | Subtotal :{subtotal_perproduk}")

print("-" * 50) #ini untuk membuat strip garis panjang serbanyak 50 kali
print(f"TOTAL YANG HARUS DIBAYAR :{total_barang}")

#CATATAN PENTING : RUN NYA DI FILE MAIN.PY ALWAYS.