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

def hitung_total(belanjaan):
    total = 0
    for barang in belanjaan:
        # maksud dari += itu adalah sama aja kayak kalian memakai fungsi seperti ini
        # total = total + (barang["harga"] * barang["jumlah"])
        # Jadi, setiap kali perulangan for membaca satu barang, subtotal harga barang tersebut akan langsung ditambahkan (diakumulasikan) ke dalam variabel total yang ada di sebelah kiri.
        total += barang["harga"] * barang["jumlah"]
    return total

def cari_barang_termahal(belanjaan):
    barang_mahal = belanjaan[0]

    for barang in belanjaan:
        if barang["harga"] > barang_mahal["harga"]:
            barang_mahal = barang

    return barang_mahal

def cari_barang_termurah(belanjaan):
    barang_murah = belanjaan[0]

    for barang in belanjaan:
        if barang["harga"] < barang_murah["harga"]:
            barang_murah = barang

    return barang_murah