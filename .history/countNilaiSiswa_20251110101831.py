import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
data.info()

# Tampilkan 5 ertama
data.head()

# Tampilkan statistik deskriptif dari dataset
data.describe()

# Hitung rata-rata, median, dan modus nilai mata pelajaran
print("Rata-rata:", data["Nilai"].mean())
print("Median:", data["Nilai"].median())
print("Modus:", data["Nilai"].mode()[0])

# Tampilkan nilai per mata pelajaran
matematika = data[data["Matpel"] == "Matematika"]
print(matematika)

english = data[data["Matpel"] == "Bahasa Inggris"]
print(english)

indonesia = data[data["Matpel"] == "Bahasa Indonesia"]
print(indonesia)

produktif = data[data["Matpel"] == "Produktif"]
print(produktif)

# Tampilkan nilai maksimum dan minimum per mata pelajaran
data.groupby("Matpel")["Nilai"].agg(["max","min"])

# Visualisasi Distribusi Nilai
rata = data.groupby("Matpel")["Nilai"].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Rata-Rata Nilai')
plt.show()