import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.data_utils import load_nutrition_data, load_placement_opportunities

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Prediksi Kebutuhan Formasi",
    page_icon="📊",
    layout="wide"
)

def main():
    # Header
    st.title("Prediksi Kebutuhan Formasi SPPI 2025")
    
    # Introduction
    st.markdown("""
    # Sistem Prediksi Kebutuhan Formasi SPPI 2025 - Fokus Kesehatan Gizi
    
    Halaman ini menyajikan model prediktif untuk kebutuhan formasi Program SPPI 2025 dalam bidang kesehatan gizi
    berdasarkan data demografis, kesehatan, dan pendidikan. Proyeksi ini dapat membantu pemerintah dan sektor swasta
    untuk merencanakan kolaborasi dalam mengatasi tantangan gizi nasional.
    
    > **Catatan:** Model prediksi ini menggunakan kombinasi data historis dan proyeksi berdasarkan indikator kesehatan terkini.
    """)
    
    # Load data
    nutrition_data = load_nutrition_data()
    placement_data = load_placement_opportunities()
    
    # Create simulation data for prediction model
    # This would typically come from machine learning models in production
    def generate_prediction_data():
        provinces = nutrition_data['province'].unique()
        predictions = []
        
        for province in provinces:
            province_nutrition = nutrition_data[nutrition_data['province'] == province].iloc[0]
            
            # Generate prediction based on nutrition indicators
            # Higher stunting leads to higher formasi needs
            stunting_factor = province_nutrition['stunting_percentage'] / 20  # normalize
            
            # Higher wasting also increases needs
            wasting_factor = province_nutrition['wasting_percentage'] / 10  # normalize
            
            # Lower health workers increases needs
            inverse_health_worker = 5 - province_nutrition['health_workers_per_1000']
            if inverse_health_worker < 0:
                inverse_health_worker = 0
            health_worker_factor = inverse_health_worker / 5  # normalize
            
            # Calculate basic needs with some randomness for simulation
            base_needs = int(20 + stunting_factor * 30 + wasting_factor * 20 + health_worker_factor * 25 + np.random.normal(0, 5))
            
            # Adjust based on priority level
            priority_adjustment = province_nutrition['priority_level'] / 3
            formasi_needed = int(base_needs * priority_adjustment)
            
            # Ensure reasonable range
            if formasi_needed < 10:
                formasi_needed = 10
            if formasi_needed > 100:
                formasi_needed = 100
            
            # Calculate current placements from placement data
            current_placements = placement_data[placement_data['province'] == province]['positions_available'].sum()
            
            # Calculate gap
            gap = formasi_needed - current_placements
            
            # Private sector opportunity score (higher when gap is higher)
            private_opportunity = np.clip(int(gap / 10) + np.random.randint(1, 5), 1, 10)
            
            # Required skills based on indicators
            if province_nutrition['stunting_percentage'] > 25:
                primary_need = "Specialist Gizi Anak"
            elif province_nutrition['wasting_percentage'] > 12:
                primary_need = "Nutritionist Klinis"
            elif province_nutrition['obesity_percentage'] > 20:
                primary_need = "Edukator Gizi"
            elif province_nutrition['anemia_percentage'] > 30:
                primary_need = "Specialist Gizi Maternal"
            else:
                primary_need = "Public Health Nutritionist"
            
            # Create prediction entry
            predictions.append({
                'province': province,
                'region': province_nutrition['region'],
                'formasi_needed': formasi_needed,
                'current_placements': current_placements,
                'gap': gap,
                'primary_need': primary_need,
                'priority_level': province_nutrition['priority_level'],
                'private_sector_opportunity': private_opportunity
            })
        
        return pd.DataFrame(predictions)
    
    prediction_data = generate_prediction_data()
    
    # Metrics overview
    st.header("Ringkasan Prediksi Kebutuhan")
    
    total_needed = prediction_data['formasi_needed'].sum()
    total_gap = prediction_data['gap'].sum()
    high_priority_provinces = len(prediction_data[prediction_data['priority_level'] >= 4])
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        st.metric("Total Kebutuhan Formasi", f"{total_needed:,}")
    
    with metrics_col2:
        st.metric("Gap Penempatan Saat Ini", f"{total_gap:,}")
    
    with metrics_col3:
        st.metric("Provinsi Prioritas Tinggi", f"{high_priority_provinces}")
    
    with metrics_col4:
        avg_opportunity = prediction_data['private_sector_opportunity'].mean()
        st.metric("Rata-rata Skor Peluang Swasta", f"{avg_opportunity:.1f}/10")
    
    # Prediction map
    st.header("Peta Prediksi Kebutuhan Formasi")
    
    # Create a scatter map with prediction data
    fig = px.scatter_geo(
        prediction_data,
        lat=prediction_data['province'].apply(lambda x: -6 + (hash(x) % 10) / 10),  # Simulate coordinates
        lon=prediction_data['province'].apply(lambda x: 107 + (hash(x[::-1]) % 25) / 10),
        color='formasi_needed',
        size='formasi_needed',
        hover_name='province',
        hover_data={
            'formasi_needed': True,
            'current_placements': True,
            'gap': True,
            'primary_need': True,
            'priority_level': True
        },
        title='Prediksi Kebutuhan Formasi SPPI 2025 berdasarkan Provinsi',
        color_continuous_scale=px.colors.sequential.Plasma
    )
    
    # Center on Indonesia
    fig.update_geos(
        center=dict(lat=-2, lon=118),
        projection_scale=5,
        visible=True,
        resolution=50,
        showcountries=True,
        countrycolor="Black",
        showcoastlines=True,
        coastlinecolor="Black",
        showland=True,
        landcolor="lightgray",
        showocean=True,
        oceancolor="aliceblue"
    )
    
    fig.update_layout(height=600)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Regional analysis
    st.header("Analisis Kebutuhan berdasarkan Wilayah")
    
    region_tab1, region_tab2 = st.tabs(["Kebutuhan per Region", "Distribusi Keahlian"])
    
    with region_tab1:
        # Group by region
        region_needs = prediction_data.groupby('region')[['formasi_needed', 'current_placements', 'gap']].sum().reset_index()
        
        # Create horizontal bar chart for regions
        fig = px.bar(
            region_needs,
            y='region',
            x=['current_placements', 'gap'],
            orientation='h',
            title='Kebutuhan Formasi dan Gap berdasarkan Region',
            labels={
                'value': 'Jumlah Formasi',
                'region': 'Region',
                'variable': 'Kategori'
            },
            color_discrete_map={
                'current_placements': '#0066cc',
                'gap': '#ff9900'
            },
            barmode='stack'
        )
        
        fig.update_layout(
            legend=dict(
                title='',
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1
            ),
            yaxis_title='',
            xaxis_title='Jumlah Formasi',
            height=400
        )
        
        # Update legend labels
        newnames = {'current_placements': 'Penempatan Saat Ini', 'gap': 'Gap Kebutuhan'}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Add explanation
        st.markdown("""
        **Insight:**
        
        Grafik di atas menunjukkan perbandingan antara penempatan saat ini dan gap kebutuhan di setiap region.
        Region dengan gap besar memerlukan fokus lebih dalam alokasi formasi SPPI 2025 dan berpotensi untuk kolaborasi dengan sektor swasta.
        """)
    
    with region_tab2:
        # Count primary needs by region
        need_counts = pd.crosstab(
            prediction_data['region'], 
            prediction_data['primary_need']
        ).reset_index()
        
        # Melt for plotting
        need_counts_melted = pd.melt(
            need_counts, 
            id_vars=['region'], 
            var_name='keahlian', 
            value_name='jumlah'
        )
        
        # Create stacked bar chart
        fig = px.bar(
            need_counts_melted,
            x='region',
            y='jumlah',
            color='keahlian',
            title='Distribusi Kebutuhan Keahlian berdasarkan Region',
            labels={
                'region': 'Region',
                'jumlah': 'Jumlah Provinsi',
                'keahlian': 'Keahlian Utama Dibutuhkan'
            },
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        
        fig.update_layout(
            legend=dict(
                title='Keahlian:',
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1
            ),
            xaxis_title='',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Insight:**
        
        Grafik di atas menampilkan distribusi kebutuhan keahlian di setiap region. Perbedaan ini menunjukkan:
        - Daerah dengan prevalensi stunting tinggi membutuhkan lebih banyak specialist gizi anak
        - Daerah dengan prevalensi wasting tinggi memerlukan nutritionist klinis
        - Daerah dengan tingkat obesitas tinggi membutuhkan edukator gizi
        
        Informasi ini dapat membantu dalam perencanaan pelatihan dan kolaborasi dengan institusi pendidikan.
        """)
    
    # Gap analysis and projection
    st.header("Analisis Gap dan Proyeksi")
    
    gap_col1, gap_col2 = st.columns(2)
    
    with gap_col1:
        # Sort by gap
        top_gap = prediction_data.sort_values('gap', ascending=False).head(10)
        
        # Create bar chart for top 10 provinces with highest gap
        fig = px.bar(
            top_gap,
            x='province',
            y='gap',
            color='priority_level',
            color_continuous_scale='Reds',
            title='10 Provinsi dengan Gap Terbesar',
            labels={
                'province': 'Provinsi',
                'gap': 'Gap Kebutuhan',
                'priority_level': 'Tingkat Prioritas'
            }
        )
        
        fig.update_layout(
            xaxis_tickangle=-45,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with gap_col2:
        # Compare gap with private sector opportunity
        fig = px.scatter(
            prediction_data,
            x='gap',
            y='private_sector_opportunity',
            size='formasi_needed',
            color='priority_level',
            hover_name='province',
            color_continuous_scale='Viridis',
            title='Peluang Kolaborasi Sektor Swasta berdasarkan Gap',
            labels={
                'gap': 'Gap Kebutuhan Formasi',
                'private_sector_opportunity': 'Skor Peluang Sektor Swasta (1-10)',
                'priority_level': 'Tingkat Prioritas'
            }
        )
        
        fig.update_layout(height=400)
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed forecast table
    st.header("Tabel Prediksi Detail")
    
    # Add filters for table
    st.sidebar.header("Filter Tabel Prediksi")
    
    # Region filter
    regions = sorted(prediction_data['region'].unique())
    selected_regions = st.sidebar.multiselect(
        "Region",
        options=regions,
        default=regions
    )
    
    # Minimum gap filter
    min_gap = st.sidebar.slider(
        "Gap Minimum",
        min_value=0,
        max_value=int(prediction_data['gap'].max()),
        value=0
    )
    
    # Priority level filter
    min_priority = st.sidebar.slider(
        "Tingkat Prioritas Minimum",
        min_value=1,
        max_value=5,
        value=1
    )
    
    # Apply filters
    filtered_pred = prediction_data.copy()
    
    if selected_regions:
        filtered_pred = filtered_pred[filtered_pred['region'].isin(selected_regions)]
    
    filtered_pred = filtered_pred[filtered_pred['gap'] >= min_gap]
    filtered_pred = filtered_pred[filtered_pred['priority_level'] >= min_priority]
    
    # Format data for display
    display_pred = filtered_pred.copy()
    display_pred.columns = [
        'Provinsi',
        'Region',
        'Formasi Dibutuhkan',
        'Penempatan Saat Ini',
        'Gap',
        'Kebutuhan Utama',
        'Tingkat Prioritas',
        'Skor Peluang Swasta'
    ]
    
    # Show table
    if not display_pred.empty:
        st.write(f"Menampilkan {len(display_pred)} dari {len(prediction_data)} provinsi")
        st.dataframe(display_pred.sort_values('Gap', ascending=False), height=400)
    else:
        st.warning("Tidak ada data yang sesuai dengan filter yang dipilih")
    
    # Recommendations for private sector
    st.header("Rekomendasi Kolaborasi Sektor Swasta")
    
    # Create recommendation cards
    recom_col1, recom_col2, recom_col3 = st.columns(3)
    
    with recom_col1:
        st.markdown("""
        ### 🎓 Pelatihan & Pengembangan
        
        **Provinsi Target:** Papua, Papua Barat, NTT, NTB, Maluku
        
        **Kebutuhan:**
        - Pelatihan khusus untuk Specialist Gizi Anak
        - Program pendampingan tenaga gizi di daerah terpencil
        - Pengembangan kurikulum khusus gizi stunting
        
        **Potensi Dampak:** 
        Peningkatan kapasitas lokal untuk mengatasi masalah gizi kronis di daerah prioritas tinggi
        
        **Mitra Potensial:**
        Institusi pendidikan, lembaga pelatihan profesional, perusahaan nutrisi global
        """)
    
    with recom_col2:
        st.markdown("""
        ### 🥗 Produk & Intervensi Gizi
        
        **Provinsi Target:** Sulawesi Tengah, Kalimantan Barat, Aceh, Gorontalo
        
        **Kebutuhan:**
        - Produk fortifikasi makanan untuk mengatasi defisiensi zat besi
        - Suplementasi mikronutrien untuk ibu hamil dan balita
        - Program pemberian makanan tambahan berbasis local food
        
        **Potensi Dampak:** 
        Penurunan prevalensi anemia dan peningkatan status gizi sensitif di daerah prioritas
        
        **Mitra Potensial:**
        Produsen makanan, perusahaan farmasi, produsen suplementasi gizi
        """)
    
    with recom_col3:
        st.markdown("""
        ### 📱 Teknologi & Monitoring
        
        **Provinsi Target:** Seluruh Indonesia dengan prioritas Jawa Timur, Jawa Barat, Sulawesi Selatan
        
        **Kebutuhan:**
        - Sistem monitoring gizi berbasis aplikasi mobile
        - Platform edukasi gizi untuk masyarakat
        - Sistem manajemen data kesehatan gizi terintegrasi
        
        **Potensi Dampak:** 
        Peningkatan efektivitas program melalui pengumpulan data real-time dan intervensi tepat sasaran
        
        **Mitra Potensial:**
        Perusahaan teknologi, startup kesehatan, penyedia solusi data
        """)
    
    # Private sector benefits
    st.subheader("Manfaat bagi Sektor Swasta")
    
    benefit_col1, benefit_col2 = st.columns(2)
    
    with benefit_col1:
        # Create donut chart for impact areas
        impact_labels = ['Kesehatan', 'Edukasi', 'Teknologi', 'Penelitian', 'Infrastruktur', 'Lainnya']
        impact_values = [30, 25, 20, 15, 7, 3]
        
        fig = go.Figure(data=[go.Pie(
            labels=impact_labels,
            values=impact_values,
            hole=.4,
            textinfo='label+percent',
            marker_colors=px.colors.qualitative.Pastel
        )])
        
        fig.update_layout(
            title_text='Area Dampak Kolaborasi',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with benefit_col2:
        st.markdown("""
        ### Keuntungan Strategis:
        
        1. **Pengembangan Pasar**: Akses ke daerah baru dan segmen konsumen yang belum terlayani
        
        2. **Branding & Reputasi**: Pengakuan sebagai mitra pemerintah dalam program nasional prioritas
        
        3. **Jaringan**: Koneksi dengan stakeholders pemerintah dan masyarakat lokal
        
        4. **Inovasi Produk**: Insight untuk pengembangan produk yang relevan dengan kebutuhan lokal
        
        5. **Talent Pipeline**: Akses ke lulusan terlatih sebagai kandidat rekrutmen potensial
        
        6. **Riset & Data**: Kesempatan memperoleh data nyata untuk penelitian dan pengembangan
        """)
    
    # Next steps
    st.header("Langkah Kolaborasi Selanjutnya")
    
    st.markdown("""
    ### Jalur Kemitraan SPPI 2025:
    
    1. **Konsultasi Awal**
       * Diskusi kebutuhan dan kapasitas
       * Identifikasi area kolaborasi potensial
       * Penyelarasan dengan target strategis
    
    2. **Pengembangan Proposal**
       * Penyusunan proposal kemitraan detail
       * Penentuan target dan indikator keberhasilan
       * Perencanaan alokasi sumber daya
    
    3. **Implementasi & Monitoring**
       * Penandatanganan MoU dengan kementerian terkait
       * Pelaksanaan program sesuai rencana
       * Sistem pemantauan dan evaluasi bersama
    
    4. **Evaluasi & Skalabilitas**
       * Pengukuran dampak dan hasil program
       * Identifikasi pembelajaran dan praktik terbaik
       * Peluang untuk perluasan dan replikasi model
    
    **Untuk informasi lebih lanjut tentang kemitraan, hubungi:**
    
    Tim Kemitraan SPPI 2025  
    Email: partnership@sppi.kemdikbud.go.id  
    Telepon: (021) 5790-3335
    """)

if __name__ == "__main__":
    main()