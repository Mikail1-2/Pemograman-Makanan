def main():
    # Fungsi utama program
    while True:
        print("\n----- Selamat datang di restoran -----")
        print("-----    Kentacky Wide Chicken    ------")
        print("\n1. Daftar menu")
        print("2. Kasir")
        print("3. Laporan penjualan")
        print("4. Exit")

        pilihan = input("\nPilih opsi (1-4): ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            kasir()
        elif pilihan == "3":
            laporan_penjualan()
        elif pilihan == "4":
            print("Terima kasih telah berkunjung!\n")
            break
        else:
            print("Opsi tidak valid, silakan pilih kembali.")

# Daftar menu
menu = {
    "1A": ("Ayam Dada", 12000),
    "1B": ("Ayam Paha Bawah", 10000),
    "1C": ("Ayam Sayap", 10000),
    "1D": ("Ayam Paha Atas", 12000),
    "2": ("Kentang", 5000),
    "3": ("Nasi", 3000),
    "4": ("Burger", 8000),
    "5": ("Cocacola", 5000),
    "6": ("Fanta", 5000),
    "7": ("Air Mineral", 3000),
    "8": ("Teh Manis", 4500),
    "9": ("Saus Sambal", 0),
    "10": ("Saus Matta", 2000),
    "11": ("Saus Keju", 2000)
}

penjualan = []
keranjang = []

def tampilkan_menu():
    print("\n------ DAFTAR MENU KWC -------")
    print("\n----- MAKANAN -----")
    for kode in ["1A", "1B", "1C", "1D", "2", "3", "4"]:
        nama, harga = menu[kode]
        print(f"{kode}. {nama:15} | {harga}")
    print("\n----- MINUMAN -----")
    for kode in ["5", "6", "7", "8"]:
        nama, harga = menu[kode]
        print(f"{kode}. {nama:15} | {harga}")
    print("\n----- SAUS -----")
    for kode in ["9", "10", "11"]:
        nama, harga = menu[kode]
        if harga == 0:
            harga_str = "Gratis Refil"
        else:
            harga_str = str(harga)
        print(f"{kode}. {nama:15} | {harga_str}")

def tampilkan_keranjang():
    print("\n----- Keranjang Pesanan -----")
    if keranjang:
        for item in keranjang:
            print(f"{item[1]}x {item[0]:15} = {item[2]}")
    else:
        print("Keranjang kosong.")

def kasir():
    total = 0
    pesanan = []

    while True:
        tampilkan_menu()
        tampilkan_keranjang()
        pilihan = input("\nMasukkan kode menu (atau '0' untuk selesai): ").upper()

        if pilihan == "0":
            break

        if pilihan in menu:
            nama, harga = menu[pilihan]
            jumlah = int(input(f"Berapa jumlah {nama}? "))
            total += harga * jumlah
            item = (nama, jumlah, harga * jumlah)
            pesanan.append(item)
            keranjang.append(item)
            print(f"{nama} ditambahkan ke pesanan. Total sementara: {total}")
        else:
            print("Kode menu tidak ditemukan, coba lagi.")

    print("\n----- Rincian Pesanan -----")
    print("\n{:<5} {:<15} {:<10} {:<10}".format("Qty", "Nama Item", "Harga", "Total"))
    print("-" * 40)
    for item in pesanan:
        print(f"{item[1]:<5} {item[0]:<15} {menu[[key for key in menu if menu[key][0] == item[0]][0]][1]:<10} {item[2]:<10}")
    print("-" * 40)
    print(f"{'Total Pembayaran':<30} {total}")
    penjualan.append(total)
    keranjang.clear()

def laporan_penjualan():
    print("\n----- Laporan Penjualan -----")
    if penjualan:
        print(f"Total transaksi: {len(penjualan)}")
        print(f"Total pendapatan: {sum(penjualan)}")
    else:
        print("Belum ada transaksi hari ini.")

if __name__ == "__main__":
    main()
