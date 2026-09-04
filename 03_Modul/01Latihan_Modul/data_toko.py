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
    barang_murah = belanjaan[0] #Sebelum mulai membandingkan satu per satu, komputer mengambil barang yang paling pertama (urutan ke-0 di dalam list) untuk dijadikan "pembanding awal" atau diasumsikan sementara sebagai barang yang paling murah.

    for barang in belanjaan: #Ini adalah perintah perulangan (loop) untuk memeriksa seluruh isi barang yang ada di dalam belanjaan satu persatu dari awal sampai akhir.
        if barang["harga"] < barang_murah["harga"]: #Apakah harga barang yang sedang diperiksa saat ini lebih kecil (<) daripada harga barang_murah yang disimpan sebelumnya?"
            barang_murah = barang #Jika ternyata ada barang yang harganya lebih murah dari simpanan sebelumnya, komputer akan memperbarui variabel barang_murah dengan data barang yang baru ini. Tapi kalau tidak lebih murah, baris ini dilewati.

    return barang_murah

def cari_sesuai_budget(belanjaan, budget):
    #buat list kosong untuk menampung barang-barang yang harganya cocok
    barang_pilihan = []

    for barang in belanjaan:
        #Jika harga barang kurang dari atau sama dengan budget
        if barang["harga"] <= budget:
            #masukkan barang tersebut ke dalam list barang_pilihan
            barang_pilihan.append(barang)

    #kembalikan list yang sudah berisi barang-barang hasil saringan
    return barang_pilihan

def cari_barang_berdasarkan_jumlah_beli(belanjaan):
    barang_beli = []

    for barang in belanjaan:
        if barang["jumlah"] > 2:
            barang_beli.append(barang)

    return barang_beli