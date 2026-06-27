import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Dashboard Analisis Properti",
    page_icon="🏠",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("dataset_2.csv")

# =========================
# HEADER
# =========================
st.title("🏠 Dashboard Analisis Data Real Estate")
st.subheader("Project Data Visualization")
st.markdown("**Created by : Aflahul Azkiyak**")

st.divider()

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.title("Filter Dashboard")

selected_location = st.sidebar.multiselect(
    "Pilih Lokasi",
    options=df["Location"].unique(),
    default=df["Location"].unique()
)

selected_property = st.sidebar.multiselect(
    "Pilih Jenis Properti",
    options=df["Property_Type"].unique(),
    default=df["Property_Type"].unique()
)

# Filter data
filtered_df = df[
    (df["Location"].isin(selected_location)) &
    (df["Property_Type"].isin(selected_property))
]

# =========================
# KPI SECTION
# =========================
st.subheader("📌 Ringkasan Data")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Jumlah Data Properti",
        value=len(filtered_df)
    )

with col2:
    avg_price = filtered_df["Price"].mean()
    st.metric(
        label="Rata-rata Harga",
        value=f"${avg_price:,.0f}"
    )

with col3:
    max_price = filtered_df["Price"].max()
    st.metric(
        label="Harga Tertinggi",
        value=f"${max_price:,.0f}"
    )

st.divider()

# =========================
# TABEL DATA
# =========================
st.subheader("📋 Dataset Properti")

st.dataframe(filtered_df, use_container_width=True)

st.divider()

# =========================
# CHART 1
# =========================
st.subheader("📊 Rata-rata Harga Berdasarkan Jenis Properti")

avg_property = filtered_df.groupby("Property_Type")["Price"].mean()

fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.bar(avg_property.index, avg_property.values)
ax1.set_xlabel("Jenis Properti")
ax1.set_ylabel("Average Price")
plt.xticks(rotation=30)

st.pyplot(fig1)

# =========================
# CHART 2
# =========================
st.subheader("🛏 Distribusi Jumlah Kamar")

fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.hist(filtered_df["Rooms"], bins=8)
ax2.set_xlabel("Jumlah Kamar")
ax2.set_ylabel("Frekuensi")

st.pyplot(fig2)

# =========================
# CHART 3
# =========================
st.subheader("🏊 Persentase Properti Dengan Pool")

pool_data = filtered_df["Has_Pool"].value_counts()

fig3, ax3 = plt.subplots(figsize=(6, 6))
ax3.pie(
    pool_data,
    labels=pool_data.index,
    autopct="%1.1f%%"
)

st.pyplot(fig3)

st.divider()

# =========================
# STATISTIK DESKRIPTIF
# =========================
st.subheader("📈 Statistik Dataset")

st.write(filtered_df.describe())

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<center>Developed by <b>Aflahul Azkiyak</b> | Streamlit Dashboard Project 2026</center>",
    unsafe_allow_html=True
)
