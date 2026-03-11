import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul
st.title("Dashboard Hasil Observasi Responden")

# Membaca data Excel
df = pd.read_excel("DATA HASIL OBSERVASI.xlsx")

# Tampilkan data
st.subheader("Data Jawaban Responden")
st.dataframe(df)

# Membuat grafik
fig, ax = plt.subplots()

# Plot setiap responden
for i in range(len(df)):
    ax.plot(range(1,21), df.iloc[i,1:21], marker='o', label=f'Responden {i+1}')

# Pengaturan grafik
ax.set_xlabel("Nomor Soal (1-20)")
ax.set_ylabel("Skala Jawaban")
ax.set_title("Grafik Jawaban Responden")

# Rentang nilai 1–4
ax.set_ylim(1,4)

ax.set_xticks(range(1,21))
ax.legend()

st.pyplot(fig)
