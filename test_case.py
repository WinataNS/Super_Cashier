#!/usr/bin/env python
# coding: utf-8

# In[3]:


import module_cashier as mc


# In[4]:


# Test Case 1: Menambahkan dua item baru
user = mc.Transaction()
print("Test Case 1")
print("\n")
user.add_item("Ayam Goreng", 2, 20_000)
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
print("Berikut adalah transaksi belanja Anda :")
user.check_order()
user.total_price()


# In[5]:


# Test Case 2: Menghapus salah satu item
user.delete_item("Pasta Gigi")
print("Berikut adalah transaksi belanja Anda :")
user.check_order()
user.total_price()


# In[6]:


# Test Case 3: Menghapus semua item
user.reset_transaction()


# In[8]:


# Test Case 4: Menghitung total belanja
user.add_item("Ayam Goreng", 2, 20_000)
user.add_item("Pasta Gigi", 3, 15_000)
user.add_item("Mainan Mobil", 1, 200_000)
user.add_item("Mie Instan", 5, 3_000)
print("\n")
print("Tabel Pemesanan :")
user.check_order()
user.total_price()


# In[9]:


# Test Case 5: Memperbaharui Item, Quantity, dan Harga
print("Tabel Pemesanan before Update:")
user.check_order()
user.total_price()
print("\n")
user.update_item_name("Pasta Gigi", "Sabun Mandi")
user.update_item_quantity("Ayam Goreng", 3)
user.update_item_price("Mie Instan", 3_500)
print("\n")
print("Tabel Pemesanan after Update:")
user.check_order()
user.total_price()


# In[10]:


# Test Case 6: Kesalahan Input
user.add_item("Gula", -25, 10_000)


# In[11]:


# Test Case 7: Kesalahan Input
user.add_item("Gula", "Lima", 10_000)


# In[ ]:




