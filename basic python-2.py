#!/usr/bin/env python
# coding: utf-8

# In[2]:


#OPERASI STRING


# In[3]:


#MENGUBAH HURUF BESAR/KECIL


# In[4]:


#Upper
nama = "bayu"
nama_cap = nama.upper()
print(nama_cap)


# In[5]:


#Lower
nama = "ANNELIES"
nama_lower = nama.lower()
print(nama_lower)


# In[6]:


print(nama.lower())


# In[7]:


#AWALAN DAN AKHIRAN


# In[8]:


#rstrip
rstrip = "Indonesia           "
print(rstrip.rstrip())


# In[9]:


#lstrip
lstrip = "       Indonesia"
print(lstrip.lstrip())


# In[10]:


#strip
strip = "    Indonesia    "
strip_dua = "Merdeka!"
print(strip.strip() + strip_dua)


# In[12]:


#strip => menghilangkan bagian tertentu di kalimat
word = "dokidokiliteratureclub"
print(word.strip('club'))


# In[13]:


#MENGGABUNGKAN DAN MEMISAHKAN STRING


# In[14]:


#Join
print(','.join(['Indonesia', '.', 'AI']))


# In[15]:


#Split
var = "Indonesia tanah airku"
var_dua = var.split("Indonesia")


# In[16]:


print(var_dua)


# In[17]:


#MENGGANTI ELEMEN DI STRING


# In[18]:


nama = "Indonesia Negaraku"
print(nama)
print(nama.replace('Negaraku', 'Tanah Airku'))


# In[19]:


lower = "Aku cinta indonesia"
print(lower.isalpha())


# In[20]:


#LAIN-LAIN


# In[21]:


nama = "muhammad iqbal"
print(nama.capitalize())


# In[22]:


print(nama.title())


# In[23]:


#KONVERSI TIPE DATA


# In[24]:


#String
angka = 1
print(type(angka))


# In[25]:


angka_dua = str(angka)
print(type(angka_dua))
print(angka_dua)


# In[26]:


#Integer
float = 1.5
print(type(float))


# In[27]:


float_dua = int(float)
print(float_dua)


# In[28]:


print(type(float_dua))


# In[29]:


#CARA LAIN UNTUK PRINT


# In[30]:


print('Halo {}'.format('Semuanya'))


# In[31]:


var = "Indonesia"
print('Aku cinta %s' % var)


# In[32]:


var_dua = 1234
print('Berhitung mulai dari %d' % var_dua)


# In[33]:


#INPUT DATA


# In[34]:


nama_satu = input('Siapa Nama Kamu?')
print(type(nama_satu))


# In[ ]:


tambah = input("Masukkan Angka: ")
tambah_dua = 200
tambah_tiga = int(tambah) + 200
print(tambah_tiga)


# In[ ]:


#IF, ELSE, ELIF


# In[ ]:


Type Markdown and LaTeX:  𝛼2


# In[ ]:


#if
y = 40
z = 200
w = y < z
print(w)
if w == True:
    print("ternyata 40 lebih kecil dari 100")


# In[ ]:


#else
var_x = 0
if var_x > 1:
    print("5 besar dari 1")
else:
    print("Enggak benar, nih!")


# In[ ]:


masukkan = int(input("Masukkan angka: "))
var_y = 10
if masukkan < var_y:
    print(masukkan, 'lebih kecil dari', var_y)
else:
    print(masukkan, 'Lebih besar', var_y)


# In[ ]:


#elif
your_name = input("Masukkan Nama Anda!")
time = int(input("Pukul berapa Anda datang?"))
masuk = 8
limit = 10
print("Halo", your_name)
if time == 8:
    print("Wah! Anda datang tepat waktu, %s!" % your_name)
elif time < 8:
    print("Wah, Anda sangat rajin, %s!" % your_name)
elif time > 8 & time < limit:
    print("Kenapa Anda terlambat, %s?" % your_name)
else:
    print("Anda dipotong gaji!")


# In[ ]:


#LOOP


# In[ ]:


foods = ['Kebab', 'Burger', 'Kofta']
for elemen in foods:
    print("Saya ingin makan %s" % elemen)


# In[ ]:


angka_ = [1, 2, 3, 4, 5, 6, 7]
for nomor in angka_:
    print(nomor)


# In[ ]:


#WHILE


# In[ ]:


t = 1
while t <= 10:
    print(t)
    t += 1


# In[ ]:


input_angka = int(input("Masukkan Angka "))
angka_z = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
for a in angka_z:
    print(a)
    if a == input_angka:
        print("Angka %d ditemukan" % input_angka)
        break


# In[ ]:




