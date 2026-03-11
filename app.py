import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =================================================
# KONFIGURASI HALAMAN
# =================================================
st.set_page_config(page_title="Dashboard Hasil Observasi", layout="wide")
st.title("📊 Dashboard Hasil Observasi Responden")

# =================================================
# LOAD DATA
# =================================================
df = pd.read_excel("DATA HASIL OBSERVASI.xlsx")

st.subheader("Data Responden")
st.dataframe(df)

# =================================================
# AMBIL DATA SOAL 1 - 20
# =================================================
soal = df.iloc[:,1:21]   # kolom Soal 1 sampai Soal 20

# =================================================
# HITUNG RATA-RATA SETIAP SOAL
# =================================================
rata_rata = soal.mean()

st.subheader("Rata-rata Jawaban Setiap Soal")
st.write(rata_rata)

# =================================================
# GRAFIK RATA-RATA
# =================================================
fig, ax = plt.subplots()

ax.bar(rata_rata.index, rata_rata.values)

ax.set_title("Grafik Rata-rata Jawaban Responden (Soal 1–20)")
ax.set_xlabel("Pertanyaan")
ax.set_ylabel("Nilai Rata-rata")

plt.xticks(rotation=45)

st.pyplot(fig)
