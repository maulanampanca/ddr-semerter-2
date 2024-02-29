product = {
    "caffe americao": 18000,
    "caramel macchiato": 59000,
    "asian dolce latte": 55000,
    "caramel latte": 52000,
    "vanilla late": 52000,
    "caffe late": 48000,
    "cappucino": 48000,
    "caffe mocha":55000,

}

def belanja():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per gelas") 
        
    total_belanja = 0
    while True:
        barang_dipilih = input("Masukkan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if barang_dipilih.lower() == 'selesai':
             break
        if barang_dipilih not in product:
            print("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa gelas {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    if total_belanja > 350000:
        diskon = total_belanja * 0.15 
        total_belanja -= barang_dipilih * ppn


    ppn = 0.10
    total_belanja += total_belanja * ppn

    print(f"total Belanja anda adalah: Rp{total_belanja}")

belanja()       
            