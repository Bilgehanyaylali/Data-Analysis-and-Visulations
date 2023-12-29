#########################################################################################
# IMPORT PANDAS
#########################################################################################

import pandas as pd

a = pd.Series([10, 77, 12, 4, 5], [1, 2, 3, 4, 5])  # indeksin default değeri 0 dan başlar.
type(a)

a.index
a.dtype  # dtype : data type demektir. içindeki datanın tipi demektir.
a.ndim  # kaç boyutlu (pandas serileri tek boyutludur ve indeks numaraları vardır.)
a.size  # kaç tane veri var
a.values  # içindeki itemleri bir array olarak bize verir.
type(a.values)  # pandas series için valuelara ulaşmak istersek. bize bir ndarray verir.

a.head(2)  # içindeki ilk 2 elemanı ver.

a.tail(2)  # sondan 2 elemanı ver.

#########################################################################################
# READING DATA
#########################################################################################

df = pd.read_csv("004 2 Pandas/heightweight.csv")
df.head()

#########################################################################################
# DATA OVERVIEW
#########################################################################################


import seaborn as sns

df = sns.load_dataset("titanic")  # sns.load_dataset() seaborn kütüphanesine eklenen dataframelere ulaşabiliriz.
df.head()
df.tail()
df.shape()
df.info()
df.columns
df.index
df.describe()  # istatistiksel bilgileri verir
df.describe().T  # özet bilgilerinin transpozesini verir
df.isnull().values.any()  # toplamda herhangi bir boş değer varsa True döndür
df.isnull().values  # bir ndarray verir. boş olanları True, olmayaları False döndürür
df.isnull().sum()  # hangi satırda kaç tane boş varsa onu yazar

df["sex"].head()

df = sns.load_dataset("titanic")
df.head()

df.index  # indeksleri verir. yani kaç tane satır olduğunu

df[0:13]  # girilen aralıktaki indeksleri (satırları) listeler

df.drop(0, axis=0)  # axis=0 satırı ifade eder. satırdan 0. elamnı sil.

df.drop("sex", axis=1)  # axis=1 sütunu ifade eder. sütunlardan "sex" olanı sil

deleted_index = [1, 3, 5, 7, 9]

df.drop(deleted_index, axis=0).head()  # yukarıda tanımlı indeksleri sil

df.drop(deleted_index, axis=0, inplace=False).head()  # inplace=True olursa ana df de kalıcı yap.

df.index = df["age"]
df.head()

df.reset_index().head()  # indeksi yeniden oluşturu. 0 dan başlar.

pd.set_option("display.max_columns", None)  # tüm sütunları göster.

df = sns.load_dataset("titanic")

print(df.head())

"age" in df  # df için age diye bir sütun var mı

print(type(df["age"]))  # tek [] ile bir series tipi olur
print(type(df[["age"]]))  # çift [[]] ile bir dataframe tipi olur

# Sütun isimlerinde "age" kelimesi geçen sütunları listele.

print(df.loc[:, df.columns.str.contains("age")].head())

print(df.loc[:, ~df.columns.str.contains("age")].head())
# ~ (tilde) değili demek (tersi demek). Yani sütun isminde age kelimesi geçmeyenleri listele


#########################################################################################
# LOC & ILOC
#########################################################################################

pd.set_option("display.max_columns", None)  # tüm sütunları göster.

df = sns.load_dataset("titanic")

print(df.head())

df.iloc[0:3]

df.iloc[0:3, 0:2]  # excel deki gibi hücre konumları sayısal olarak verilir

df.loc[0:3, "age"]  # sanırım hem sayısal hem de string olarak verilirer. burada 0:3 demek 0,1,2,3 demektir.

df.loc[0:3, 0:2]

#########################################################################################
# CONDITIONAL EXPRESSIONS
#########################################################################################

df = sns.load_dataset("titanic")

df[df["age"] > 50].head()  # Yaşı 50 den büyük olanlar

df[df["age"] > 50].count()

df[df["age"] > 50]["age"].count()

df[df["age"] > 50]["deck"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
# birden çok koşul isterken () kullanmak gerekir

#########################################################################################
# AGGREGATION AND GROUPING
#########################################################################################

pd.set_option("display.max_columns", None)  # tüm sütunları göster.
# pd.set_option("Display.with", 500) # sanırım tüm değerleri alta geçmeden veriyor.

df = sns.load_dataset("titanic")

df.head()

df["age"].mean()  # yaş sütununun ortalamasını ver.

df.groupby("sex")["age"].mean()
# sex stünunu kendi içinde grupla ve o grupların age ortalamasını ver.

df.groupby("sex").agg({"age": "mean"})

df.groupby("sex").agg({"age": ["mean", "max", "sum", "min", "std"]})
# bu kullanımı alışkanlık haline getir.
# sex stünunu kendi içinde grupla ve o grupların age ortalamasını, max, sum ... ver.

df.groupby("sex").agg({"age": ["mean", "max", "sum", "min", "std"],
                       "survived": ["mean", "max"],
                       "embark_town": "count"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "max", "sum", "min", "std"],
                                                 "survived": ["mean", "max"],
                                                 "embark_town": "count"})

#########################################################################################
# PIVOT TABLE
#########################################################################################

pd.set_option("Display.width", 500)
# çıktının alt satıra geçmemesi için. 500 ekranın genişliğini ifade eder. pixel mi????

pd.set_option("display.max_columns", None)  # tüm sütunları göster.

df = sns.load_dataset("titanic")

df.head()

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

#########################################################################################
# CONCAT AND MERGE
#########################################################################################

m = np.random.randint(1, 30, size=(5, 5))
m

df_1 = pd.DataFrame(m, columns=["var1", "var2", "var3", "var4", "var5"])
df_1

df_2 = df_1 * 10
df_2

# concat ile birleştirme işlemleri

df_3 = pd.concat([df_1, df_2])
df_3

df_3 = pd.concat([df_1, df_2], ignore_index=True)
df_3
# birleştirmeyi alt alta yapar


df_4 = pd.concat([df_1, df_2], axis=1)
df_4

df_5 = pd.concat([df_1, df_2], ignore_index=True, axis=1)
df_5

df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})

df1

df2

pd.concat([df1, df2])

pd.merge(df1, df2)
# hangi sütuna göre birleştirme yapacağını vermediğimiz halde "employes" olarak kendisi seçti.

df3 = pd.merge(df1, df2, on="employees")
# on= ile  hangi sütun ile birleştirme yapacağını belirtiriz.


df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

# her çalışanın müdür bilgisine ulaşmak istersek
# birleştirme işlemleri daha çok sql tarafından yapılır.
pd.merge(df3, df4)

#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

#########################################################################################
# IMPORT PANDAS AND DATA READING
#########################################################################################

import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option('display.expand_frame_repr', False)  # tüm satıları aynı hizada göster
df = pd.read_csv("supermarket.csv")

df.info()

df.ndim  # kaç boyutlu olduğunu ver
df.shape  # hangi boyutta kaç tane elemanı var (hangi eksende kaç değişken (sütun/özellik) var)
df.size  # toplamda kaç elemanı olduğunu ver

#########################################################################################
# DATA OVERVIEW
#########################################################################################

df.head()
df.tail()
df.shape()
df.info()
df.columns

df.describe()  # istatistiksel bilgileri verir
df.describe().T  # özet bilgilerinin transpozesini verir
df.isnull().values.any()  # toplamda herhangi bir boş değer varsa True döndür
df.isnull().values  # bir ndarray verir. boş olanları True, olmayaları False döndürür
df.isnull().sum()  # hangi satırda kaç tane boş varsa onu yazar

df.index  # indeksleri verir. yani kaç tane satır olduğunu

df[0:13]  # girilen aralıktaki indeksleri (satırları) listeler

df.drop(0, axis=0)  # axis=0 satırı ifade eder. satırdan 0. elamnı sil.

df.drop("City", axis=1)  # axis=1 sütunu ifade eder. sütunlardan "sex" olanı sil

deleted_index = [1, 3, 5, 7, 9]

df.drop(deleted_index, axis=0).head()  # yukarıda tanımlı indeksleri sil

df.drop(deleted_index, axis=0, inplace=False).head()  # inplace=True olursa ana df de kalıcı yap.

df.head()
df.index = df["Invoice ID"]
df.head()

df.reset_index().head()  # indeksi yeniden oluşturu. 0 dan başlar.
df.head()

"City" in df  # df için city diye bir sütun var mı

print(type(df["City"]))  # tek [] ile bir series tipi olur
print(type(df[["City"]]))  # çift [[]] ile bir dataframe tipi olur

# Sütun isimlerinde "City" kelimesi geçen sütunları listele.

print(df.loc[:, df.columns.str.contains("City")].head())

print(df.loc[:, ~df.columns.str.contains("City")].head())
# ~ (tilde) değili demek (tersi demek). Yani sütun isminde City kelimesi geçmeyenleri listele


#########################################################################################
# LOC & ILOC
#########################################################################################


df.head()

df.iloc[0:3]

df.iloc[0:3, 0:2]  # excel deki gibi hücre konumları sayısal olarak verilir

df.loc[0:3, "City"]  # sanırım hem sayısal hem de string olarak verilirer. burada 0:3 demek 0,1,2,3 demektir.

df.loc[0:3, 0:2]

#########################################################################################
# CONDITIONAL EXPRESSIONS
#########################################################################################
df.head()

df[df["Unit price"] > 50].head()  # Unit price ı 50 den büyük olanlar

df[df["Unit price"] > 50].count()

df[df["Unit price"] > 50]["Unit price"].count()

df[df["Unit price"] > 50]["City"].count()

df.loc[df["Unit price"] > 50, ["Unit price", "City"]].head()

df.loc[(df["Unit price"] > 50) & (df["Branch"] == "A"), ["Unit price", "Payment"]].head()
# birden çok koşul isterken () kullanmak gerekir


#########################################################################################
# AGGREGATION AND GROUPING
#########################################################################################


df.head()

df["Unit price"].mean()  # Unit price ortalamasını ver.

df.groupby("City")["Unit price"].mean()
# City stünunu kendi içinde grupla ve o grupların Unit price ortalamasını ver.

df.groupby("Gender").agg({"Unit price": "mean"})

df.groupby("Gender").agg({"Unit price": ["mean", "max", "sum", "min", "std"]})
# bu kullanımı alışkanlık haline getir.
# Gender stünunu kendi içinde grupla ve o grupların Unit price ortalamasını, max, sum ... ver.

df.groupby("Gender").agg({"Unit price": ["mean", "max", "sum", "min", "std"],
                          "Total": ["mean", "max"],
                          "Product line": "count"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "max", "sum", "min", "std"],
                                                 "survived": ["mean", "max"],
                                                 "embark_town": "count"})

#########################################################################################
# PIVOT TABLE
#########################################################################################

df.head()

df.pivot_table("Rating", "Gender", "City")

df.pivot_table("Rating", "Gender", "City", aggfunc="std")

df.pivot_table("Rating", "Gender", ["City", "Customer type"])

#########################################################################################
# CONCAT AND MERGE
#########################################################################################

m = np.random.randint(1, 30, size=(5, 5))
m

df_1 = pd.DataFrame(m, columns=["var1", "var2", "var3", "var4", "var5"])
df_1

df_2 = df_1 * 10
df_2

# concat ile birleştirme işlemleri

df_3 = pd.concat([df_1, df_2])
df_3

df_3 = pd.concat([df_1, df_2], ignore_index=True)
df_3
# birleştirmeyi alt alta yapar


df_4 = pd.concat([df_1, df_2], axis=1)
df_4

df_5 = pd.concat([df_1, df_2], ignore_index=True, axis=1)
df_5

df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})

df2 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})

df1

df2

pd.concat([df1, df2])

pd.merge(df1, df2)
# hangi sütuna göre birleştirme yapacağını vermediğimiz halde "employes" olarak kendisi seçti.

df3 = pd.merge(df1, df2, on="employees")
# on= ile  hangi sütun ile birleştirme yapacağını belirtiriz.


df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

# her çalışanın müdür bilgisine ulaşmak istersek
# birleştirme işlemleri daha çok sql tarafından yapılır.
pd.merge(df3, df4)
