import streamlit as st
import pandas as pd
import os
from utils.data_utils import load_program_info

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 Nutrition Health Program",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main content
def main():
    # Header
    st.title("SPPI 2025 Nutrition Health Program")
    
    # Description
    st.markdown("""
    # Selamat Datang di Platform Informasi Program SPPI 2025 - Fokus Kesehatan Gizi
    
    Program **Sarjana Penggerak Pembangunan Indonesia (SPPI)** 2025 membuka peluang baru di bidang kesehatan gizi.
    Platform ini menyediakan informasi tentang program, kebutuhan gizi nasional, peluang penempatan,
    dan potensi kolaborasi dengan sektor swasta.
    
    ## Tentang Platform Ini
    
    Platform ini bertujuan untuk:
    - Memberikan informasi tentang formasi SPPI 2025 di bidang kesehatan gizi
    - Menampilkan data kesehatan gizi berdasarkan wilayah
    - Memetakan peluang penempatan SPPI
    - Memfasilitasi kolaborasi dengan sektor swasta
    - Menyediakan sumber daya tentang eligibilitas dan aplikasi
    
    Gunakan navigasi di sidebar untuk menjelajahi berbagai bagian platform ini.
    """)
    
    # Quick stats in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Perkiraan Formasi SPPI 2025", value="3,500+", delta="15% dari 2024")
    
    with col2:
        st.metric(label="Fokus Kesehatan Gizi", value="750+", delta="25% dari 2024")
    
    with col3:
        st.metric(label="Provinsi Target", value="34", delta="Seluruh Indonesia")
    
    # Features overview
    st.subheader("Fitur Platform")
    
    feature_col1, feature_col2 = st.columns(2)
    
    with feature_col1:
        st.info("**🔍 Informasi Program**\nDetail tentang program SPPI 2025, fokus kesehatan gizi, dan tujuan program.")
        st.info("**📊 Data Gizi Nasional**\nVisualisasi data gizi berdasarkan wilayah dan indikator kesehatan.")
        st.info("**🗺️ Peta Penempatan**\nPeta interaktif lokasi penempatan potensial SPPI 2025.")
    
    with feature_col2:
        st.info("**🤝 Kolaborasi Sektor Swasta**\nPeluang kerja sama untuk organisasi kesehatan sektor swasta.")
        st.info("**📝 Eligibilitas & Aplikasi**\nPanduan lengkap tentang persyaratan dan proses aplikasi.")
        st.info("**❓ FAQ**\nJawaban atas pertanyaan umum tentang program SPPI 2025.")
    
    # Call to action
    st.success("Mulai jelajahi platform ini dengan mengklik halaman di sidebar sebelah kiri")

# Sidebar
def sidebar():
    st.sidebar.title("Navigasi")
    st.sidebar.info(
        """
        Gunakan menu navigasi di atas untuk menjelajahi berbagai bagian platform.
        """
    )
    
    st.sidebar.title("Tentang")
    st.sidebar.info(
        """
        Platform ini menyediakan informasi tentang Program SPPI 2025 
        dengan fokus khusus pada kesehatan gizi dan peluang kolaborasi 
        dengan sektor swasta.
        """
    )
    
    st.sidebar.title("Kontak")
    st.sidebar.info(
        """
        Email: info@sppi.go.id  
        Website: https://sppi.kemdikbud.go.id
        """
    )

if __name__ == "__main__":
    sidebar()
    main()
