import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_utils import load_placement_opportunities, load_nutrition_data
from utils.map_utils import display_map_with_filters
from utils.visualization_utils import create_specialization_distribution

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Placement Opportunities",
    page_icon="🗺️",
    layout="wide"
)

def main():
    # Header
    st.title("Peluang Penempatan SPPI 2025")
    
    # Load data
    placement_data = load_placement_opportunities()
    nutrition_data = load_nutrition_data()
    
    # Introduction
    st.markdown("""
    Halaman ini menampilkan informasi tentang peluang penempatan untuk program SPPI 2025 
    dengan fokus kesehatan gizi. Gunakan peta interaktif dan filter untuk menemukan 
    lokasi yang sesuai dengan minat dan keahlian Anda.
    
    > **Catatan:** Lokasi penempatan aktual dapat berubah berdasarkan kebutuhan daerah dan hasil seleksi.
    """)
    
    # Overview statistics
    total_positions = placement_data['positions_available'].sum()
    total_locations = len(placement_data)
    total_provinces = placement_data['province'].nunique()
    remote_percentage = (len(placement_data[placement_data['remote_area'] == True]) / total_locations) * 100
    
    st.header("Statistik Penempatan")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Posisi Tersedia", f"{total_positions:,}")
    
    with col2:
        st.metric("Total Lokasi Penempatan", f"{total_locations:,}")
    
    with col3:
        st.metric("Provinsi Tercakup", f"{total_provinces} dari 34")
    
    with col4:
        st.metric("Lokasi Area Terpencil", f"{remote_percentage:.1f}%")
    
    # Interactive map with filters
    display_map_with_filters(placement_data, "placement_page")
    
    # Distribution of positions
    st.header("Distribusi Posisi")
    
    dist_tab1, dist_tab2, dist_tab3 = st.tabs(["Berdasarkan Spesialisasi", "Berdasarkan Provinsi", "Berdasarkan Prioritas"])
    
    with dist_tab1:
        specialization_chart = create_specialization_distribution(placement_data)
        st.plotly_chart(specialization_chart, use_container_width=True)
        
        st.markdown("""
        **Tentang Spesialisasi:**
        
        Program SPPI 2025 dengan fokus kesehatan gizi membutuhkan berbagai spesialisasi untuk 
        mengatasi tantangan gizi yang kompleks di Indonesia. Spesialisasi ini mencakup ahli gizi, 
        kesehatan masyarakat, pendidikan kesehatan, dan bidang terkait lainnya.
        """)
    
    with dist_tab2:
        # Group by province and sum positions
        province_positions = placement_data.groupby('province')['positions_available'].sum().reset_index()
        province_positions = province_positions.sort_values('positions_available', ascending=False)
        
        fig = px.bar(
            province_positions,
            x='province',
            y='positions_available',
            color='positions_available',
            color_continuous_scale=px.colors.sequential.Viridis,
            title='Distribusi Posisi berdasarkan Provinsi',
            labels={
                'province': 'Provinsi',
                'positions_available': 'Jumlah Posisi'
            }
        )
        
        fig.update_layout(
            xaxis_tickangle=-45,
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Merge with nutrition data to show correlation
        merged_data = province_positions.merge(
            nutrition_data[['province', 'stunting_percentage']].groupby('province').mean(),
            on='province'
        )
        
        if not merged_data.empty:
            correlation_fig = px.scatter(
                merged_data,
                x='stunting_percentage',
                y='positions_available',
                color='positions_available',
                size='positions_available',
                hover_name='province',
                title='Korelasi antara Tingkat Stunting dan Jumlah Posisi',
                labels={
                    'stunting_percentage': 'Persentase Stunting',
                    'positions_available': 'Jumlah Posisi'
                }
            )
            
            st.plotly_chart(correlation_fig, use_container_width=True)
            
            st.markdown("""
            **Insight:** 
            Grafik di atas menunjukkan bagaimana alokasi posisi SPPI 2025 berkorelasi dengan 
            tingkat stunting di setiap provinsi. Provinsi dengan tingkat stunting yang lebih 
            tinggi cenderung mendapatkan lebih banyak posisi untuk membantu mengatasi masalah tersebut.
            """)
    
    with dist_tab3:
        # Group by priority level and sum positions
        priority_positions = placement_data.groupby('priority_level')['positions_available'].sum().reset_index()
        
        fig = px.pie(
            priority_positions,
            values='positions_available',
            names='priority_level',
            title='Distribusi Posisi berdasarkan Tingkat Prioritas',
            color='priority_level',
            color_discrete_sequence=px.colors.sequential.RdBu_r,
            hole=0.4
        )
        
        fig.update_layout(
            height=500,
            annotations=[dict(text='Tingkat<br>Prioritas', x=0.5, y=0.5, font_size=20, showarrow=False)]
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Tentang Tingkat Prioritas:**
        
        Tingkat prioritas ditentukan berdasarkan kombinasi dari beberapa faktor, termasuk:
        - Tingkat prevalensi stunting dan masalah gizi lainnya
        - Ketersediaan tenaga kesehatan gizi di daerah tersebut
        - Akses terhadap layanan kesehatan dasar
        - Status daerah (3T: Terdepan, Terluar, Tertinggal)
        
        Tingkat 5 menunjukkan prioritas tertinggi, dengan kebutuhan intervensi gizi yang paling mendesak.
        """)
    
    # Placement details
    st.header("Detail Penempatan")
    
    # Add filters to sidebar for the detail view
    st.sidebar.header("Filter Tabel Detail")
    
    # Province filter for table
    provinces = sorted(placement_data['province'].unique())
    selected_provinces_table = st.sidebar.multiselect(
        "Pilih Provinsi untuk Tabel",
        options=provinces,
        default=[]
    )
    
    # Specialization filter for table
    specializations = sorted(placement_data['specialization'].unique())
    selected_specializations_table = st.sidebar.multiselect(
        "Pilih Spesialisasi untuk Tabel",
        options=specializations,
        default=[]
    )
    
    # Priority level filter for table
    min_priority_table = st.sidebar.slider(
        "Tingkat Prioritas Minimum untuk Tabel",
        min_value=1,
        max_value=5,
        value=1
    )
    
    # Apply filters for table
    filtered_table_data = placement_data.copy()
    
    if selected_provinces_table:
        filtered_table_data = filtered_table_data[filtered_table_data['province'].isin(selected_provinces_table)]
        
    if selected_specializations_table:
        filtered_table_data = filtered_table_data[filtered_table_data['specialization'].isin(selected_specializations_table)]
        
    filtered_table_data = filtered_table_data[filtered_table_data['priority_level'] >= min_priority_table]
    
    # Prepare data for display
    display_columns = {
        'province': 'Provinsi',
        'district': 'Kabupaten/Kota',
        'specialization': 'Spesialisasi',
        'positions_available': 'Jumlah Posisi',
        'priority_level': 'Tingkat Prioritas',
        'remote_area': 'Area Terpencil',
        'housing_provided': 'Akomodasi Disediakan',
        'stipend_level': 'Tingkat Tunjangan'
    }
    
    display_data = filtered_table_data[display_columns.keys()].copy()
    display_data.columns = [display_columns[col] for col in display_data.columns]
    
    # Convert boolean columns to Yes/No
    display_data['Area Terpencil'] = display_data['Area Terpencil'].map({True: 'Ya', False: 'Tidak'})
    display_data['Akomodasi Disediakan'] = display_data['Akomodasi Disediakan'].map({True: 'Ya', False: 'Tidak'})
    
    # Show table with pagination
    if not display_data.empty:
        st.write(f"Menampilkan {len(display_data)} dari {len(placement_data)} penempatan")
        st.dataframe(display_data, height=400)
    else:
        st.warning("Tidak ada data yang sesuai dengan filter yang dipilih")
    
    # Placement benefits and considerations
    st.header("Manfaat dan Pertimbangan Penempatan")
    
    benefit_col1, benefit_col2 = st.columns(2)
    
    with benefit_col1:
        st.subheader("Manfaat Penempatan")
        st.markdown("""
        - **Tunjangan Bulanan**: Peserta akan menerima tunjangan bulanan yang besarannya bervariasi berdasarkan lokasi penempatan.
        
        - **Akomodasi**: Sebagian besar lokasi menyediakan akomodasi atau tunjangan perumahan.
        
        - **Pengembangan Profesional**: Pelatihan dan pengembangan kapasitas berkelanjutan selama program.
        
        - **Jejaring**: Kesempatan untuk membangun jejaring profesional dengan institusi kesehatan dan pemerintah daerah.
        
        - **Pengalaman Lapangan**: Pengalaman praktis yang berharga dalam implementasi program kesehatan gizi di lapangan.
        
        - **Kontribusi Nyata**: Kesempatan untuk berkontribusi secara langsung dalam mengatasi masalah gizi masyarakat Indonesia.
        """)
    
    with benefit_col2:
        st.subheader("Pertimbangan Penting")
        st.markdown("""
        - **Lokasi Terpencil**: Beberapa penempatan berada di daerah terpencil dengan akses terbatas ke fasilitas modern.
        
        - **Tantangan Budaya**: Peserta perlu beradaptasi dengan budaya dan bahasa lokal.
        
        - **Infrastruktur Terbatas**: Beberapa daerah memiliki keterbatasan infrastruktur seperti listrik, air bersih, atau internet.
        
        - **Dukungan Kesehatan**: Akses ke layanan kesehatan komprehensif mungkin terbatas di beberapa lokasi.
        
        - **Mobilitas**: Beberapa daerah memiliki tantangan transportasi dan mobilitas.
        
        - **Komitmen Waktu**: Peserta diharapkan untuk berkomitmen penuh selama durasi program (minimal 1 tahun).
        """)
    
    # FAQ about placements
    st.header("Pertanyaan yang Sering Diajukan tentang Penempatan")
    
    with st.expander("Bagaimana proses penempatan ditentukan?"):
        st.markdown("""
        Proses penempatan ditentukan berdasarkan kombinasi dari:
        1. Kebutuhan daerah berdasarkan data kesehatan gizi
        2. Kompetensi dan latar belakang pendidikan peserta
        3. Preferensi peserta (meskipun tidak dijamin)
        4. Pertimbangan khusus seperti bahasa daerah dan pengalaman sebelumnya
        
        Tim SPPI akan mencocokkan kandidat dengan lokasi yang paling sesuai untuk memaksimalkan dampak program.
        """)
    
    with st.expander("Apakah saya dapat memilih lokasi penempatan saya?"):
        st.markdown("""
        Peserta dapat mengajukan preferensi lokasi penempatan, namun keputusan akhir akan 
        ditentukan oleh tim SPPI berdasarkan kebutuhan program dan kesesuaian kandidat.
        
        Semua peserta harus bersedia ditempatkan di seluruh wilayah Indonesia sebagai prasyarat
        untuk berpartisipasi dalam program SPPI.
        """)
    
    with st.expander("Apa yang termasuk dalam paket tunjangan?"):
        st.markdown("""
        Paket tunjangan untuk peserta SPPI 2025 biasanya mencakup:
        - Tunjangan bulanan (bervariasi berdasarkan lokasi)
        - Tunjangan perumahan atau akomodasi (di sebagian besar lokasi)
        - Asuransi kesehatan
        - Tunjangan transportasi untuk penempatan dan akhir program
        - Tunjangan komunikasi (di beberapa lokasi)
        - Tunjangan pengembangan profesional
        
        Detail spesifik akan disampaikan saat penawaran penempatan.
        """)
    
    with st.expander("Bagaimana dengan keamanan dan dukungan selama penempatan?"):
        st.markdown("""
        SPPI berkomitmen untuk memastikan keamanan dan kesejahteraan semua peserta program. Dukungan yang disediakan meliputi:
        
        - Orientasi dan pelatihan pra-penempatan komprehensif
        - Kontak darurat 24/7
        - Koordinator daerah yang dapat dihubungi untuk bantuan
        - Evaluasi keamanan lokasi penempatan secara berkelanjutan
        - Protokol evakuasi untuk situasi darurat
        - Dukungan psikososial jika diperlukan
        
        Peserta juga akan terhubung dengan jaringan alumni SPPI dan peserta lain di daerah tersebut.
        """)
    
    with st.expander("Apa yang terjadi setelah program berakhir?"):
        st.markdown("""
        Setelah program SPPI 2025 berakhir, peserta memiliki beberapa jalur potensial:
        
        1. **Perpanjangan program**: Peserta berkinerja baik dapat ditawarkan perpanjangan untuk tahun kedua
        
        2. **Rekrutmen oleh pemerintah daerah**: Beberapa peserta dapat direkrut oleh pemda tempat mereka bertugas
        
        3. **Peluang kerja sektor swasta**: Kemitraan dengan sektor swasta membuka peluang rekrutmen
        
        4. **Studi lanjut**: Program beasiswa untuk studi lanjut (dalam dan luar negeri)
        
        5. **Jaringan alumni**: Akses ke jaringan alumni SPPI untuk peluang karir jangka panjang
        
        Semua peserta akan menerima sertifikat penyelesaian program dan surat rekomendasi.
        """)

if __name__ == "__main__":
    main()
