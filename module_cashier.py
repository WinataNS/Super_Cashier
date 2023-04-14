#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pds
import numpy as npy
from tabulate import tabulate

class Transaction:
    # Membuat dictionary untuk transaksi
    dictionary = {"Item": [], "Qty": [], "Price": []}
    data = pds.DataFrame(dictionary)
    
    def _init_(self):
        """Fungsi untuk Inisialisasi class Transaction"""
        self.store_name = "Super_Cashier"
        
    def add_item(self, item_name: str, item_qty: int, item_price: float or int):
        """Fungsi untuk menambahkan item ke dalam dictionary"""
        
        # Fungsi untuk memeriksa data type item_name (str)
        if type(item_name) != str:
            print("Tipe data untuk item_name harus String")
        
        # Fungsi untuk memeriksa data type item_qty (int) dan >= 0
        elif type(item_qty) != int or item_qty < 0:
            print("Tipe data untuk item_qty harus Integer dan lebih besar dari 0")
             
        # Fungsi untuk memeriksa data type item_price (float & int)
        elif type(item_price) != float and type(item_price) != int:
            print("Tipe data untuk item_price harus Float atau Integer")
            
        else:
            self.data.loc[len(self.data)] = [item_name, item_qty, item_price,]
            print("Item berhasil ditambahkan ke dalam keranjang")
            print(f"Item Name     : {item_name}")
            print(f"Quantity      : {item_qty}")
            print(f"Price         : Rp. {item_price}")
            
    def update_item_name(self, item_name: str, update_name: str):
        """Fungsi untuk merubah atau memperbaharui item_name ke dalam dictionary"""
        
        # List item_name
        list_item_name = self.data["Item"].tolist()

        # Fungsi untuk memeriksa apakah item terdapat di dalam keranjang
        if item_name not in list_item_name:
            print("Nama item tidak ditemukan di dalam keranjang")
            
        # Fungsi untuk memeriksa data type item_name (str)
        elif type(item_name) != str:
            print("Tipe data untuk item_name harus String")
            
        # Fungsi untuk memeriksa data type item_name (str)
        elif type(update_name) != str:
            print("Tipe data untuk update_name harus String")
            
        else:
            self.data.loc[self.data.Item == item_name, "Item"] = update_name
            print(f"Berhasil memperbaharui item {item_name} menjadi {update_name}")
            
    def update_item_quantity(self, item_name: str, update_qty: int):
        """Fungsi untuk merubah atau memperbaharui item_qty ke dalam dictionary"""
        
        # List item_name
        list_item_name = self.data["Item"].tolist()
        
        # Fungsi untuk memeriksa apakah item terdapat di dalam keranjang
        if item_name not in list_item_name:
            print("Nama item tidak ditemukan di dalam keranjang")
            
        # Fungsi untuk memeriksa data type item_name (str)
        elif type(item_name) != str:
            print("Tipe data untuk item_name harus String")
            
        # Fungsi untuk memeriksa data type update_qty (int)
        elif type(update_qty) != int:
            print("Tipe data untuk update_qty harus Integer")
            
        else:
            self.data.loc[self.data.Item == item_name, "Qty"] = update_qty
            print(f"Berhasil memperbaharui jumlah item {item_name} menjadi {update_qty}")
            
    def update_item_price(self, item_name: str, update_price: float or int):
        """Fungsi untuk merubah atau memperbaharui item_price ke dalam dictionary"""
        
        # List item_name
        list_item_name = self.data["Item"].tolist()
        
        # Fungsi untuk memeriksa apakah item terdapat di dalam keranjang
        if item_name not in list_item_name:
            print("Nama item tidak ditemukan di dalam keranjang")
            
        # Fungsi untuk memeriksa data type item_name (str)
        elif type(item_name) != str:
            print("Tipe data untuk item_name harus String")
            
        # Fungsi untuk memeriksa data type update_price (float & int)
        elif type(update_price) != float and type(update_price) != int:
            print("Tipe data untuk update_price harus Float dan Integer")

        else:
            self.data.loc[self.data.Item == item_name, "Price"] = update_price
            print(f"Berhasil memperbaharui harga item {item_name} menjadi {update_price}")

    def delete_item(self, item_name: str):
        """Fungsi untuk menghapus satu atau beberapa item dari dalam dictionary"""
        
        # List item_name
        list_item_name = self.data["Item"].tolist()
     
        # Fungsi untuk memeriksa apakah item terdapat di dalam keranjang
        if item_name not in list_item_name:
            print("Nama item tidak ditemukan di dalam keranjang")
            
        # Fungsi untuk memeriksa data type item_name (str)
        elif type(item_name) != str:
            print("Tipe data untuk item_name harus String")
            
        else:
        # Menampilkan keterangan item yang telah dihapus
            print(f"Berhasil menghapus item {item_name} dari dalam keranjang")

            data = self.data.drop(self.data.index[self.data.Item == item_name],inplace=True,)

        # Menampilkan keranjang dalam bentuk tabel
            table = tabulate(data, headers="keys", tablefmt="firstrow")
        
        return print(table)
    
    def reset_transaction(self):
        """Fungsi untuk menghapus semua item dari dalam dictionary"""

        # Menampilkan keterangan
        print("Keranjang telah dikosongkan")

        self.data.drop(self.data.index, inplace=True)

        # Menampilkan keranjang dalam bentuk tabel
        table = tabulate(self.data, headers="keys", tablefmt="firstrow")

        return print(table)
    
    def check_order(self):
        """Fungsi untuk mengecek kembali item yang ada di dalam dictionary"""

        # Memanggil data item dalam dictionary
        output_data = self.data.copy()

        # Menambahkan kolom baru untuk menghitung Total_Price
        output_data["Total_Price"] = (output_data.Qty * output_data.Price)
        
        # Menampilkan hasil dalam bentuk tabel
        table = tabulate(output_data, headers = "keys", tablefmt = "firstrow")

        return print(table)
    
    def total_price(self):
        """Fungsi untuk menghitung total harga dan diskon dari item"""
        
        # Memanggil data item dalam dictionary
        output_data = self.data.copy()

        # Menambahkan kolom baru untuk menghitung Total_Price
        output_data["Total_Price"] = (output_data.Qty * output_data.Price)
        
        # Menambahkan variabel total harga
        total = npy.sum(output_data.Total_Price)

        # Diskon 0 persen, jika Total_Price <= 200 ribu
        if total >= 0 and total <= 200_000:
            return print(f"Total pembayaran sebesar Rp.{int(total)}")

        # Diskon 5 persen, jika Total_Price > 200 ribu & <= 300 ribu
        elif total > 200_000 and total <= 300_000:
            total_belanja = total * 0.95
            return print(f"Total harga item sebesar Rp.{int(total)} \nDiskon sebesar 5% \nTotal pembayaran sebesar Rp.{int(total_belanja)}")

        # Diskon 8 persen, jika Total_Price > 300 ribu & <= 500 ribu
        elif total > 300_000 and total <= 500_000:
            total_belanja = total * 0.92
            return print(f"Total harga item sebesar Rp.{int(total)} \nDiskon sebesar 8% \nTotal pembayaran sebesar Rp.{int(total_belanja)}")

        # Diskon 10 persen, jika Total_Price > 500 ribu
        elif total > 500_000:
            total_belanja = total * 0.90
            return print(f"Total harga item sebesar Rp.{int(total)} \nDiskon sebesar 10% \nTotal pembayaran sebesar Rp.{int(total_belanja)}")

        else:
            return "Total harga tidak boleh kurang dari nol"

