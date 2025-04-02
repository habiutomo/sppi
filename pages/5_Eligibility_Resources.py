import streamlit as st
from utils.data_utils import load_eligibility_criteria

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Eligibility & Resources",
    page_icon="📝",
    layout="wide"
)

def main():
    # Header
    st.title("Eligibilitas dan Sumber Daya")
    
    # Load eligibility data
    eligibility = load_eligibility_criteria()
    
    # Introduction
    st.markdown("""
    # Panduan Eligibilitas dan Aplikasi SPPI 2025 - Fokus Kesehatan Gizi
    
    Halaman ini menyediakan informasi lengkap tentang persyaratan, proses aplikasi, dan sumber daya untuk 
    calon peserta Program Sarjana Penggerak Pembangunan Indonesia (SPPI) 2025 dengan fokus kesehatan gizi.
    
    > **Catatan:** Informasi pada halaman ini bersifat informatif. Untuk persyaratan resmi dan detail lebih lanjut, 
    silakan kunjungi portal resmi SPPI.
    """)
    
    # Eligibility criteria
    st.header("Kriteria Eligibilitas")
    
    criteria_col1, criteria_col2 = st.columns(2)
    
    with criteria_col1:
        st.subheader("Persyaratan Umum")
        for requirement in eligibility['general_requirements']:
            st.markdown(f"- {requirement}")
    
    with criteria_col2:
        st.subheader("Persyaratan Khusus Bidang Gizi")
        for requirement in eligibility['nutrition_specialization_requirements']:
            st.markdown(f"- {requirement}")
    
    # Application process
    st.header("Proses Aplikasi")
    
    # Timeline visual
    timeline_data = eligibility['timeline']
    
    st.markdown("### Timeline Aplikasi")
    
    timeline_cols = st.columns(5)
    
    with timeline_cols[0]:
        st.markdown(f"#### {timeline_data['registration_start']}")
        st.markdown("Pendaftaran Dibuka")
    
    with timeline_cols[1]:
        st.markdown(f"#### {timeline_data['registration_end']}")
        st.markdown("Pendaftaran Ditutup")
    
    with timeline_cols[2]:
        st.markdown(f"#### {timeline_data['selection_process']}")
        st.markdown("Proses Seleksi")
    
    with timeline_cols[3]:
        st.markdown(f"#### {timeline_data['announcement']}")
        st.markdown("Pengumuman Hasil")
    
    with timeline_cols[4]:
        st.markdown(f"#### {timeline_data['placement_start']}")
        st.markdown("Mulai Penempatan")
    
    # Application steps
    st.subheader("Tahapan Aplikasi")
    
    # Create a sequential display of application steps
    for i, step in enumerate(eligibility['application_process']):
        step_col1, step_col2 = st.columns([1, 3])
        
        with step_col1:
            st.markdown(f"### Tahap {i+1}")
        
        with step_col2:
            st.info(step)
    
    # Required documents
    st.header("Dokumen yang Diperlukan")
    
    document_cols = st.columns(2)
    
    half_length = len(eligibility['documents_required']) // 2
    
    with document_cols[0]:
        for document in eligibility['documents_required'][:half_length + len(eligibility['documents_required']) % 2]:
            st.markdown(f"- {document}")
    
    with document_cols[1]:
        for document in eligibility['documents_required'][half_length + len(eligibility['documents_required']) % 2:]:
            st.markdown(f"- {document}")
    
    # Resources
    st.header("Sumber Daya")
    
    # Format resources as clickable cards
    resource_cols = st.columns(2)
    
    for i, resource in enumerate(eligibility['resources']):
        col_idx = i % 2
        
        with resource_cols[col_idx]:
            st.markdown(f"""
            <div style="padding: 10px; border-radius: 5px; border: 1px solid #ddd; margin-bottom: 10px;">
                <h3>{resource['name']}</h3>
                <p>{resource['description']}</p>
                <a href="{resource['url']}" target="_blank">Kunjungi Resource</a>
            </div>
            """, unsafe_allow_html=True)
    
    # Preparation tips
    st.header("Tips Persiapan")
    
    tip_cols = st.columns(3)
    
    with tip_cols[0]:
        st.subheader("Persiapan Dokumen")
        st.markdown("""
        - Mulai menyiapkan dan memverifikasi dokumen lebih awal
        - Pastikan ijazah dan transkrip nilai telah dilegalisir
        - Siapkan salinan digital semua dokumen (scan berwarna)
        - Periksa validitas dan masa berlaku KTP
        - Siapkan CV yang diperbarui dengan fokus pada pengalaman kesehatan gizi
        """)
    
    with tip_cols[1]:
        st.subheader("Persiapan Tes")
        st.markdown("""
        - Pelajari materi dasar kesehatan gizi masyarakat
        - Pahami isu-isu gizi di Indonesia, terutama stunting
        - Latih kemampuan analisis data dan pemecahan masalah
        - Kembangkan pemahaman tentang program gizi nasional
        - Siapkan diri untuk tes pemecahan masalah kasus nyata
        """)
    
    with tip_cols[2]:
        st.subheader("Persiapan Wawancara")
        st.markdown("""
        - Refleksikan motivasi dan komitmen Anda untuk program ini
        - Siapkan contoh pengalaman relevan di bidang gizi/kesehatan
        - Kembangkan pemahaman tentang budaya daerah potensial penempatan
        - Praktik menjawab pertanyaan situasional
        - Tunjukkan adaptabilitas dan kemampuan bekerja dalam lingkungan terbatas
        """)
    
    # Selection criteria
    st.header("Kriteria Seleksi")
    
    st.markdown("""
    Seleksi SPPI 2025 untuk formasi kesehatan gizi akan mempertimbangkan beberapa faktor utama:
    
    ### 1. Kompetensi Akademik (30%)
    - Latar belakang pendidikan yang relevan
    - Prestasi akademik dan pengalaman penelitian
    - Pengetahuan tentang kesehatan gizi dan kesehatan masyarakat
    
    ### 2. Pengalaman & Keterampilan (25%)
    - Pengalaman kerja/magang di bidang kesehatan
    - Keterampilan teknis yang relevan
    - Keterlibatan dalam kegiatan sosial dan kemasyarakatan
    
    ### 3. Potensi Kepemimpinan (20%)
    - Pengalaman kepemimpinan
    - Inisiatif dan kemampuan memecahkan masalah
    - Visi dan strategi untuk kontribusi
    
    ### 4. Motivasi & Komitmen (15%)
    - Kejelasan motivasi bergabung dengan program
    - Komitmen untuk berkontribusi pada pembangunan
    - Kesiapan menghadapi tantangan di daerah penempatan
    
    ### 5. Kesesuaian dengan Kebutuhan Program (10%)
    - Kesesuaian profil dengan fokus program tahun 2025
    - Kemampuan bahasa daerah (jika relevan)
    - Pemahaman tentang budaya dan konteks lokal
    """)
    
    # Frequently Asked Questions
    st.header("Pertanyaan yang Sering Diajukan (FAQ)")
    
    with st.expander("Apakah ada batasan usia untuk pendaftaran?"):
        st.markdown("""
        Ya, batas usia maksimal untuk pendaftar adalah 27 tahun pada saat mendaftar.
        """)
    
    with st.expander("Apakah ada ketentuan khusus untuk IPK?"):
        st.markdown("""
        Ya, pendaftar harus memiliki IPK minimal 3.00 dari skala 4.00.
        """)
    
    with st.expander("Saya bukan lulusan bidang kesehatan/gizi, apakah saya bisa mendaftar untuk formasi gizi?"):
        st.markdown("""
        Formasi kesehatan gizi diprioritaskan untuk lulusan bidang Gizi, Kesehatan Masyarakat, Kedokteran, 
        atau bidang terkait lainnya. Namun, lulusan bidang lain dengan pengalaman yang relevan di bidang 
        kesehatan gizi juga dapat mendaftar, meskipun daya saingnya mungkin lebih rendah.
        """)
    
    with st.expander("Apakah saya bisa memilih lokasi penempatan?"):
        st.markdown("""
        Pendaftar dapat mengajukan preferensi lokasi, tetapi keputusan akhir penempatan akan ditentukan 
        oleh panitia SPPI berdasarkan kebutuhan program dan kesesuaian kandidat. Semua pendaftar harus 
        bersedia ditempatkan di seluruh wilayah Indonesia.
        """)
    
    with st.expander("Berapa besar tunjangan yang akan diterima?"):
        st.markdown("""
        Besaran tunjangan bervariasi tergantung lokasi penempatan. Secara umum, tunjangan meliputi:
        
        - Tunjangan bulanan pokok
        - Tunjangan perumahan (atau akomodasi disediakan)
        - Asuransi kesehatan
        - Tunjangan transportasi
        
        Detail besaran tunjangan akan diinformasikan saat penawaran penempatan.
        """)
    
    with st.expander("Berapa lama durasi program SPPI?"):
        st.markdown("""
        Durasi program SPPI adalah 1 tahun dan dapat diperpanjang berdasarkan evaluasi kinerja.
        """)
    
    with st.expander("Bagaimana proses seleksi akan dilaksanakan?"):
        st.markdown("""
        Proses seleksi meliputi:
        
        1. Seleksi administrasi
        2. Tes potensi akademik dan bahasa
        3. Tes bidang kesehatan gizi
        4. Wawancara dan simulasi
        5. Pemeriksaan kesehatan
        6. Pengumuman hasil
        """)
    
    with st.expander("Apakah ada biaya yang harus dibayarkan untuk mendaftar?"):
        st.markdown("""
        Tidak, pendaftaran SPPI tidak dipungut biaya sama sekali. Berhati-hatilah terhadap penipuan 
        yang mengatasnamakan program SPPI.
        """)
    
    # Success profiles
    st.header("Profil Sukses Peserta SPPI")
    
    profile_col1, profile_col2 = st.columns(2)
    
    with profile_col1:
        st.markdown("""
        ### Ahmad Ridwan, Ahli Gizi
        
        **Latar Belakang:** Sarjana Gizi dari Universitas Indonesia
        
        **Penempatan:** Kabupaten Sumba Timur, NTT
        
        **Kontribusi Utama:**
        - Mengembangkan program edukasi gizi berbasis kearifan lokal
        - Melatih kader posyandu dalam pemantauan status gizi balita
        - Membangun sistem peringatan dini untuk risiko malnutrisi
        
        **Pencapaian:** Penurunan kasus stunting sebesar 12% di desa dampingan dalam setahun
        
        **Kutipan:**
        *"SPPI memberikan kesempatan bagi saya untuk menerapkan ilmu secara langsung di masyarakat yang paling membutuhkan. Tantangan di lapangan membantu saya berkembang secara profesional dan personal."*
        """)
    
    with profile_col2:
        st.markdown("""
        ### Siti Aminah, Kesehatan Masyarakat
        
        **Latar Belakang:** Sarjana Kesehatan Masyarakat dari Universitas Airlangga
        
        **Penempatan:** Kabupaten Mamberamo Tengah, Papua
        
        **Kontribusi Utama:**
        - Mengintegrasikan praktik kesehatan tradisional dengan pendekatan gizi modern
        - Mengembangkan program ketahanan pangan berbasis budaya lokal
        - Memberdayakan perempuan dalam produksi makanan bergizi
        
        **Pencapaian:** Peningkatan 35% cakupan pemantauan pertumbuhan balita dan adopsi praktik pemberian makan sehat
        
        **Kutipan:**
        *"Program SPPI membuka mata saya tentang realitas di lapangan dan pentingnya pendekatan yang disesuaikan dengan konteks lokal. Pengalaman ini mengubah cara saya memandang intervensi kesehatan masyarakat."*
        """)
    
    # Final call to action
    st.header("Mulai Perjalanan SPPI Anda")
    
    st.markdown("""
    Jika Anda memiliki semangat untuk berkontribusi pada perbaikan gizi masyarakat Indonesia dan 
    memenuhi persyaratan yang disebutkan di atas, kami mendorong Anda untuk mendaftar di Program 
    SPPI 2025 dengan fokus kesehatan gizi.
    
    ### Langkah Selanjutnya:
    
    1. Kunjungi [portal resmi SPPI](https://sppi.kemdikbud.go.id) untuk informasi terbaru
    2. Daftar untuk menerima notifikasi ketika pendaftaran dibuka
    3. Mulai menyiapkan dokumen dan materi yang diperlukan
    4. Bergabung dengan grup diskusi calon pendaftar untuk informasi dan tips
    
    **Jadilah bagian dari solusi untuk meningkatkan kesehatan gizi masyarakat Indonesia!**
    """)
    
    # Helpdesk information
    st.markdown("---")
    st.subheader("Butuh Bantuan?")
    
    help_col1, help_col2, help_col3 = st.columns(3)
    
    with help_col1:
        st.markdown("""
        ### 📧 Email
        helpdesk@sppi.kemdikbud.go.id
        """)
    
    with help_col2:
        st.markdown("""
        ### ☎️ Telepon
        (021) 5790-3333 ext. 2022
        """)
    
    with help_col3:
        st.markdown("""
        ### 💬 Live Chat
        Tersedia pada portal resmi SPPI
        """)

if __name__ == "__main__":
    main()
