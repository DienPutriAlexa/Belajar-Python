keranjang = {
    "Nama_Pembeli" : "Dien",
    "Items" : [
        {
            "Nama_Produk": "Polo shirt",
            "harga" : "250000",
            "jumlah" : 2
        },
        {
            "Nama_Produk" : "Cardigan",
            "harga" : "200000",
            "jumlah" : 1
        }
    ]
}

#print("Nama_pembeli :", keranjang["Nama_Pembeli"])
print(f"Daftar belanjaan {keranjang['Nama_Pembeli']}:\n")

# Gunakan for loop disini untuk mencetak semua produk di keranjang["Items"]
for barang in keranjang["Items"]:
    print(f"- produk: {barang['Nama_Produk']} | Harga : {barang['harga']} | Jumlah : {barang['jumlah']}")
    