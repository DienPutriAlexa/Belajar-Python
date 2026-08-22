# Membuat dictionary keranjang belanja
keranjang = {
    "Nama_Pembeli": "Dien",
    "Items": [
        # Produk ke-1 (indeks ke-0)
        {"nama_produk": "Polo Shirt", "harga": 150000, "jumlah": 2},
        
        # Produk ke-2 (indeks ke-1)
        {"nama_produk": "Cardigan", "harga": 200000, "jumlah": 1}
    ]
}

# 1. Menampilkan Nama Pembeli
print("Nama Pembeli:", keranjang["Nama_Pembeli"])

# 2. Menampilkan Nama Produk Pertama (mengambil dari list indeks ke-0)
print("Nama Produk 1:", keranjang["Items"][0]["nama_produk"])

# 3. Menghitung total harga produk pertama (harga * jumlah)
harga_p1 = keranjang["Items"][0]["harga"]
jumlah_p1 = keranjang["Items"][0]["jumlah"]
total_p1 = harga_p1 * jumlah_p1

print(f"Total harga {keranjang['Items'][0]['nama_produk']}: {total_p1}")