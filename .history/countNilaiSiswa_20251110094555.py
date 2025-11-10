import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
data.info()
data.head()
data.describe()
print("Rata-rata:", data.get['nilai'].mean())
print("Median:", data[]].median())
print("Modus:", data["nilai"].mode()[0])

matematika = data[data["Matpel"] == "Matematika"]
print(matematika)

english = data[data["Matpel"] == "Bahasa Inggris"]
print(english)

indonesia = data[data["Matpel"] == "Bahasa Indonesia"]
print(indonesia)

produktif = data[data["Matpel"] == "Produktif"]
print(produktif)

data.groupby("Mapel")["nilai"].agg(["max","min"])
