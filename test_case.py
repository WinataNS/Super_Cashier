#!/usr/bin/env python
# coding: utf-8

# In[6]:


import module_cashier as mc


# In[7]:


# Test Case
user = mc.Transaction()
user.add_item("Ayam Goreng", 2, 20_000)
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
user.check_order()


# In[8]:


# Test Case 2: Menghapus salah satu item
user.delete_item("Pasta Gigi")
print("\n")
user.check_order()


# In[9]:


# Test Case 3: Menghapus semua item
user.reset_transaction()


# In[10]:


# Test Case 4: Menghitung total belanja
user.add_item("Ayam Goreng", 2, 20_000)
user.add_item("Pasta Gigi", 3, 15_000)
user.add_item("Mainan Mobil", 1, 200_000)
user.add_item("Mie Instan", 5, 3_000)
print("\n")
print("Rincian Keranjang :")
user.check_order()
print("\n")
user.total_price()


# In[ ]:




