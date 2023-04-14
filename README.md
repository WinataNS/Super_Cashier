# Latar Belakang
Menciptakan sebuah sistem kasir self service untuk membantu pelanggan dalam berbelanja. Sistem kasir yang dilengkapi dengan fitur menyimpan data barang yang akan dibeli (nama, jumlah, dan harga per satuan), serta dapat melakukan kalkukasi total harga yang harus dibayar oleh pelanggan beserta diskonnya.

# Requirement / Objektif
- Fitur menciptakan ID Transaction
- Fitur menambahkan Nama, Jumlah, dan Harga Item dengan fungsi add_item
- Fitur merubah detail Item (Change or Delete)
  - Change, menggunakan fungsi update_name, update_qty, update_price
  - Delete, menggunakan fungsi delete_item
- Fitur Reset Transaction dengan fungsi reset_transaction
- Fitur menghitung total harga transaksi dengan fungsi check_order
- Fitur menghitung total harga yang harus dibayar setelah diskon menggunakan fungsi total_price, sesuai ketentuan
  - Total Harga lebih besar dari sama dengan Rp 200.000 mendapatkan diskon 5%
  - Total Harga lebih besar dari sama dengan Rp 300.000 mendapatkan diskon 8%
  - Total Harga lebih besar dari sama dengan Rp 500.000 mendapatkan diskon 10%

# Flowchart
![Flowchart](https://user-images.githubusercontent.com/130718918/231976256-18439d22-22c5-456f-9b64-309c8a9532ba.png)



