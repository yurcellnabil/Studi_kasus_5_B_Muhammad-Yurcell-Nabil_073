daftar_kamar = {
    1: "Standard",
    2: "Deluxe",
}
# daftar kamar merupakan dari dictionary untuk penyimpanan dan pengelolaan data disitu saya memasukan jenis kamar
# yang tersedia yaitu Standard dan Deluxe

def hitung_biaya_pemesanan(jenis_kamar, lama_menginap):

# saya menggunakan variable def untuk membuat sebuah fungsi contoh hitung_biaya_pemesanan untuk menghitung biaya 
# dan yang di dalam kurung jenis_kamar untuk menyimpan kamar yang dipilih oleh pengguna dan lama_menginap untuk
#  menyimpan berapa hari menginap

    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000

# disini saya menggunakan if dan elif untuk menyimpan jenis kamar dan menyeleksi untuk menentukan harga
# kamar sesuai jenis kamar yang di pilih oleh pengguna jika tidak menggunakan if dan elif program tidak akan tau 
# harga kamar, untuk tarif untuk menyimpan harga kamar permalam, disini saya tidak menggunakan variable lower jadi pengguna harus mengisi sesuai data nya misalnya
# Standard maka S nya harus kapital

    total_biaya = tarif * lama_menginap
    return total_biaya

# variable total_biaya untuk menghitung total biaya dengan rumus tarif dikali (*) berapa lama menginapnya terus 
# saya menggunakan return mengembalikan atau mengirimkan hasil perhitungan biaya kamar lalu menyimpannya di dalam
# variable total_biaya 

jenis_kamar = input("Masukkan jenis kamar: ")

# memerintahkan input untuk menampilkan teks ke layar dan pengguna memilih jenis kamar lalu menyimpanannya ke 
# variable

check_in = int(input("Masukkan tanggal check-in: "))
check_out = int(input("Masukkan tanggal check-out: "))

# memerintah input untuk menampilkan teks ke layar dan pengguna memilih mau check in tanggal berapa lalu check out 
# tanggal berapa, dan saya juga menggunakan int untuk mengubah menjadi bilangan bulat agar bisa dihitung oleh
# program

lama_menginap = check_out - check_in

# untuk menghitung biaya dengan rumus check out dikurang check in misal sekarang tanggal 22-09-2026 dan check out 
# 25-09-2026 maka program akan menghitung lalu menampilkan teks 3 hari

total_biaya = hitung_biaya_pemesanan(jenis_kamar, lama_menginap)

# Memanggil fungsi hitung_biaya_pemesanan dengan mengirimkan nilai jenis_kamar dan lama_menginap.
# lalu hasil perhitungannya kemudian disimpan di variabel total_biaya.

print("Jenis Kamar:", jenis_kamar)
print("Tanggal Check-in:", check_in)
print("Tanggal Check-out:", check_out)
print("Lama Menginap:", lama_menginap, "hari")
print("Total Biaya:", total_biaya)

# print untuk mencetak atau memerintah untuk menampilkan hasil ke layar jenis_kamar untuk menampilkan jenis kamar,
# check_in untuk menampilkan tanggal check in, check_out untuk menampilkan tanggal check out, lama_menginap untuk 
# menampilkan lama menginap, total_biaya untuk menampilkan total biaya yang di bayar