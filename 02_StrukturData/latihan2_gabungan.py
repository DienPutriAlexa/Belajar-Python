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

# for barang in keranjang["Items"]:
#     if barang['harga'] >= 1000000:
#         kategori = "(Barang Mewah)"
#     else:
#         kategori = "(Barang Standar)"

#     print(f"- Produk: {barang['nama_produk']}  | Harga : {barang['harga']}  | Jumlah: {barang['jumlah']} |  {kategori}")

# Menggunakan enumerate(..., start=1) untuk nomor urut 1, 2, 3...
for nomor, barang in enumerate(keranjang["Items"], start=1):
    if barang['harga'] >= 1000000:
        kategori = "(Barang Mewah ✨)"
    else:
        kategori = "(Barang Standar 👍)"
        
    print(f"{nomor}. Produk: {barang['nama_produk']} | Harga: {barang['harga']} | {kategori}")    