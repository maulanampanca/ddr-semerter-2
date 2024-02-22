product ={
    "Beras": 18000,
    "Gula": 12500,
    "Telur": 35000,
    "Susu": 19000,
}

def belanja():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per kg")

    total_belanja = 0
    while True:
         barang_dipilih = input("Masukan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower()=='selesai':
            Break
        if barang_dipilih not in product:
            print("maaf,barang tersebut tidak tersedia")
            Continue
        jumlah = float(input(f"Berapa kg{barang_dipilih}yang ingin dibeli?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total Belanja anda adalah: Rp  {total_belanja}")
