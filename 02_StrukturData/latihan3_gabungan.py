keranjang = {
    "Nama_Pembeli" : "Dien",
    "Items":[
        {
            "nama_produk" : "Sepatu Adidas",
            "harga" : 1000000,
            "jumlah" : 3
        },
        {
           "nama_produk" : "Sweater Stone Island",
           "harga" : 8000000,
           "jumlah" : 2
        },
        {
            "nama_produk" : "Lafiye Hijab",
            "harga" : 200000,
            "jumlah" : 4
        },
        {
            "nama_produk" : "Fjalraven Kanken",
            "harga" : 1200000,
            "jumlah" : 2
        },
        {
            "nama_produk" : "Iphone",
            "harga" : 10000000,
            "jumlah" : 2
        }
    ]  
}



print("===STRUK BELANJA TOKO DIEN===\n")
print(f"Nama Pembeli : {keranjang['Nama_Pembeli']}")

total_barang = 0 #supaya komputer ga bingung, kita inisialisasi dulu nilai awal nya 0 , supaya nanti di perulangannya jadi tidak berantakan
for nomor, barang in enumerate(keranjang["Items"], start=1): #enumerate disini untuk menampilkan urutan angka di depan
    subtotal_perproduk = barang["harga"] * barang["jumlah"] 
    total_barang = total_barang + subtotal_perproduk
    
    print(f"{nomor}. Produk: {barang['nama_produk']} |  Harga satuan : {barang['harga']}  | Jumlah Beli : {barang['jumlah']}  | Subtotal :{subtotal_perproduk}")

print("-" * 50) #ini untuk membuat strip garis panjang serbanyak 50 kali
print(f"TOTAL YANG HARUS DIBAYAR :{total_barang}")