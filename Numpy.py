#########################################################################################
# IMPORT NUMPY
#########################################################################################

import numpy as np

list_1 = [1, 2, 3, 4]
list_2 = [2, 3, 4, 5]

# Bu iki listeyi normal metod ile çarpalım.
list_3 = []

for i in range(0, len(list_1)):
    list_3.append(list_1[i] * list_2[i])
list_3

# Numpy ile yapalım

list_4 = np.array([1, 2, 3, 4])
list_5 = np.array([2, 3, 4, 5])
list_4 * list_5

a = np.array([[1, 2, 3, 4, 5, 6],
              [9, 8, 7, 6, 5, 4]])

#########################################################################################
# CREATE NUMPY ARRAY
#########################################################################################


import numpy as np

np.array([1, 2, 3, 4])
type(np.array([1, 2, 3, 4]))

np.zeros(10, dtype=int)  # 0 dan oluşan, 10 tane int elemanı olan ndarray

np.ones(10, dtype=int)  # 1 dan oluşan, 10 tane int elemanı olan ndarray

np.random.randint(0, 10, size=10)  # 0-10 arasında 10 tane rastgele sayı üret.

np.random.normal(10, 4, (3, 4))  # ortalaması 10 standart sapması 4 olan 3x4 lük bir ndarray oluştur.

#########################################################################################
# NUMPY ARRAY FEATURES
#########################################################################################

a = np.random.randint(10, size=5)  # 0-10 arasında 5 tane rastgele sayı üret. default değeri 0 dır.

print(a.dtype)  # elemanların veri tipini ver
print(a.ndim)  # kaç boyutlu olduğunu ver
print(a.shape)  # hangi boyutta kaç tane elemanı var (hangi eksende kaç değişken (sütun/özellik) var)
print(a.size)  # toplamda kaç elemanı olduğunu ver

print("********************************")

# b = np.random.randint(10, size=(5, 6, 3))
b = np.random.randint(10, size=(3, 4, 5))
# 0-10 arasında 90 tane (x ekseninde 3 tane, y ekseninde 6 tane, z ekseninde 5 tane olacak şekilde) rastgele sayı üret.

print(b)
print(b.dtype)
print(b.ndim)
print(b.shape)
print(b.size)

c = np.random.randint(10, size=(2, 3, 4, 2))

#########################################################################################
# RESHAPE
#########################################################################################

import numpy as np

np.random.randint(1, 10, size=9)  # Tek boyutlu, 1-10 arasında rastgele 9 elemanı olan ndarray

np.random.randint(1, 10, size=9).reshape(3, 3)  # 3x3 lük bir matrise dönüştürelim.

np.random.randint(1, 10, size=27).reshape(3, 3, 3)  # 3x3x3 lük bir çok boyutlu bir matrise dönüştürelim.

print("*" * 111)

np.random.randint(1, 900, size=100)  # Tek boyutlu 1-900 arasında rastgele 100 tane elemanı olan bir ndarray oluştur.

np.random.randint(1, 900, size=100).reshape(10, 10)  # bunu 10x10 luk bir matrise dönüştür.

np.random.randint(1, 10, size=1000).reshape(10, 10,
                                            10)  # 1-10 arasında 1000 tane sayı üret ve bunu 10x10x10 luk bir matrise yerleştir.

#########################################################################################
# INDEX OPERATIONS
#########################################################################################

a = np.random.randint(10, size=10)

a[0]

a[0:3]

a[0] = 999

m = np.random.randint(10, size=(3, 5))  # 0-9 arasında rastgele 3x5 büyüklüğünde matris yap

m[2, 3]  # aynı exceldeki gibi index numarası 2 ve dizinin içinden index numarası 3 olan elemanı ver.

m[0, 2] = 111
m

k = np.random.randint(10, size=(3, 5, 4))  # hangisi hangi eksen. sıralma şöyle olacak: z, x, y
k
k[1, 1, 1]

m[
    0, 2] = 2.9  # numpy "fix type" yani sabit tiptir. bu yüzden 2 olarak yazar. üzerindeki tüm veriler için tek tip veri tipi tutar

m[0:2, 2:4]  # satırlardan 0,1 sütunlardan 2,3 ü al

#########################################################################################
# FANCY INDEX
#########################################################################################


v = np.arange(0, 30, 3)  # 0 dan 30 a kadar 3 lük artışla (muhtemelen ArrayRange in kısaltmasıdır
v

catch = [1, 2, 3]  # indeks numaraları 1,2,3 olan elemanları ver.

v[catch]

catch = [5, 2, 9]  # indeks numaraları 5,9 lan elemanları ver.

#########################################################################################
# CONDITIONAL COMPREHENSION
#########################################################################################


v = np.array([1, 2, 3, 4, 5])

# 4 ten küçük olan elemanların olduğu bir liste yap. bunu normal metodlarla yapalım.

new = []
for i in v:
    if i < 4:
        new.append(i)

# şimdi de bunu numpy ile yapalım.

v < 4  # v nin elemanlarının 4 küçük olanlarını True olmayanlarını False olarak işaretle ve bir dizi olarak döndür

v[v < 4]  # bu durumda da bir ndarray verir. True olanlarını yazacak False diğerlerini yazmayacak
type(v[v < 4])

#########################################################################################
# MATHEMATICAL OPERATIONS
#########################################################################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

v / 5  # Tüm elemanları 5 e böl ve yeni bir ndarray olarak ver

v ** 2

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)
np.std(v)

# iki bilinmeyenli denklem çözümğ

# (5 * a) + (1 * b) = 12
# (1 * a) + (3 * b) = 10

x = np.array([[5, 1], [1, 3]])  # birinci denklemin sol taraf katsayıları, ikinci denklemin sol taraf katsayıları
y = np.array([12, 10])  # birinci denklemin sonucu, ikinci denklemin sonucu

np.linalg.solve(x, y)  # linear algoritma.

print(np.__version__)  # numpy versiyonunu verir.



