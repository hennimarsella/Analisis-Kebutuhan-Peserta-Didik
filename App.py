import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Dashboard Hasil Observasi Responden")

# Contoh data responden
data = {
    "Responden": ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10"],
    "Nilai": [3,4,2,3,4,3,3,4,2,3]
}

df = pd.DataFrame(data)

# Tampilkan tabel
st.subheader("Data Jawaban Responden")
st.dataframe(df)

# Membuat grafik
fig, ax = plt.subplots()

ax.plot(df["Responden"], df["Nilai"], marker="o")

ax.set_title("Grafik Jawaban Responden")
ax.set_xlabel("Responden")
ax.set_ylabel("Skala Jawaban")

# Rentang nilai 1–4
ax.set_ylim(1,4)

st.pyplot(fig)
