import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.data_utils import load_private_sector_opportunities

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Dashboard Kolaborasi Swasta",
    page_icon="💼",
    layout="wide"
)

def main():
    # Header
    st.title("Dashboard Kolaborasi Sektor Swasta")
    
    # Introduction
    st.markdown("""
    # Dashboard Kolaborasi Sektor Swasta untuk SPPI 2025
    
    Dashboard interaktif ini menyediakan visualisasi dan analitik untuk memfasilitasi kolaborasi antara 
    program SPPI 2025 dan sektor swasta di bidang kesehatan gizi. Informasi ini dapat membantu perusahaan 
    dan organisasi swasta untuk mengidentifikasi peluang kerjasama strategis yang selaras dengan 
    tujuan bisnis dan dampak sosial.
    
    > **Catatan:** Dashboard ini menyediakan proyeksi dan peluang potensial berdasarkan kebutuhan program 
    SPPI 2025. Untuk informasi yang lebih spesifik, silakan hubungi tim kemitraan SPPI.
    """)
    
    # Load data
    private_opps = load_private_sector_opportunities()
    
    # Create simulation data for additional analyses
    def create_sector_simulation_data():
        # Define sectors and their participation level
        sectors = [
            "Makanan & Minuman", "Farmasi & Suplemen", "Teknologi Kesehatan", 
            "Retail & Distribusi", "Pendidikan & Pelatihan", "Logistik & Supply Chain",
            "Konsultan Kesehatan", "Manufaktur", "Teknologi Informasi", "Asuransi Kesehatan"
        ]
        
        # Create some meaningful data
        data = []
        for sector in sectors:
            if sector in ["Makanan & Minuman", "Farmasi & Suplemen"]:
                current_participation = np.random.randint(40, 70)
                potential_growth = np.random.randint(15, 30)
            elif sector in ["Teknologi Kesehatan", "Pendidikan & Pelatihan", "Teknologi Informasi"]:
                current_participation = np.random.randint(25, 45)
                potential_growth = np.random.randint(30, 50)
            else:
                current_participation = np.random.randint(10, 35)
                potential_growth = np.random.randint(20, 40)
            
            investment_level = "High" if current_participation > 50 else "Medium" if current_participation > 30 else "Low"
            roi_score = np.random.randint(60, 95)
            impact_score = np.random.randint(65, 98)
            
            data.append({
                "sector": sector,
                "current_participation": current_participation,
                "potential_growth": potential_growth,
                "investment_level": investment_level,
                "roi_score": roi_score,
                "impact_score": impact_score,
                "total_opportunities": np.random.randint(5, 25)
            })
        
        return pd.DataFrame(data)
    
    # Create regional opportunity data
    def create_regional_opportunity_data():
        regions = ["Indonesia Barat", "Indonesia Tengah", "Indonesia Timur", "Nasional"]
        opportunity_types = [
            "Pelatihan & Pemberdayaan", "Distribusi Produk Gizi", "Riset & Pengembangan", 
            "Teknologi & Inovasi", "Pendanaan Program", "Infrastruktur"
        ]
        
        data = []
        
        for region in regions:
            for opportunity in opportunity_types:
                # Add some variation based on region and opportunity type
                if region == "Indonesia Timur":
                    # Higher need in eastern Indonesia
                    need_level = np.random.randint(70, 100)
                    business_potential = np.random.randint(60, 90)
                elif region == "Indonesia Barat":
                    # More business potential in western Indonesia but lower need
                    need_level = np.random.randint(40, 70)
                    business_potential = np.random.randint(70, 95)
                elif region == "Indonesia Tengah":
                    # Balanced in central Indonesia
                    need_level = np.random.randint(50, 85)
                    business_potential = np.random.randint(50, 80)
                else:  # National
                    need_level = np.random.randint(60, 80)
                    business_potential = np.random.randint(65, 85)
                
                # Adjust based on opportunity type
                if opportunity in ["Distribusi Produk Gizi", "Teknologi & Inovasi"]:
                    business_potential += np.random.randint(5, 15)
                elif opportunity in ["Pendanaan Program", "Infrastruktur"]:
                    need_level += np.random.randint(5, 15)
                
                # Ensure values are in range 0-100
                need_level = min(100, need_level)
                business_potential = min(100, business_potential)
                
                # Calculate a combined score
                overall_score = (need_level + business_potential) / 2
                
                data.append({
                    "region": region,
                    "opportunity_type": opportunity,
                    "need_level": need_level,
                    "business_potential": business_potential,
                    "overall_score": overall_score
                })
        
        return pd.DataFrame(data)
    
    # Create case studies data
    def create_case_studies():
        return [
            {
                "title": "Program Fortifikasi Makanan di NTT",
                "company": "PT Nutrisi Indonesia",
                "sector": "Makanan & Minuman",
                "region": "Indonesia Timur",
                "investment": "Rp 5 Miliar",
                "duration": "24 bulan",
                "impact": [
                    "15,000 keluarga menerima produk fortifikasi",
                    "Penurunan 22% kasus anemia pada anak",
                    "50 tenaga kesehatan lokal dilatih"
                ],
                "business_benefits": [
                    "Pengembangan pasar baru di Indonesia Timur",
                    "Peningkatan citra perusahaan sebagai pioneer nutrisi",
                    "Pembelajaran untuk inovasi produk baru"
                ]
            },
            {
                "title": "Aplikasi Monitoring Gizi untuk SPPI",
                "company": "TechHealth Indonesia",
                "sector": "Teknologi Informasi",
                "region": "Nasional",
                "investment": "Rp 3.5 Miliar",
                "duration": "18 bulan",
                "impact": [
                    "Pemantauan real-time 50,000 anak balita",
                    "Peningkatan 35% dalam deteksi dini masalah gizi",
                    "Data analytics untuk perbaikan program gizi"
                ],
                "business_benefits": [
                    "Ekspansi ke pasar kesehatan publik",
                    "Akuisisi data untuk pengembangan AI kesehatan",
                    "Kontrak jangka panjang dengan pemerintah"
                ]
            },
            {
                "title": "Program Pelatihan Fasilitator Gizi",
                "company": "EduHealth Consortium",
                "sector": "Pendidikan & Pelatihan",
                "region": "Indonesia Barat",
                "investment": "Rp 2 Miliar",
                "duration": "12 bulan",
                "impact": [
                    "500 fasilitator gizi terlatih",
                    "Jangkauan program ke 200+ desa",
                    "Pengembangan kurikulum gizi berbasis kearifan lokal"
                ],
                "business_benefits": [
                    "Pengakuan sebagai penyedia pelatihan kesehatan terkemuka",
                    "Sertifikasi dan akreditasi nasional",
                    "Pipeline talent untuk rekrutmen"
                ]
            }
        ]
    
    # Generate simulation data
    sector_data = create_sector_simulation_data()
    regional_opps = create_regional_opportunity_data()
    case_studies = create_case_studies()
    
    # Summary metrics
    st.header("Metrik Utama Kolaborasi")
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        st.metric("Total Peluang Kolaborasi", f"{len(private_opps)}")
    
    with metrics_col2:
        high_impact_opps = len(private_opps[private_opps['investment_level'] == 'High'])
        st.metric("Peluang Dampak Tinggi", f"{high_impact_opps}")
    
    with metrics_col3:
        total_sectors = len(sector_data)
        st.metric("Sektor Industri Terlibat", f"{total_sectors}")
    
    with metrics_col4:
        avg_roi = sector_data['roi_score'].mean()
        st.metric("Rata-rata ROI Score", f"{avg_roi:.1f}/100")
    
    # Sector analysis
    st.header("Analisis Partisipasi Sektor Swasta")
    
    sector_col1, sector_col2 = st.columns([3, 2])
    
    with sector_col1:
        # Create a horizontal bar chart showing current participation and potential
        sorted_sectors = sector_data.sort_values('current_participation')
        
        fig = go.Figure()
        
        # Add current participation bars
        fig.add_trace(go.Bar(
            y=sorted_sectors['sector'],
            x=sorted_sectors['current_participation'],
            name='Partisipasi Saat Ini (%)',
            orientation='h',
            marker=dict(color='#0066cc')
        ))
        
        # Add potential growth bars
        fig.add_trace(go.Bar(
            y=sorted_sectors['sector'],
            x=sorted_sectors['potential_growth'],
            name='Potensi Pertumbuhan (%)',
            orientation='h',
            marker=dict(color='#00cc99'),
            base=sorted_sectors['current_participation']
        ))
        
        fig.update_layout(
            title='Partisipasi dan Potensi Pertumbuhan berdasarkan Sektor',
            xaxis_title='Persentase (%)',
            yaxis_title='',
            barmode='stack',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with sector_col2:
        # Create a bubble chart showing ROI vs Impact by sector
        fig = px.scatter(
            sector_data,
            x='roi_score',
            y='impact_score',
            size='total_opportunities',
            color='investment_level',
            hover_name='sector',
            text='sector',
            title='ROI vs Dampak Sosial berdasarkan Sektor',
            labels={
                'roi_score': 'Potensi ROI (0-100)',
                'impact_score': 'Skor Dampak Sosial (0-100)',
                'investment_level': 'Tingkat Investasi'
            },
            color_discrete_map={
                'Low': '#92c5de',
                'Medium': '#4393c3',
                'High': '#2166ac'
            },
            size_max=40
        )
        
        fig.update_traces(
            textposition='top center',
            textfont=dict(size=10)
        )
        
        fig.update_layout(
            height=500,
            xaxis=dict(range=[50, 100]),
            yaxis=dict(range=[50, 100])
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Opportunity heatmap
    st.header("Pemetaan Peluang berdasarkan Region")
    
    # Create pivot table for heatmap
    pivot_data = regional_opps.pivot_table(
        values='overall_score',
        index='region',
        columns='opportunity_type',
        aggfunc='mean'
    )
    
    # Create heatmap
    fig = px.imshow(
        pivot_data,
        text_auto='.0f',
        aspect='auto',
        color_continuous_scale='RdYlGn',
        title='Skor Peluang berdasarkan Region dan Tipe Kolaborasi',
        labels=dict(x='Tipe Peluang', y='Region', color='Skor')
    )
    
    fig.update_layout(height=450)
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Interpretasi Peta Panas:**
    
    Peta panas di atas menampilkan skor peluang kolaborasi berdasarkan kombinasi tipe peluang dan region. 
    Skor yang lebih tinggi (hijau) menunjukkan area dengan potensi kolaborasi yang lebih menjanjikan, 
    yang mempertimbangkan baik dampak sosial maupun potensi bisnis.
    
    * Indonesia Timur menunjukkan peluang signifikan di bidang distribusi produk gizi dan infrastruktur
    * Indonesia Barat memiliki skor tinggi untuk teknologi dan inovasi
    * Peluang nasional menunjukkan skor yang konsisten tinggi di berbagai tipe kolaborasi
    """)
    
    # ROI and Impact analysis
    st.header("Analisis ROI dan Dampak")
    
    roi_tab1, roi_tab2 = st.tabs(["ROI berdasarkan Tipe Kolaborasi", "Analisis Dampak"])
    
    with roi_tab1:
        # Use the data from private_opps to create visualization based on collaboration type
        collab_roi = pd.DataFrame({
            'collaboration_type': ['Training & Development', 'Nutritional Product Supply', 'Research Partnership', 
                                'Technology Support', 'Funding Program', 'Community Outreach', 
                                'Infrastructure Development', 'Healthcare Service'],
            'avg_roi': [78, 85, 72, 81, 68, 75, 70, 76],
            'time_to_roi': [12, 18, 24, 15, 36, 9, 30, 18]  # in months
        })
        
        # Create scatter plot for ROI
        fig = px.scatter(
            collab_roi,
            x='time_to_roi',
            y='avg_roi',
            size=[20] * len(collab_roi),  # consistent size
            color='avg_roi',
            hover_name='collaboration_type',
            text='collaboration_type',
            title='ROI vs Waktu berdasarkan Tipe Kolaborasi',
            labels={
                'avg_roi': 'Rata-rata ROI (%)',
                'time_to_roi': 'Waktu untuk ROI (bulan)'
            },
            color_continuous_scale='Viridis'
        )
        
        fig.update_traces(
            textposition='top center',
            textfont=dict(size=10)
        )
        
        fig.update_layout(
            height=500,
            xaxis=dict(range=[0, 40]),
            yaxis=dict(range=[65, 90])
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Insight ROI:**
        
        Grafik di atas menunjukkan perbandingan antara potensi ROI dan waktu yang dibutuhkan untuk mencapai ROI 
        berdasarkan tipe kolaborasi. Beberapa insights penting:
        
        * **Nutritional Product Supply** menunjukkan ROI tertinggi tetapi memerlukan waktu menengah (18 bulan)
        * **Community Outreach** menawarkan waktu ROI tercepat (9 bulan) dengan ROI yang cukup baik
        * **Funding Program** dan **Infrastructure Development** memerlukan waktu lebih lama untuk ROI
        
        Perusahaan dapat memilih tipe kolaborasi berdasarkan preferensi antara ROI jangka pendek vs jangka panjang.
        """)
    
    with roi_tab2:
        # Create impact data
        impact_data = pd.DataFrame({
            'impact_category': ['Perbaikan Status Gizi', 'Peningkatan Kesadaran Masyarakat', 
                                'Pengembangan Kapasitas Lokal', 'Penguatan Sistem Kesehatan', 
                                'Keberlanjutan Program', 'Advokasi Kebijakan'],
            'direct_impact': [85, 78, 65, 60, 55, 40],
            'indirect_impact': [70, 90, 80, 75, 85, 95],
            'measurability': [90, 65, 75, 60, 50, 45]
        })
        
        # Create radar chart for impact
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=impact_data['direct_impact'],
            theta=impact_data['impact_category'],
            fill='toself',
            name='Dampak Langsung',
            line_color='#0066cc'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=impact_data['indirect_impact'],
            theta=impact_data['impact_category'],
            fill='toself',
            name='Dampak Tidak Langsung',
            line_color='#ff9900'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=impact_data['measurability'],
            theta=impact_data['impact_category'],
            fill='toself',
            name='Kemudahan Pengukuran',
            line_color='#00cc66'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=True,
            title='Analisis Dampak Kolaborasi SPPI-Swasta',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Insight Dampak:**
        
        Diagram radar di atas menunjukkan tiga dimensi dampak kemitraan SPPI-swasta:
        
        * **Dampak Langsung** - Efek langsung pada penerima manfaat program
        * **Dampak Tidak Langsung** - Efek sekunder dan jangka panjang
        * **Kemudahan Pengukuran** - Seberapa mudah dampak dapat diukur
        
        Perbaikan status gizi dan peningkatan kesadaran masyarakat menunjukkan dampak tertinggi, 
        sementara kategori seperti advokasi kebijakan memiliki dampak tidak langsung yang lebih besar
        namun lebih sulit untuk diukur dalam jangka pendek.
        """)
    
    # Case studies
    st.header("Studi Kasus Kolaborasi Sukses")
    
    # Display case studies in expandable sections
    for i, case in enumerate(case_studies):
        with st.expander(f"{case['title']} - {case['company']}"):
            case_col1, case_col2 = st.columns([3, 2])
            
            with case_col1:
                st.markdown(f"""
                ### {case['title']}
                
                **Perusahaan:** {case['company']}  
                **Sektor:** {case['sector']}  
                **Region:** {case['region']}  
                **Investasi:** {case['investment']}  
                **Durasi Program:** {case['duration']}
                
                **Dampak Sosial:**
                """)
                
                for impact in case['impact']:
                    st.markdown(f"- {impact}")
                
                st.markdown("**Manfaat Bisnis:**")
                
                for benefit in case['business_benefits']:
                    st.markdown(f"- {benefit}")
            
            with case_col2:
                # Create a gauge chart for success metrics
                success_score = np.random.randint(75, 98)
                
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=success_score,
                    title={'text': "Skor Keberhasilan Program"},
                    gauge={
                        'axis': {'range': [0, 100]},
                        'bar': {'color': "#0066cc"},
                        'steps': [
                            {'range': [0, 50], 'color': "#ff9999"},
                            {'range': [50, 75], 'color': "#ffcc99"},
                            {'range': [75, 100], 'color': "#99cc99"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 90
                        }
                    }
                ))
                
                fig.update_layout(height=300)
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Create ROI vs Impact mini-chart
                roi = np.random.randint(70, 95)
                impact = np.random.randint(75, 98)
                
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=[roi],
                    y=[impact],
                    mode='markers',
                    marker=dict(
                        size=20,
                        color='#0066cc'
                    ),
                    showlegend=False
                ))
                
                fig.update_layout(
                    title="ROI vs Dampak",
                    xaxis=dict(
                        title="Return on Investment",
                        range=[60, 100]
                    ),
                    yaxis=dict(
                        title="Dampak Sosial",
                        range=[60, 100]
                    ),
                    height=200
                )
                
                st.plotly_chart(fig, use_container_width=True)
    
    # Collaboration toolkit
    st.header("Toolkit Kolaborasi")
    
    st.markdown("""
    ### Alat Bantu untuk Merencanakan Kolaborasi SPPI
    
    Tim SPPI menyediakan berbagai toolkit untuk membantu sektor swasta merencanakan dan mengimplementasikan 
    kolaborasi yang efektif:
    """)
    
    toolkit_col1, toolkit_col2, toolkit_col3 = st.columns(3)
    
    with toolkit_col1:
        st.markdown("""
        ### 📋 Template Proposal Kemitraan
        
        Template standar untuk menyusun proposal kolaborasi dengan SPPI, mencakup:
        
        - Format penawaran nilai
        - Struktur anggaran dan pembiayaan
        - Rencana implementasi
        - Kerangka monitoring dan evaluasi
        
        [Unduh Template Proposal](#)
        """)
    
    with toolkit_col2:
        st.markdown("""
        ### 📊 Kalkulator ROI Investasi Sosial
        
        Spreadsheet interaktif untuk menghitung:
        
        - Proyeksi ROI dari investasi sosial
        - Estimasi dampak sosial
        - Analisis biaya-manfaat
        - Model keberlanjutan program
        
        [Akses Kalkulator ROI](#)
        """)
    
    with toolkit_col3:
        st.markdown("""
        ### 🔍 Panduan Due Diligence
        
        Checklist untuk melakukan due diligence sebelum kolaborasi:
        
        - Analisis kebutuhan daerah
        - Pemetaan stakeholder
        - Kajian risiko dan mitigasi
        - Framework legal dan kepatuhan
        
        [Unduh Panduan](#)
        """)
    
    # Next steps
    st.header("Langkah Selanjutnya")
    
    st.markdown("""
    ### Bagaimana Berpartisipasi dalam Program SPPI 2025?
    
    Untuk organisasi sektor swasta yang tertarik berkolaborasi dengan program SPPI 2025, berikut adalah 
    langkah-langkah yang dapat diambil:
    """)
    
    next_col1, next_col2, next_col3, next_col4 = st.columns(4)
    
    with next_col1:
        st.markdown("""
        ### Langkah 1: Explorasi
        
        - Identifikasi area fokus dan interest
        - Review dashboard dan peluang
        - Download materi informasi
        
        [Request Info Pack](#)
        """)
    
    with next_col2:
        st.markdown("""
        ### Langkah 2: Konsultasi
        
        - Jadwalkan konsultasi dengan tim SPPI
        - Diskusikan kebutuhan spesifik
        - Identifikasi keselarasan strategis
        
        [Jadwalkan Konsultasi](#)
        """)
    
    with next_col3:
        st.markdown("""
        ### Langkah 3: Proposal
        
        - Kembangkan konsep kolaborasi
        - Siapkan proposal menggunakan template
        - Ajukan untuk review oleh komite
        
        [Lihat Kriteria Proposal](#)
        """)
    
    with next_col4:
        st.markdown("""
        ### Langkah 4: Implementasi
        
        - Penandatanganan MoU
        - Pengembangan workplan detail
        - Pelaksanaan dan monitoring
        
        [Lihat Success Stories](#)
        """)
    
    # Contact information
    st.header("Kontak Tim Kemitraan")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("""
        ### Tim Kemitraan SPPI 2025
        
        Untuk informasi lebih lanjut tentang peluang kolaborasi, silakan hubungi:
        
        **Email:** partnership@sppi.kemdikbud.go.id  
        **Telepon:** (021) 5790-3335  
        **Alamat:** Gedung C Kemdikbud, Jalan Jenderal Sudirman, Jakarta Pusat
        
        **Jam Kerja:** Senin-Jumat, 08.00-16.00 WIB
        """)
    
    with contact_col2:
        # Create a sample form
        st.markdown("### Formulir Permintaan Informasi")
        
        company_name = st.text_input("Nama Perusahaan")
        business_sector = st.selectbox("Sektor Bisnis", options=[
            "Pilih Sektor", "Makanan & Minuman", "Farmasi & Suplemen", "Teknologi Kesehatan", 
            "Retail & Distribusi", "Pendidikan & Pelatihan", "Logistik & Supply Chain",
            "Konsultan Kesehatan", "Manufaktur", "Teknologi Informasi", "Asuransi Kesehatan", "Lainnya"
        ])
        
        interest_areas = st.multiselect("Area Minat Kolaborasi", options=[
            "Pelatihan & Pemberdayaan", "Distribusi Produk Gizi", "Riset & Pengembangan", 
            "Teknologi & Inovasi", "Pendanaan Program", "Infrastruktur"
        ])
        
        contact_person = st.text_input("Nama Kontak Person")
        email = st.text_input("Email")
        
        if st.button("Kirim Permintaan"):
            st.success("Terima kasih! Permintaan informasi Anda telah dikirim. Tim kami akan menghubungi Anda dalam 2 hari kerja.")

if __name__ == "__main__":
    main()