import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_utils import load_nutrition_data
from utils.visualization_utils import (
    create_regional_nutrition_comparison,
    create_provincial_nutrition_map,
    create_nutrition_indicators_radar,
    create_priority_level_distribution,
    create_correlation_heatmap
)
from utils.map_utils import create_nutrition_heatmap, folium_static

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Nutrition Data",
    page_icon="📊",
    layout="wide"
)

def main():
    # Header
    st.title("Data Gizi Nasional")
    
    # Load nutrition data
    nutrition_data = load_nutrition_data()
    
    # Introduction
    st.markdown("""
    Halaman ini menampilkan data dan visualisasi status gizi di seluruh Indonesia.
    Data ini menjadi dasar untuk penentuan formasi dan penempatan SPPI 2025 di bidang kesehatan gizi.
    
    > **Catatan:** Gunakan filter di sidebar untuk menyesuaikan tampilan data.
    """)
    
    # Sidebar filters
    st.sidebar.header("Filter Data")
    
    # Region filter
    regions = sorted(nutrition_data['region'].unique())
    selected_regions = st.sidebar.multiselect(
        "Pilih Region",
        options=regions,
        default=regions
    )
    
    # Province filter
    if selected_regions:
        provinces_in_selected_regions = nutrition_data[nutrition_data['region'].isin(selected_regions)]['province'].unique()
        selected_provinces = st.sidebar.multiselect(
            "Pilih Provinsi",
            options=sorted(provinces_in_selected_regions),
            default=[]
        )
    else:
        selected_provinces = []
    
    # Metric filter
    metrics = {
        'stunting_percentage': 'Stunting (%)',
        'wasting_percentage': 'Wasting (%)',
        'obesity_percentage': 'Obesitas (%)',
        'anemia_percentage': 'Anemia (%)',
        'exclusive_breastfeeding': 'ASI Eksklusif (%)',
        'food_security_score': 'Skor Ketahanan Pangan (0-100)'
    }
    
    selected_metric = st.sidebar.selectbox(
        "Pilih Metrik Utama",
        options=list(metrics.keys()),
        format_func=lambda x: metrics[x],
        index=0
    )
    
    # Filter data based on selections
    if selected_regions and not selected_provinces:
        filtered_data = nutrition_data[nutrition_data['region'].isin(selected_regions)]
    elif selected_provinces:
        filtered_data = nutrition_data[nutrition_data['province'].isin(selected_provinces)]
    else:
        filtered_data = nutrition_data
    
    # Display key statistics
    st.header("Statistik Utama")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_stunting = filtered_data['stunting_percentage'].mean()
        st.metric("Rata-rata Stunting", f"{avg_stunting:.1f}%")
    
    with col2:
        avg_wasting = filtered_data['wasting_percentage'].mean()
        st.metric("Rata-rata Wasting", f"{avg_wasting:.1f}%")
    
    with col3:
        avg_obesity = filtered_data['obesity_percentage'].mean()
        st.metric("Rata-rata Obesitas", f"{avg_obesity:.1f}%")
    
    with col4:
        avg_anemia = filtered_data['anemia_percentage'].mean()
        st.metric("Rata-rata Anemia", f"{avg_anemia:.1f}%")
    
    # Map visualization
    st.header("Peta Status Gizi")
    
    map_tab1, map_tab2 = st.tabs(["Peta Interaktif", "Distribusi Provinsi"])
    
    with map_tab1:
        st.markdown(f"Peta di bawah menunjukkan distribusi **{metrics[selected_metric]}** di seluruh Indonesia. Area merah menunjukkan daerah dengan tingkat yang lebih tinggi.")
        nutrition_map = create_nutrition_heatmap(filtered_data)
        folium_static(nutrition_map)
    
    with map_tab2:
        st.markdown(f"Visualisasi distribusi **{metrics[selected_metric]}** berdasarkan provinsi:")
        fig = create_provincial_nutrition_map(filtered_data, selected_metric)
        st.plotly_chart(fig, use_container_width=True)
    
    # Regional comparison
    st.header("Perbandingan Antar Region")
    
    region_chart = create_regional_nutrition_comparison(filtered_data, selected_metric)
    st.plotly_chart(region_chart, use_container_width=True)
    
    # Detailed provincial data
    st.header("Data Detail per Provinsi")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Sort data based on selected metric
        if 'exclusive_breastfeeding' in selected_metric or 'food_security_score' in selected_metric:
            # For positive metrics, higher is better - sort descending
            sorted_data = filtered_data.sort_values(by=selected_metric, ascending=False)
        else:
            # For negative metrics, lower is better - sort ascending
            sorted_data = filtered_data.sort_values(by=selected_metric, ascending=True)
        
        # Create a bar chart
        fig = px.bar(
            sorted_data,
            x='province',
            y=selected_metric,
            color=selected_metric,
            color_continuous_scale='RdYlGn_r' if selected_metric in ['stunting_percentage', 'wasting_percentage', 'anemia_percentage', 'obesity_percentage'] else 'RdYlGn',
            title=f"{metrics[selected_metric]} berdasarkan Provinsi",
            labels={
                'province': 'Provinsi',
                selected_metric: metrics[selected_metric]
            }
        )
        
        fig.update_layout(
            xaxis_tickangle=-45,
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Display priority level distribution
        st.subheader("Distribusi Tingkat Prioritas")
        priority_chart = create_priority_level_distribution(filtered_data)
        st.plotly_chart(priority_chart, use_container_width=True)
        
        st.markdown("""
        **Tentang Tingkat Prioritas:**
        
        Tingkat prioritas (1-5) ditentukan berdasarkan kombinasi dari berbagai indikator gizi, 
        dengan 5 menunjukkan prioritas tertinggi untuk intervensi gizi.
        """)
    
    # Multi-indicator analysis
    st.header("Analisis Multi-Indikator")
    
    indicator_tab1, indicator_tab2 = st.tabs(["Perbandingan Radar", "Korelasi Indikator"])
    
    with indicator_tab1:
        st.markdown("Diagram radar di bawah ini membandingkan beberapa indikator gizi untuk provinsi-provinsi utama:")
        radar_chart = create_nutrition_indicators_radar(nutrition_data)
        st.plotly_chart(radar_chart, use_container_width=True)
    
    with indicator_tab2:
        st.markdown("Matrik korelasi di bawah ini menunjukkan hubungan antar berbagai indikator gizi:")
        corr_fig = create_correlation_heatmap(nutrition_data)
        st.pyplot(corr_fig)
        
        st.markdown("""
        **Interpretasi Korelasi:**
        
        - Nilai positif mendekati 1 menunjukkan korelasi positif kuat
        - Nilai negatif mendekati -1 menunjukkan korelasi negatif kuat
        - Nilai mendekati 0 menunjukkan korelasi lemah atau tidak ada korelasi
        """)
    
    # Table of full data
    st.header("Tabel Data Lengkap")
    
    with st.expander("Lihat Tabel Data Lengkap"):
        # Rename columns for display
        display_columns = {
            'province': 'Provinsi',
            'region': 'Region',
            'stunting_percentage': 'Stunting (%)',
            'wasting_percentage': 'Wasting (%)',
            'obesity_percentage': 'Obesitas (%)',
            'anemia_percentage': 'Anemia (%)',
            'exclusive_breastfeeding': 'ASI Eksklusif (%)',
            'food_security_score': 'Skor Ketahanan Pangan',
            'nutrition_centers': 'Pusat Gizi',
            'health_workers_per_1000': 'Tenaga Kesehatan per 1000',
            'priority_level': 'Tingkat Prioritas'
        }
        
        # Create a display copy of the dataframe with renamed columns
        display_df = filtered_data.copy()
        display_df.columns = [display_columns.get(col, col) for col in display_df.columns]
        
        # Format numeric columns
        for col in display_df.columns:
            if col not in ['Provinsi', 'Region']:
                if 'percentage' in col.lower() or '%' in col:
                    display_df[col] = display_df[col].apply(lambda x: f"{x:.1f}%")
                elif col == 'Tenaga Kesehatan per 1000':
                    display_df[col] = display_df[col].apply(lambda x: f"{x:.2f}")
                elif col == 'Skor Ketahanan Pangan':
                    display_df[col] = display_df[col].apply(lambda x: f"{x:.1f}/100")
        
        st.dataframe(display_df, height=400)
    
    # Data insights
    st.header("Wawasan Data")
    
    st.markdown("""
    ### Kesimpulan Utama:
    
    1. **Distribusi Geografis:** Terdapat kesenjangan signifikan dalam status gizi antara wilayah barat, tengah, dan timur Indonesia.
    
    2. **Faktor Kunci:** Ada korelasi antara stunting dan beberapa indikator lain seperti akses ke layanan kesehatan dan ketahanan pangan.
    
    3. **Area Prioritas:** Beberapa provinsi di Indonesia Timur dan daerah terpencil menunjukkan kebutuhan intervensi gizi yang lebih tinggi.
    
    4. **Tantangan Spesifik:** Setiap daerah memiliki tantangan gizi yang berbeda. Beberapa daerah menghadapi masalah stunting dan wasting yang tinggi, 
       sementara daerah lain lebih berjuang dengan obesitas dan anemia.
    
    5. **Kebutuhan Sumber Daya:** Ada korelasi antara tingkat masalah gizi dengan ketersediaan tenaga kesehatan dan pusat gizi.
    
    ### Rekomendasi untuk SPPI 2025:
    
    - Prioritaskan penempatan di daerah dengan indikator gizi yang buruk dan ketersediaan tenaga kesehatan yang rendah.
    - Sesuaikan fokus program berdasarkan tantangan spesifik di setiap daerah.
    - Tekankan pendekatan kolaboratif yang melibatkan berbagai sektor (kesehatan, pendidikan, pertanian).
    - Desain intervensi yang memperhitungkan faktor sosial, ekonomi, dan budaya lokal.
    """)

if __name__ == "__main__":
    main()
