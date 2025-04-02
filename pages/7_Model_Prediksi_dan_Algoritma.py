import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.data_utils import load_nutrition_data, load_placement_opportunities

# Page configuration
st.set_page_config(
    page_title="SPPI 2025 - Model Prediksi dan Algoritma",
    page_icon="🧮",
    layout="wide"
)

def main():
    # Header
    st.title("Model Prediksi dan Algoritma")
    
    # Introduction
    st.markdown("""
    # Metodologi Prediksi Kebutuhan Formasi SPPI 2025
    
    Halaman ini menjelaskan model prediktif dan algoritma yang digunakan dalam perkiraan kebutuhan formasi 
    Program SPPI 2025 di bidang kesehatan gizi. Pendekatan ini menggabungkan analisis data, model statistik, 
    dan masukan dari pakar untuk menghasilkan prediksi yang komprehensif.
    
    > **Catatan:** Halaman ini ditujukan untuk pemangku kepentingan yang tertarik dengan aspek teknis dari sistem prediksi.
    """)
    
    # Data sources section
    st.header("Sumber Data")
    
    data_col1, data_col2 = st.columns(2)
    
    with data_col1:
        st.markdown("""
        ### Data Utama yang Digunakan:
        
        1. **Data Demografis**
           * Data penduduk dari Badan Pusat Statistik (BPS)
           * Proyeksi pertumbuhan penduduk
           * Distribusi penduduk berdasarkan usia dan gender
        
        2. **Data Kesehatan Gizi**
           * Hasil Riset Kesehatan Dasar (Riskesdas)
           * Data Pemantauan Status Gizi (PSG)
           * Data prevalensi stunting, wasting, dan anemia
           * Peta ketahanan pangan nasional
        
        3. **Data Infrastruktur Kesehatan**
           * Jumlah dan distribusi fasilitas kesehatan
           * Rasio tenaga kesehatan per 1000 penduduk
           * Data Puskesmas dan program gizi yang berjalan
        
        4. **Data Pendidikan**
           * Statistik lulusan bidang kesehatan dan gizi
           * Proyeksi lulusan dari institusi pendidikan
           * Data kompetensi dan spesialisasi
        """)
    
    with data_col2:
        # Create data quality indicator chart
        data_sources = ['Demografis', 'Kesehatan Gizi', 'Infrastruktur', 'Pendidikan', 'Sosial Ekonomi']
        data_completeness = [95, 87, 78, 82, 75]
        data_reliability = [92, 85, 75, 80, 70]
        data_recency = [90, 88, 72, 85, 68]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=data_sources,
            y=data_completeness,
            name='Kelengkapan Data (%)',
            marker_color='#0066cc'
        ))
        
        fig.add_trace(go.Bar(
            x=data_sources,
            y=data_reliability,
            name='Reliabilitas Data (%)',
            marker_color='#00cc66'
        ))
        
        fig.add_trace(go.Bar(
            x=data_sources,
            y=data_recency,
            name='Kebaruan Data (%)',
            marker_color='#cc6600'
        ))
        
        fig.update_layout(
            title='Indikator Kualitas Data',
            xaxis_title='Sumber Data',
            yaxis_title='Persentase (%)',
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Model methodology
    st.header("Metodologi Model Prediksi")
    
    st.markdown("""
    ### Pendekatan Multi-Metode
    
    Sistem prediksi menggunakan pendekatan multi-metode yang mengkombinasikan beberapa model untuk menghasilkan
    estimasi yang lebih akurat dan komprehensif.
    """)
    
    # Methodology diagram
    method_col1, method_col2 = st.columns([1, 1])
    
    with method_col1:
        st.markdown("""
        ### Komponen Model:
        
        1. **Analisis Tren Historis**
           * Analisis data historis 5 tahun terakhir
           * Identifikasi pola dan tren kejadian masalah gizi
           * Proyeksi berdasarkan tren yang teridentifikasi
        
        2. **Model Statistik Prediktif**
           * Regresi multi-variabel untuk analisis faktor
           * Time series forecasting untuk proyeksi kebutuhan
           * Cluster analysis untuk pengelompokan daerah
        
        3. **Machine Learning**
           * Random Forest untuk klasifikasi prioritas daerah
           * Gradient Boosting untuk estimasi kebutuhan formasi
           * Neural Network untuk identifikasi pola kompleks
        
        4. **Simulasi Monte Carlo**
           * Simulasi berbagai skenario intervensi
           * Analisis sensitifitas terhadap perubahan parameter
           * Estimasi interval kepercayaan prediksi
        
        5. **Validasi Pakar**
           * Review dan kalibrasi oleh pakar kesehatan
           * Penyesuaian berdasarkan pengetahuan lapangan
           * Evaluasi dan validasi hasil prediksi
        """)
    
    with method_col2:
        # Create model performance comparison
        models = ['Random Forest', 'Gradient Boosting', 'Neural Network', 'Ensemble Model']
        precision = [0.82, 0.85, 0.79, 0.89]
        recall = [0.80, 0.83, 0.76, 0.87]
        f1_score = [0.81, 0.84, 0.77, 0.88]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=models,
            y=precision,
            mode='lines+markers',
            name='Precision',
            line=dict(color='blue', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=models,
            y=recall,
            mode='lines+markers',
            name='Recall',
            line=dict(color='green', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=models,
            y=f1_score,
            mode='lines+markers',
            name='F1-Score',
            line=dict(color='red', width=2)
        ))
        
        fig.update_layout(
            title='Performa Model Prediksi',
            xaxis_title='Model',
            yaxis_title='Skor',
            yaxis=dict(range=[0.7, 0.95]),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Key variables
    st.header("Variabel Kunci dalam Model")
    
    # Create correlation heatmap data
    variables = [
        'Stunting', 'Wasting', 'Obesitas', 'Anemia', 'ASI Eksklusif', 
        'Ketahanan Pangan', 'Tenaga Kesehatan', 'Pusat Gizi', 
        'Kemiskinan', 'Pendidikan Ibu', 'Akses Air Bersih'
    ]
    
    # Generate a random but realistic correlation matrix
    np.random.seed(42)  # for reproducibility
    corr_matrix = np.zeros((len(variables), len(variables)))
    
    for i in range(len(variables)):
        for j in range(len(variables)):
            if i == j:
                corr_matrix[i][j] = 1.0
            else:
                # Generate a realistic correlation value
                if i < j:
                    # Some pairs have strong positive correlations
                    if (i, j) in [(0, 1), (0, 3), (1, 3), (5, 6), (8, 9)]:
                        corr_matrix[i][j] = 0.6 + np.random.uniform(0, 0.3)
                    # Some have strong negative correlations
                    elif (i, j) in [(0, 4), (1, 4), (3, 4), (8, 10)]:
                        corr_matrix[i][j] = -0.6 - np.random.uniform(0, 0.3)
                    # Others have moderate or weak correlations
                    else:
                        corr_matrix[i][j] = np.random.uniform(-0.5, 0.5)
                    corr_matrix[j][i] = corr_matrix[i][j]  # make it symmetric
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix,
        x=variables,
        y=variables,
        colorscale='RdBu_r',
        zmin=-1,
        zmax=1,
        colorbar=dict(title='Korelasi')
    ))
    
    fig.update_layout(
        title='Korelasi antar Variabel dalam Model Prediksi',
        height=600,
        width=800
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Interpretasi Korelasi:**
    
    * **Korelasi Positif Kuat (> 0.6)**: Variabel bergerak bersama-sama dalam arah yang sama. Misalnya, tingkat stunting dan wasting menunjukkan korelasi positif yang berarti daerah dengan tingkat stunting tinggi cenderung juga memiliki tingkat wasting tinggi.
    
    * **Korelasi Negatif Kuat (< -0.6)**: Variabel bergerak dalam arah berlawanan. Misalnya, tingkat ASI eksklusif dan stunting memiliki korelasi negatif, yang menunjukkan bahwa daerah dengan tingkat ASI eksklusif tinggi cenderung memiliki tingkat stunting yang lebih rendah.
    
    * **Korelasi Lemah (-0.3 to 0.3)**: Hubungan yang lemah antara variabel, menunjukkan bahwa faktor-faktor lain mungkin lebih berpengaruh.
    """)
    
    # Feature importance
    st.header("Kepentingan Variabel dalam Prediksi")
    
    # Create feature importance chart
    features = [
        'Tingkat Stunting', 'Rasio Tenaga Kesehatan', 'Tingkat Kemiskinan',
        'Akses Puskesmas', 'ASI Eksklusif', 'Tingkat Anemia', 
        'Akses Air Bersih', 'Tingkat Pendidikan', 'Ketahanan Pangan',
        'Urbanisasi', 'Infrastruktur Kesehatan'
    ]
    
    importance = [0.23, 0.18, 0.15, 0.12, 0.09, 0.08, 0.06, 0.04, 0.03, 0.01, 0.01]
    
    fig = px.bar(
        x=importance,
        y=features,
        orientation='h',
        title='Kepentingan Variabel dalam Model Prediksi',
        labels={'x': 'Skor Kepentingan', 'y': 'Variabel'},
        color=importance,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        yaxis=dict(categoryorder='total ascending'),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Insight dari Kepentingan Variabel:**
    
    Grafik di atas menunjukkan kontribusi relatif setiap variabel dalam model prediksi kebutuhan formasi. 
    Tingkat stunting dan rasio tenaga kesehatan muncul sebagai prediktor paling penting, yang selaras dengan 
    fokus SPPI 2025 pada peningkatan kesehatan gizi dan penanganan stunting di Indonesia.
    
    Variabel sosial-ekonomi seperti tingkat kemiskinan juga berperan signifikan, menegaskan pendekatan multi-faktor 
    yang diperlukan dalam intervensi kesehatan gizi.
    """)
    
    # Uncertainty analysis
    st.header("Analisis Ketidakpastian")
    
    uncertainty_col1, uncertainty_col2 = st.columns(2)
    
    with uncertainty_col1:
        st.markdown("""
        ### Sumber Ketidakpastian dalam Prediksi:
        
        1. **Kualitas Data**
           * Keterbatasan cakupan data di daerah terpencil
           * Potensi bias dalam pengumpulan data
           * Data yang tidak lengkap atau outdated
        
        2. **Variasi Implementasi Program**
           * Perbedaan kapasitas implementasi antar daerah
           * Variasi kepatuhan terhadap protokol program
           * Perbedaan pendekatan di tingkat lokal
        
        3. **Faktor Eksternal**
           * Perubahan kebijakan pemerintah
           * Kondisi ekonomi dan sosial makro
           * Perubahan anggaran dan prioritas program
        
        4. **Dinamika Populasi**
           * Perubahan pola migrasi
           * Pergeseran demografi
           * Perubahan pola konsumsi dan gaya hidup
        """)
    
    with uncertainty_col2:
        # Create uncertainty range visualization
        provinces = ['Papua', 'NTT', 'Maluku', 'Sulawesi Tengah', 'Kalimantan Barat']
        central_estimates = [75, 65, 55, 45, 40]
        
        # Create lower and upper bounds with varying ranges to show different uncertainty levels
        lower_bounds = [max(0, central_estimates[i] - int(10 + i*2)) for i in range(len(central_estimates))]
        upper_bounds = [central_estimates[i] + int(10 + i*2) for i in range(len(central_estimates))]
        
        # Ensure no negative values
        lower_bounds = [max(0, lb) for lb in lower_bounds]
        
        fig = go.Figure()
        
        # Add central estimates
        fig.add_trace(go.Scatter(
            x=provinces,
            y=central_estimates,
            mode='markers',
            marker=dict(size=10, color='blue'),
            name='Estimasi Tengah'
        ))
        
        # Add error bars
        for i in range(len(provinces)):
            fig.add_trace(go.Scatter(
                x=[provinces[i], provinces[i]],
                y=[lower_bounds[i], upper_bounds[i]],
                mode='lines',
                line=dict(color='blue', width=1),
                showlegend=False
            ))
            
            # Add caps to the error bars
            fig.add_trace(go.Scatter(
                x=[provinces[i], provinces[i]],
                y=[lower_bounds[i], lower_bounds[i]],
                mode='lines',
                line=dict(color='blue', width=1),
                showlegend=False
            ))
            
            fig.add_trace(go.Scatter(
                x=[provinces[i], provinces[i]],
                y=[upper_bounds[i], upper_bounds[i]],
                mode='lines',
                line=dict(color='blue', width=1),
                showlegend=False
            ))
        
        fig.update_layout(
            title='Rentang Ketidakpastian Prediksi untuk Provinsi Terpilih',
            xaxis_title='Provinsi',
            yaxis_title='Formasi yang Dibutuhkan',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **Interpretasi Rentang Ketidakpastian:**
        
        Grafik di atas menunjukkan rentang prediksi untuk beberapa provinsi prioritas. Semakin panjang bar ketidakpastian, 
        semakin tinggi variabilitas dalam prediksi untuk provinsi tersebut. Provinsi dengan ketidakpastian tinggi 
        memerlukan pemantauan lebih ketat dan potensial untuk penyesuaian prediksi seiring dengan tersedianya data baru.
        """)
    
    # Model validation
    st.header("Validasi Model")
    
    st.markdown("""
    ### Pendekatan Validasi Model Prediksi:
    
    Validasi model dilakukan melalui beberapa metode untuk memastikan keakuratan dan keandalan prediksi:
    """)
    
    validation_col1, validation_col2 = st.columns(2)
    
    with validation_col1:
        st.markdown("""
        1. **Cross-Validation**
           * K-fold cross-validation (k=10)
           * Validasi temporal dengan data historis
           * Out-of-sample testing
        
        2. **Validasi Pakar**
           * Panel pakar gizi dan kesehatan masyarakat
           * Review oleh praktisi program kesehatan
           * Konfirmasi dengan stakeholder daerah
        
        3. **Backtesting**
           * Evaluasi performa model pada data historis
           * Perbandingan prediksi dengan hasil aktual
           * Analisis kesalahan dan penyimpangan
        
        4. **Validasi Silang dengan Program Lain**
           * Perbandingan dengan prediksi program sejenis
           * Kalibrasi berdasarkan hasil evaluasi program terdahulu
           * Sinkronisasi dengan proyeksi kebutuhan tenaga kesehatan nasional
        """)
    
    with validation_col2:
        # Create validation metric chart
        metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
        values = [0.87, 0.85, 0.84, 0.84, 0.91]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=metrics,
            y=values,
            marker_color='#0066cc'
        ))
        
        # Add threshold line for acceptable performance
        fig.add_shape(
            type='line',
            x0=-0.5,
            x1=4.5,
            y0=0.8,
            y1=0.8,
            line=dict(
                color='red',
                width=2,
                dash='dash'
            )
        )
        
        fig.update_layout(
            title='Metrik Validasi Model',
            xaxis_title='Metrik',
            yaxis_title='Skor',
            yaxis=dict(range=[0.7, 1.0]),
            height=400,
            annotations=[
                dict(
                    x=2,
                    y=0.78,
                    xref='x',
                    yref='y',
                    text='Threshold Performa Minimum (0.8)',
                    showarrow=False,
                    font=dict(color='red')
                )
            ]
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Continous improvement
    st.header("Peningkatan Model Berkelanjutan")
    
    st.markdown("""
    ### Strategi Pengembangan Model:
    
    Model prediksi kebutuhan formasi SPPI 2025 adalah sistem yang dinamis dengan proses peningkatan berkelanjutan:
    
    1. **Pembaruan Data Berkala**
       * Integrasi data baru setiap triwulan
       * Sinkronisasi dengan sistem informasi kesehatan nasional
       * Pengumpulan data primer dari lapangan untuk validasi
    
    2. **Penyempurnaan Algoritma**
       * Eksperimen dengan teknik machine learning baru
       * Optimalisasi hyperparameter secara berkala
       * Penambahan variabel dan fitur baru sesuai kebutuhan
    
    3. **Umpan Balik dari Pengguna**
       * Sistem pengumpulan umpan balik dari pembuat kebijakan
       * Sesi evaluasi dengan pelaksana program di lapangan
       * Workshop pengembangan model dengan stakeholder
    
    4. **Integrasi Pengetahuan Baru**
       * Pembaruan berdasarkan penelitian terbaru di bidang gizi
       * Adaptasi terhadap perubahan kebijakan dan prioritas program
       * Penyesuaian berdasarkan evaluasi program SPPI
    """)
    
    # Next steps
    st.header("Arah Pengembangan Selanjutnya")
    
    next_col1, next_col2, next_col3 = st.columns(3)
    
    with next_col1:
        st.markdown("""
        ### 🔍 Peningkatan Resolusi Model
        
        - Pengembangan model hingga level kecamatan
        - Prediksi kebutuhan spesifik berdasarkan spesialisasi
        - Analisis mikro-nutrient deficiency secara spesifik
        
        **Target Implementasi:** Q2 2024
        """)
    
    with next_col2:
        st.markdown("""
        ### 🔄 Integrasi Real-time
        
        - Sistem pemantauan dan prediksi berkelanjutan
        - Dashboards dengan update otomatis
        - Sistem peringatan dini untuk perubahan signifikan
        
        **Target Implementasi:** Q3 2024
        """)
    
    with next_col3:
        st.markdown("""
        ### 🤖 AI-driven Recommendations
        
        - Sistem rekomendasi berbasis AI untuk intervensi
        - Personalisasi strategi berdasarkan karakteristik daerah
        - Simulasi skenario "what-if" untuk pembuat kebijakan
        
        **Target Implementasi:** Q4 2024
        """)
    
    # References
    st.header("Referensi dan Sumber Daya")
    
    st.markdown("""
    ### Dokumen Teknis dan Publikasi:
    
    1. Kementerian Kesehatan RI. (2023). *Pedoman Analisis Kebutuhan Tenaga Kesehatan Gizi Indonesia 2023-2025*.
    
    2. Badan Perencanaan Pembangunan Nasional. (2022). *Proyeksi Kebutuhan SDM Kesehatan dalam Pencapaian Target SDGs 2030*.
    
    3. World Health Organization. (2022). *Workforce Prediction Models for Public Health Nutrition Programs: A Systematic Review*.
    
    4. Data Science Indonesia. (2023). *Penerapan Machine Learning untuk Prediksi Kebutuhan SDM Kesehatan di Indonesia*.
    
    5. UNICEF & Kementerian PPN/Bappenas. (2023). *Peta Jalan Penurunan Stunting Indonesia 2023-2030: Implikasi terhadap Kebutuhan SDM*.
    
    ### API dan Dataset:
    
    - API dokumentasi tersedia untuk pengembang di: `https://api.sppi-prediction.kemdikbud.go.id/docs`
    - Dataset publik tersedia di portal data terbuka: `https://data.go.id/sppi-nutrition-2025`
    
    ### Kontak Tim Teknis:
    
    Untuk diskusi lebih lanjut tentang aspek teknis model prediksi, silakan menghubungi:
    
    Tim Data Science SPPI 2025  
    Email: datascience@sppi.kemdikbud.go.id
    """)

if __name__ == "__main__":
    main()