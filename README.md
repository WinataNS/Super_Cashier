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

# Function
- Class Transaction merupakan kelas yang berisi beberapa fungsi untuk sistem kasir self service dan menyimpan data input dari pelanggan.
<img width="688" alt="1" src="https://user-images.githubusercontent.com/130718918/232059657-a43bc613-37f7-493d-b3fd-dbed67bd13b7.png">

- Attribute, memiliki informasi tentang sistem Super_Cashier
<img width="688" alt="2" src="https://user-images.githubusercontent.com/130718918/232060297-13e2f029-567b-4905-a811-15befe113db3.png">

- Add_item merupakan fungsi yang digunakan untuk menambahkan sekaligus menyimpan data pemesanan dari pelanggan. Menyimpan tiga tipe data, antara lain:
  - item_name atau nama item menggunakan tipe data String (str)
  - item_qty atau jumlah item menggunakan tipe data Integer (int)
  - item_price atau harga item menggunakan tipe data Float (float) atau Integer (int)
- Add_item juga memiliki fungsi lain, yaitu memeriksa tipe data dan memberikan informasi apabila data yang diinput oleh pelanggan tidak sesuai dengan beberapa ketentuan (tipe data dan jumlah item yang tidak boleh kurang dari nol).
<img width="688" alt="3" src="https://user-images.githubusercontent.com/130718918/232062814-995cbcef-5c5d-431f-ba16-6e1dbc938332.png">

- Update_item_name merupakan fungsi yang digunakan untuk merubah atau memperbaharui item_name data item yang telah diinput oleh pelanggan dengan tipe data String (str). Update_item_name juga memiliki fungsi lain, yaitu untuk memeriksa tipe data dan memberikan informasi apabila data yang diinputkan ulang oleh pelanggan tidak sesuai.
<img width="688" alt="4" src="https://user-images.githubusercontent.com/130718918/232064866-30e849b9-a655-48dd-8af9-0f298ce5644f.png">

- Update_item_quantity merupakan fungsi yang digunakan untuk merubah atau memperbaharui item_qty data item yang telah diinput oleh pelanggan dengan tipe data Integer (int). Update_item_quantity juga memiliki fungsi lain, yaitu untuk memeriksa tipe data dan memberikan informasi apabila data yang diinputkan ulang oleh pelanggan tidak sesuai ketentuan (tipe data dan jumlah item yang tidak boleh kurang dari nol)
<img width="688" alt="5" src="https://user-images.githubusercontent.com/130718918/232065723-5f827a8f-1b04-437a-8594-977dce651f83.png">

- Update_item_price merupakan fungsi yang digunakan untuk merubah atau memperbaharui item_price data item yang telah diinput oleh pelanggan dengan tipe data Float (float) atau Integer (int). Update_item_price juga memiliki fungsi lain, yaitu untuk memeriksa tipe data dan memberikan informasi apabila data yang diinputkan ulang oleh pelanggan tidak sesuai.
<img width="688" alt="6" src="https://user-images.githubusercontent.com/130718918/232066288-a15b5ebf-54ec-493c-adfa-4e41f312da88.png">

- Delete_item merupakan fungsi yang digunakan untuk menghapus satu atau lebih item_name dari data item yang telah diinput oleh pelanggan dengan tipe data String (str). Delete_name juga memiliki fungsi lain, yaitu untuk memeriksa tipe data dan memberikan informasi apabila data yang ingin dihapus oleh pelanggan tidak sesuai. Selain itu, fungsi delete_item juga akan menampilkan informasi apabila item_name berhasil dihapus dengan tampilan tabel.
<img width="688" alt="7" src="https://user-images.githubusercontent.com/130718918/232067242-f75c9465-fa0c-400a-a8eb-3826e04a1bc5.png">

- Reset_transaction merupakan fungsi yang digunakan untuk menghapus seluruh item_name dari data item yang telah diinput oleh pelanggan. Fungsi reset_transaction juga akan menampilkan informasi apabila data item telah berhasil dihapus dengan tampilan tabel.
<img width="688" alt="8" src="https://user-images.githubusercontent.com/130718918/232068143-e8685f9c-6452-4f0d-a72e-9a20dcb687d2.png">

- Check_order merupakan fungsi yang digunakan untuk memeriksa kembali total harga tiap item. Fungsi check_order akan menambahkan kolom baru dengan nama Total_Price, lalu melakukan perhitungan item_qty * item_price untuk tiap item_name, lalu menampilkannya dengan tampilan tabel.
<img width="688" alt="9" src="https://user-images.githubusercontent.com/130718918/232071066-1dba9c2c-29bc-43c9-b56d-032e1531851f.png">


- Total_price merupakan fungsi yang digunakan untuk menghitung keseluruhan total harga yang harus dibayarkan oleh pelanggan. Fungsi total_price akan menghitung total harga, lalu memeriksa apakah hasil perhitungan telah memenuhi beberapa ketentuan, dengan tujuan untuk memberikan potongan harga atau diskon. Ketentuan-ketentuan tersebut antara lain:
  - Apabila total harga pembelian pelanggan lebih besar dari sama dengan Rp. 200.000, maka akan mendapat diskon 5%
  - Apabila total harga pembelian pelanggan lebih besar dari sama dengan Rp. 300.000, maka akan mendapat diskon 8%
  - Apabila total harga pembelian pelanggan lebih besar dari sama dengan Rp. 500.000, maka akan mendapat diskon 10%
- Total_price akan menghitung total harga yang harus dibayarkan oleh pelanggan apabila ketentuan telah tercapai.
<img width="688" alt="10" src="https://user-images.githubusercontent.com/130718918/232070670-963352aa-3457-44ca-b69f-ff52e4227720.png">

# Test Case
- Test Case 1
<img width="688" alt="11" src="https://user-images.githubusercontent.com/130718918/232072228-01d89dee-6afe-4b67-80fe-3521e6824ad7.png">

- Test Case 2
<img width="688" alt="12" src="https://user-images.githubusercontent.com/130718918/232072277-50ee862d-f167-4305-a77b-e3f9de7f1256.png">

- Test Case 3
<img width="688" alt="13" src="https://user-images.githubusercontent.com/130718918/232072321-cbd85ac5-3074-4add-b84e-2dea3a150de6.png">

- Test Case 4
<img width="688" alt="14" src="https://user-images.githubusercontent.com/130718918/232072379-995dba48-c6cf-4c61-88e0-fc1fe00b990f.png">
