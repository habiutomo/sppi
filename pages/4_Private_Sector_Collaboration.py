import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_utils import load_private_sector_opportunities
from utils.visualization_utils import create_collaboration_types_chart

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Private Sector Collaboration",
    page_icon="🤝",
    layout="wide"
)

def main():
    # Header
    st.title("Kolaborasi Sektor Swasta")
    
    # Load data
    collaboration_data = load_private_sector_opportunities()
    
    # Introduction
    st.markdown("""
    # Peluang Kolaborasi Sektor Swasta dalam SPPI 2025 - Fokus Kesehatan Gizi
    
    Program SPPI 2025 membuka peluang kolaborasi strategis dengan pihak swasta, khususnya yang bergerak 
    di sektor kesehatan dan gizi. Halaman ini menyajikan informasi tentang bentuk-bentuk 
    kolaborasi potensial, manfaat kemitraan, dan bagaimana organisasi swasta dapat berpartisipasi.
    
    > **Catatan:** Program SPPI mendorong partisipasi multi-stakeholder untuk meningkatkan dampak program dan keberlanjutannya.
    """)
    
    # Why collaborate
    st.header("Mengapa Berkolaborasi dengan SPPI?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 💼 Dampak Sosial
        
        - Berkontribusi langsung pada perbaikan gizi masyarakat Indonesia
        - Mendukung upaya penurunan stunting nasional
        - Memperkuat ketahanan pangan di daerah prioritas
        - Membantu pencapaian Tujuan Pembangunan Berkelanjutan (SDGs)
        """)
    
    with col2:
        st.markdown("""
        ### 🌱 Tanggung Jawab Sosial Perusahaan
        
        - Implementasi nyata program CSR bidang kesehatan
        - Pengakuan sebagai mitra pembangunan nasional
        - Peningkatan citra perusahaan sebagai pendukung kesehatan masyarakat
        - Dokumentasi dampak sosial untuk pelaporan keberlanjutan
        """)
    
    with col3:
        st.markdown("""
        ### 📈 Nilai Strategis
        
        - Akses ke jaringan program nasional
        - Peluang pengembangan pasar di daerah baru
        - Pemahaman mendalam tentang kebutuhan gizi lokal
        - Pengujian produk/program dalam konteks nyata
        - Rekrutmen talenta dari peserta SPPI
        """)
    
    # Types of collaboration
    st.header("Jenis Kolaborasi")
    
    # Display collaboration types chart
    collaboration_chart = create_collaboration_types_chart(collaboration_data)
    st.plotly_chart(collaboration_chart, use_container_width=True)
    
    # Detail for each collaboration type
    collab_tab1, collab_tab2, collab_tab3, collab_tab4 = st.tabs([
        "Pelatihan & Pengembangan", 
        "Program Nutrisi & Produk",
        "Penelitian & Teknologi",
        "Pendanaan & Infrastruktur"
    ])
    
    with collab_tab1:
        st.subheader("Pelatihan & Pengembangan")
        
        st.markdown("""
        ### 🎓 Pelatihan untuk Peserta SPPI
        
        Sektor swasta dapat memberikan pelatihan khusus untuk meningkatkan kapasitas peserta SPPI dalam bidang:
        - Manajemen program gizi masyarakat
        - Teknik edukasi gizi yang efektif
        - Analisis data kesehatan dan gizi
        - Komunikasi perubahan perilaku
        
        ### 👨‍🏫 Mentoring Profesional
        
        - Program mentoring jangka panjang oleh ahli dari perusahaan
        - Sesi berbagi pengalaman dari praktisi industri
        - Bimbingan pengembangan proyek intervensi gizi
        
        ### 🛠️ Pengembangan Keterampilan Teknis
        
        - Pelatihan penggunaan alat/teknologi kesehatan
        - Sertifikasi khusus untuk peserta SPPI
        - Workshop praktis implementasi program gizi
        """)
    
    with collab_tab2:
        st.subheader("Program Nutrisi & Produk")
        
        st.markdown("""
        ### 🥗 Distribusi Produk Nutrisi
        
        - Penyediaan produk nutrisi untuk program intervensi gizi
        - Suplementasi mikronutrien untuk kelompok rentan
        - Produk gizi khusus untuk penanganan malnutrisi
        - Fortifikasi makanan untuk masyarakat lokal
        
        ### 🍲 Program Edukasi Gizi
        
        - Pengembangan materi edukasi gizi yang inovatif
        - Kampanye kesadaran pola makan sehat
        - Program memasak sehat berbasis bahan lokal
        - Modul pendidikan gizi untuk berbagai kelompok usia
        
        ### 🌾 Penguatan Ketahanan Pangan Lokal
        
        - Program pertanian gizi (nutrition-sensitive agriculture)
        - Diversifikasi tanaman pangan lokal kaya nutrisi
        - Teknologi pengolahan dan pengawetan makanan sederhana
        - Pemberdayaan petani lokal untuk produksi pangan bergizi
        """)
    
    with collab_tab3:
        st.subheader("Penelitian & Teknologi")
        
        st.markdown("""
        ### 🔬 Kemitraan Penelitian
        
        - Studi efektivitas intervensi gizi
        - Penelitian pola konsumsi dan status gizi masyarakat
        - Analisis faktor determinan masalah gizi di daerah spesifik
        - Pengembangan metode intervensi gizi yang inovatif
        
        ### 📱 Solusi Teknologi
        
        - Aplikasi mobile untuk pemantauan status gizi
        - Sistem informasi manajemen data kesehatan gizi
        - Platform pembelajaran jarak jauh untuk edukasi gizi
        - Alat diagnostik sederhana untuk deteksi masalah gizi
        
        ### 📊 Analisis Data & Evaluasi
        
        - Dukungan analisis data program gizi
        - Pengembangan dashboard monitoring intervensi
        - Metode evaluasi dampak program
        - Visualisasi data untuk pengambilan keputusan
        """)
    
    with collab_tab4:
        st.subheader("Pendanaan & Infrastruktur")
        
        st.markdown("""
        ### 💰 Program Hibah & Pendanaan
        
        - Pendanaan proyek intervensi gizi inovatif
        - Hibah peralatan dan perlengkapan kesehatan
        - Beasiswa untuk pengembangan kapasitas peserta SPPI
        - Insentif untuk pencapaian target program
        
        ### 🏥 Pengembangan Infrastruktur
        
        - Pembangunan atau renovasi pusat gizi masyarakat
        - Penyediaan fasilitas penyimpanan makanan
        - Pengembangan dapur komunal untuk demonstrasi gizi
        - Fasilitas air bersih dan sanitasi untuk mendukung program gizi
        
        ### 🚚 Dukungan Logistik
        
        - Bantuan transportasi untuk distribusi produk gizi
        - Jaringan rantai dingin untuk produk nutrisi
        - Sistem manajemen logistik untuk program gizi
        - Solusi distribusi untuk daerah terpencil
        """)
    
    # Success stories (placeholder for future real stories)
    st.header("Contoh Kolaborasi Sukses")
    
    success_col1, success_col2 = st.columns(2)
    
    with success_col1:
        st.markdown("""
        ### Kemitraan Perusahaan Nutrisi di NTT
        
        **Tantangan**: Tingginya angka stunting di kabupaten terpencil di NTT dengan akses terbatas ke produk nutrisi.
        
        **Solusi**: Kolaborasi dengan perusahaan nutrisi untuk menyediakan suplementasi mikronutrien dan pelatihan kader kesehatan.
        
        **Hasil**:
        - 200+ kader kesehatan terlatih dalam edukasi gizi
        - 5,000+ keluarga menerima paket suplementasi
        - Penurunan 18% kasus malnutrisi dalam 1 tahun
        - Pengembangan modul edukasi gizi berbasis budaya lokal
        """)
    
    with success_col2:
        st.markdown("""
        ### Program Teknologi Kesehatan di Papua
        
        **Tantangan**: Sulitnya pemantauan status gizi di daerah terpencil Papua dengan keterbatasan tenaga kesehatan.
        
        **Solusi**: Kemitraan dengan perusahaan teknologi untuk mengembangkan aplikasi sederhana pemantauan gizi yang dapat digunakan offline.
        
        **Hasil**:
        - 50+ desa terpencil terhubung dengan sistem pemantauan
        - Peningkatan 40% dalam identifikasi dini kasus malnutrisi
        - Data real-time untuk perencanaan intervensi tepat sasaran
        - Adopsi teknologi oleh Dinas Kesehatan setempat
        """)
    
    # How to get involved
    st.header("Cara Berpartisipasi")
    
    st.markdown("""
    ### Langkah-langkah Menjadi Mitra SPPI 2025:
    
    1. **Identifikasi Peluang Kolaborasi** - Tentukan jenis kolaborasi yang sesuai dengan kapasitas dan fokus organisasi Anda
    
    2. **Kirim Proposal Kemitraan** - Ajukan proposal yang menjelaskan bentuk kolaborasi, cakupan, dan kontribusi potensial
    
    3. **Konsultasi Awal** - Diskusikan proposal dengan tim SPPI untuk menyelaraskan dengan kebutuhan program
    
    4. **Penyusunan Rencana Kerja** - Kembangkan rencana kerja detail dengan timeline, target, dan indikator keberhasilan
    
    5. **Penandatanganan MoU** - Formalisasi kemitraan melalui Memorandum of Understanding
    
    6. **Implementasi Program** - Pelaksanaan program kolaborasi sesuai rencana kerja
    
    7. **Monitoring dan Evaluasi** - Pemantauan berkala dan evaluasi dampak kemitraan
    """)
    
    # Show collaboration opportunities table
    st.header("Daftar Peluang Kolaborasi Saat Ini")
    
    # Add sidebar filters for the opportunities table
    st.sidebar.header("Filter Peluang Kolaborasi")
    
    # Collaboration type filter
    collab_types = sorted(collaboration_data['collaboration_type'].unique())
    selected_collab_types = st.sidebar.multiselect(
        "Jenis Kolaborasi",
        options=collab_types,
        default=[]
    )
    
    # Target region filter
    regions = sorted(collaboration_data['target_region'].unique())
    selected_regions = st.sidebar.multiselect(
        "Wilayah Target",
        options=regions,
        default=[]
    )
    
    # Investment level filter
    investment_levels = ["Low", "Medium", "High"]
    selected_investment_levels = st.sidebar.multiselect(
        "Tingkat Investasi",
        options=investment_levels,
        default=[]
    )
    
    # Apply filters
    filtered_opps = collaboration_data.copy()
    
    if selected_collab_types:
        filtered_opps = filtered_opps[filtered_opps['collaboration_type'].isin(selected_collab_types)]
        
    if selected_regions:
        filtered_opps = filtered_opps[filtered_opps['target_region'].isin(selected_regions)]
        
    if selected_investment_levels:
        filtered_opps = filtered_opps[filtered_opps['investment_level'].isin(selected_investment_levels)]
    
    # Display data if available
    if not filtered_opps.empty:
        # Create a display copy with better column names
        display_columns = {
            'id': 'ID',
            'collaboration_type': 'Jenis Kolaborasi',
            'description': 'Deskripsi',
            'target_region': 'Wilayah Target',
            'investment_level': 'Tingkat Investasi',
            'duration_months': 'Durasi (bulan)',
            'benefits': 'Jumlah Manfaat',
            'requirements': 'Jumlah Persyaratan'
        }
        
        display_opps = filtered_opps.copy()
        display_opps.columns = [display_columns.get(col, col) for col in display_opps.columns]
        
        # Format the investment level column for better readability
        investment_map = {"Low": "Rendah", "Medium": "Menengah", "High": "Tinggi"}
        display_opps['Tingkat Investasi'] = display_opps['Tingkat Investasi'].map(investment_map)
        
        st.write(f"Menampilkan {len(filtered_opps)} dari {len(collaboration_data)} peluang kolaborasi")
        st.dataframe(display_opps, height=400)
        
        # Add a section to explore a specific opportunity
        st.subheader("Eksplorasi Detail Peluang")
        
        selected_id = st.selectbox(
            "Pilih ID Peluang untuk Detail Lebih Lanjut",
            options=display_opps['ID'].tolist()
        )
        
        if selected_id:
            selected_opp = filtered_opps[filtered_opps['id'] == selected_id].iloc[0]
            
            # Create detail card
            st.markdown(f"""
            ### Peluang Kolaborasi #{selected_id}: {selected_opp['description']}
            
            **Jenis Kolaborasi:** {selected_opp['collaboration_type']}
            
            **Wilayah Target:** {selected_opp['target_region']}
            
            **Tingkat Investasi:** {investment_map[selected_opp['investment_level']]}
            
            **Durasi Program:** {selected_opp['duration_months']} bulan
            
            **Manfaat Utama:**
            """)
            
            # Generate some fictitious benefits based on the collaboration type and other fields
            if selected_opp['collaboration_type'] == 'Training & Development':
                benefits = [
                    "Peningkatan kapasitas tenaga kesehatan lokal",
                    "Transfer pengetahuan dari sektor swasta ke pelaksana program",
                    "Pengembangan modul pelatihan yang dapat direplikasi",
                    "Sertifikasi profesional untuk peserta SPPI"
                ]
            elif 'Nutritional Product' in selected_opp['collaboration_type']:
                benefits = [
                    "Distribusi produk nutrisi ke masyarakat target",
                    "Pengenalan produk ke wilayah baru",
                    "Analisis dampak produk pada status gizi",
                    "Adaptasi produk sesuai kebutuhan lokal"
                ]
            elif 'Research' in selected_opp['collaboration_type']:
                benefits = [
                    "Data penelitian dari daerah yang sulit dijangkau",
                    "Publikasi bersama hasil penelitian",
                    "Pengembangan solusi berbasis bukti",
                    "Validasi metodologi di konteks lokal"
                ]
            elif 'Technology' in selected_opp['collaboration_type']:
                benefits = [
                    "Penerapan teknologi di daerah prioritas",
                    "Umpan balik langsung dari pengguna di lapangan",
                    "Adaptasi teknologi untuk konteks lokal",
                    "Pengembangan kapasitas digital masyarakat"
                ]
            elif 'Funding' in selected_opp['collaboration_type']:
                benefits = [
                    "Dampak sosial yang terukur dari program pendanaan",
                    "Pengakuan sebagai pendukung utama program nasional",
                    "Alokasi dana CSR yang efektif dan tepat sasaran",
                    "Laporan dampak komprehensif untuk stakeholders"
                ]
            else:
                benefits = [
                    "Kolaborasi dengan program nasional prioritas",
                    "Kontribusi pada perbaikan status gizi masyarakat",
                    "Membangun hubungan dengan pemangku kepentingan lokal",
                    "Mendukung pencapaian target pembangunan nasional"
                ]
            
            # Display benefits
            for i, benefit in enumerate(benefits[:selected_opp['benefits']]):
                st.markdown(f"- {benefit}")
            
            st.markdown("**Persyaratan & Komitmen:**")
            
            # Generate some fictitious requirements based on the collaboration type and investment level
            if selected_opp['investment_level'] == 'High':
                requirements = [
                    "Komitmen pendanaan jangka panjang (minimal durasi program)",
                    "Penyediaan tim teknis untuk implementasi dan monitoring",
                    "Partisipasi dalam evaluasi berkala program",
                    "Berbagi pengetahuan dan sumber daya dengan mitra lokal",
                    "Penyesuaian program dengan kebijakan nasional"
                ]
            elif selected_opp['investment_level'] == 'Medium':
                requirements = [
                    "Kontribusi sumber daya sesuai cakupan program",
                    "Tim koordinasi untuk penyelarasan dengan program SPPI",
                    "Partisipasi dalam pertemuan koordinasi triwulanan",
                    "Berbagi data dan laporan dengan pemangku kepentingan"
                ]
            else:
                requirements = [
                    "Kontribusi spesifik sesuai kapasitas perusahaan",
                    "Penunjukan koordinator program",
                    "Laporan berkala tentang implementasi program"
                ]
            
            # Display requirements
            for i, requirement in enumerate(requirements[:selected_opp['requirements']]):
                st.markdown(f"- {requirement}")
            
            # Add contact button
            st.markdown("---")
            st.markdown("Tertarik dengan peluang ini? Hubungi tim kami untuk diskusi lebih lanjut.")
            contact_col1, contact_col2, contact_col3 = st.columns([1, 1, 1])
            
            with contact_col2:
                st.button("Hubungi Tim Kolaborasi SPPI", key=f"contact_{selected_id}")
    else:
        st.warning("Tidak ada peluang kolaborasi yang sesuai dengan filter yang dipilih")
    
    # Contact information
    st.header("Kontak Kolaborasi")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        ### Tim Kemitraan SPPI 2025
        
        **Email:** kemitraan@sppi.kemdikbud.go.id
        
        **Telepon:** (021) 5790-3333 ext. 5225
        
        **Alamat:** 
        Gedung C Lt. 13
        Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi
        Jl. Jenderal Sudirman, Senayan, Jakarta 10270
        """)
    
    with contact_col2:
        st.markdown("""
        ### Jadwalkan Konsultasi
        
        Tim Kemitraan SPPI siap membantu organisasi Anda mengeksplorasi peluang kolaborasi 
        yang sesuai dengan fokus dan kapasitas Anda.
        
        Silakan isi formulir kontak di portal resmi SPPI atau hubungi kami melalui email 
        untuk menjadwalkan konsultasi awal.
        
        **Dokumen yang Perlu Disiapkan:**
        - Profil singkat organisasi
        - Area minat kolaborasi
        - Kapasitas dan sumber daya yang dapat dikontribusikan
        - Wilayah target yang diminati (jika ada)
        """)

if __name__ == "__main__":
    main()
