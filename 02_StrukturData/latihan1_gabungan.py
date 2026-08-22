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
        }
    ]
        
    
}

total_belanja_pertama = keranjang["Items"][0]["harga"] * keranjang["Items"][0]["jumlah"]
total_belanja_kedua = keranjang["Items"][1]["harga"] * keranjang["Items"][1]["jumlah"]
total_belanja_ketiga = keranjang["Items"][2]["harga"] * keranjang["Items"][2]["jumlah"]

total_belanja = total_belanja_pertama + total_belanja_kedua +total_belanja_ketiga


for barang in keranjang["Items"]:
    print(f"- produk: {barang['nama_produk']} | Harga : {barang['harga']} | Jumlah : {barang['jumlah']}")

print(f"Nama Pembeli:{keranjang['Nama_Pembeli']}")
print(f"Total belanja keseluruhan :{total_belanja}")