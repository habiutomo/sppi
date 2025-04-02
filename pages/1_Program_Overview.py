import streamlit as st
from utils.data_utils import load_program_info

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Program Overview",
    page_icon="🍏",
    layout="wide"
)

def main():
    # Header
    st.title("Program Overview")
    
    # Load program information
    program_info = load_program_info()
    
    # Program description section
    st.header("Tentang Program SPPI 2025")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        ## {program_info['program_name']} ({program_info['year']})
        
        {program_info['description']}
        
        **Fokus Area:** {program_info['focus_area']}
        
        **Periode Aplikasi:** {program_info['application_period']}
        
        **Durasi Program:** {program_info['program_duration']}
        """)
        
        st.subheader("Tujuan Program")
        for objective in program_info['objectives']:
            st.markdown(f"- {objective}")
    
    with col2:
        # Program stats
        st.markdown("### Statistik Program")
        st.metric("Perkiraan Total Formasi", program_info['estimated_positions'])
        st.metric("Fokus Kesehatan Gizi", program_info['nutrition_focus_positions'])
        st.metric("Persentase Formasi Gizi", f"{(program_info['nutrition_focus_positions'] / program_info['estimated_positions'] * 100):.1f}%")
        
        # Show program logo
        st.image("assets/sppi_logo.svg", width=200)
    
    # Program timeline
    st.header("Timeline Program")
    
    timeline_col1, timeline_col2, timeline_col3, timeline_col4, timeline_col5 = st.columns(5)
    
    with timeline_col1:
        st.markdown("#### Pendaftaran")
        st.markdown("Januari - Maret 2025")
        st.markdown("Pembukaan portal aplikasi dan penerimaan dokumen")
    
    with timeline_col2:
        st.markdown("#### Seleksi")
        st.markdown("April - Mei 2025")
        st.markdown("Tes tertulis, wawancara, dan penilaian")
    
    with timeline_col3:
        st.markdown("#### Pengumuman")
        st.markdown("Juni 2025")
        st.markdown("Pengumuman peserta yang lolos seleksi")
    
    with timeline_col4:
        st.markdown("#### Pelatihan")
        st.markdown("Juli 2025")
        st.markdown("Pembekalan dan orientasi program")
    
    with timeline_col5:
        st.markdown("#### Penempatan")
        st.markdown("Agustus 2025")
        st.markdown("Peserta mulai bertugas di lokasi penempatan")
    
    # Program focus
    st.header("Fokus Kesehatan Gizi")
    
    st.markdown("""
    Program SPPI 2025 memberikan penekanan khusus pada kesehatan gizi untuk mengatasi tantangan kesehatan masyarakat di Indonesia.
    Formasi di bidang kesehatan gizi akan ditugaskan untuk:
    
    1. **Pemantauan Status Gizi**: Melakukan pengumpulan dan analisis data status gizi masyarakat di daerah penempatan.
    
    2. **Edukasi Gizi**: Memberikan penyuluhan dan edukasi tentang pola makan sehat dan gizi seimbang kepada masyarakat.
    
    3. **Program Intervensi**: Merancang dan melaksanakan program intervensi gizi berbasis masyarakat.
    
    4. **Koordinasi Lintas Sektor**: Bekerja sama dengan dinas kesehatan setempat, sekolah, dan organisasi masyarakat.
    
    5. **Pemantauan Pertumbuhan**: Membantu dalam pemantauan pertumbuhan bayi dan balita untuk pencegahan stunting.
    
    6. **Keamanan Pangan**: Mengadvokasi praktik keamanan pangan dan sanitasi di tingkat rumah tangga dan komunitas.
    """)
    
    # Target areas
    st.header("Area Target")
    
    st.markdown("""
    Program SPPI 2025 akan menempatkan peserta di seluruh wilayah Indonesia dengan prioritas pada:
    
    - **Daerah 3T** (Terdepan, Terluar, Tertinggal)
    - **Daerah dengan prevalensi stunting tinggi**
    - **Daerah dengan keterbatasan tenaga kesehatan gizi**
    - **Daerah rawan pangan**
    
    Penempatan akan disesuaikan dengan kebutuhan daerah dan kompetensi peserta.
    """)
    
    # Additional resources
    st.header("Sumber Informasi Tambahan")
    
    resources_col1, resources_col2 = st.columns(2)
    
    with resources_col1:
        st.markdown("""
        ### Situs Web Resmi
        - [Portal SPPI Kemdikbud](https://sppi.kemdikbud.go.id)
        - [Kementerian Kesehatan](https://www.kemkes.go.id)
        
        ### Dokumen Terkait
        - Panduan Program SPPI 2025
        - Peta Jalan Perbaikan Gizi Indonesia 2020-2024
        - Rencana Pembangunan Jangka Menengah Nasional (RPJMN) 2020-2024
        """)
    
    with resources_col2:
        st.markdown("""
        ### Kontak
        - Email: info@sppi.kemdikbud.go.id
        - Telepon: (021) 5790-3333
        
        ### Media Sosial
        - Twitter: @SPPI_official
        - Instagram: @sppi_kemdikbud
        - Facebook: SPPI Kemdikbud
        """)
    
    # FAQ Section
    st.header("Pertanyaan yang Sering Diajukan (FAQ)")
    
    with st.expander("Apa itu Program SPPI?"):
        st.markdown("""
        Program Sarjana Penggerak Pembangunan Indonesia (SPPI) adalah program penempatan
        sarjana di berbagai daerah di Indonesia untuk mendukung pembangunan nasional.
        Program ini memberikan kesempatan bagi lulusan sarjana untuk berkontribusi dalam
        pembangunan daerah sambil mengembangkan kompetensi profesional mereka.
        """)
    
    with st.expander("Apa fokus khusus SPPI 2025?"):
        st.markdown("""
        SPPI 2025 akan memberikan penekanan khusus pada kesehatan gizi, dengan tujuan
        untuk mendukung upaya nasional dalam perbaikan status gizi masyarakat Indonesia,
        terutama untuk mengurangi stunting dan masalah gizi lainnya.
        """)
    
    with st.expander("Siapa yang dapat mendaftar?"):
        st.markdown("""
        Program SPPI terbuka bagi lulusan S1/D4 dari perguruan tinggi terakreditasi dengan
        latar belakang pendidikan yang sesuai dengan formasi yang dibuka, terutama 
        bidang kesehatan, gizi, atau ilmu terkait untuk formasi kesehatan gizi.
        """)
    
    with st.expander("Apa manfaat mengikuti program SPPI?"):
        st.markdown("""
        Manfaat mengikuti program SPPI antara lain:
        - Pengalaman kerja yang berharga di bidang pembangunan
        - Pengembangan kompetensi profesional
        - Tunjangan bulanan dan fasilitas selama program
        - Jaringan profesional yang luas
        - Kesempatan untuk berkontribusi pada pembangunan nasional
        - Peluang karir yang lebih baik setelah program
        """)
    
    with st.expander("Bagaimana proses seleksi SPPI?"):
        st.markdown("""
        Proses seleksi SPPI meliputi:
        1. Seleksi administrasi
        2. Tes tertulis (potensi akademik dan bidang keahlian)
        3. Wawancara dan simulasi
        4. Pemeriksaan kesehatan
        5. Pengumuman hasil seleksi
        """)
    
    with st.expander("Apakah ada biaya pendaftaran?"):
        st.markdown("""
        Tidak, pendaftaran program SPPI tidak dipungut biaya (gratis).
        """)

if __name__ == "__main__":
    main()
