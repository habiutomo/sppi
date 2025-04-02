import pandas as pd
import numpy as np
import streamlit as st
import json
import os

# Cache for performance optimization
@st.cache_data
def load_program_info():
    """
    Load SPPI program information
    This would typically come from an API or database, but for this example,
    we'll create structured information about the program
    """
    program_info = {
        "program_name": "Sarjana Penggerak Pembangunan Indonesia (SPPI)",
        "year": 2025,
        "focus_area": "Kesehatan Gizi",
        "description": """
        Program Sarjana Penggerak Pembangunan Indonesia (SPPI) adalah inisiatif nasional 
        yang bertujuan untuk menempatkan lulusan sarjana di berbagai daerah Indonesia 
        untuk mendukung pembangunan. Pada tahun 2025, program ini akan memberikan 
        penekanan khusus pada bidang kesehatan gizi.
        """,
        "objectives": [
            "Meningkatkan status gizi masyarakat Indonesia",
            "Mengurangi prevalensi stunting pada anak-anak",
            "Meningkatkan kesadaran tentang pola makan sehat",
            "Memastikan akses ke makanan bergizi di daerah terpencil",
            "Memberdayakan masyarakat dalam praktik keamanan pangan"
        ],
        "estimated_positions": 3500,
        "nutrition_focus_positions": 750,
        "application_period": "Januari - Maret 2025",
        "program_duration": "1 tahun (dapat diperpanjang)"
    }
    
    return program_info

@st.cache_data
def load_nutrition_data():
    """
    Load nutrition data by region
    This function simulates nutrition data that would typically come from a real database
    """
    # Create province list (all Indonesia provinces)
    provinces = [
        "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Jambi", "Sumatera Selatan",
        "Bengkulu", "Lampung", "Kepulauan Bangka Belitung", "Kepulauan Riau", "DKI Jakarta",
        "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Jawa Timur", "Banten", "Bali",
        "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah",
        "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Utara",
        "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", "Gorontalo",
        "Sulawesi Barat", "Maluku", "Maluku Utara", "Papua Barat", "Papua"
    ]
    
    # In a real application, these would be real values from research/databases
    # Simulating data for educational purposes
    data = {
        "province": provinces,
        "stunting_percentage": np.random.uniform(15, 35, len(provinces)),
        "wasting_percentage": np.random.uniform(5, 15, len(provinces)),
        "obesity_percentage": np.random.uniform(3, 25, len(provinces)),
        "anemia_percentage": np.random.uniform(10, 40, len(provinces)),
        "exclusive_breastfeeding": np.random.uniform(30, 70, len(provinces)),
        "food_security_score": np.random.uniform(50, 90, len(provinces)),
        "nutrition_centers": np.random.randint(5, 100, len(provinces)),
        "health_workers_per_1000": np.random.uniform(0.5, 5.0, len(provinces)),
        "priority_level": np.random.randint(1, 6, len(provinces))
    }
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Add regional grouping
    western_indonesia = [
        "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Jambi", "Sumatera Selatan",
        "Bengkulu", "Lampung", "Kepulauan Bangka Belitung", "Kepulauan Riau", "DKI Jakarta",
        "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Jawa Timur", "Banten", "Bali"
    ]
    
    central_indonesia = [
        "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah",
        "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Utara",
        "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", "Gorontalo",
        "Sulawesi Barat"
    ]
    
    eastern_indonesia = ["Maluku", "Maluku Utara", "Papua Barat", "Papua"]
    
    def get_region(province):
        if province in western_indonesia:
            return "Indonesia Barat"
        elif province in central_indonesia:
            return "Indonesia Tengah"
        else:
            return "Indonesia Timur"
    
    df["region"] = df["province"].apply(get_region)
    
    return df

@st.cache_data
def load_placement_opportunities():
    """
    Load SPPI placement opportunities
    """
    # Creating a representative dataset based on regions in Indonesia
    provinces = [
        "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Jambi", "Sumatera Selatan",
        "Bengkulu", "Lampung", "Kepulauan Bangka Belitung", "Kepulauan Riau", "DKI Jakarta",
        "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Jawa Timur", "Banten", "Bali",
        "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah",
        "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara", "Sulawesi Utara",
        "Sulawesi Tengah", "Sulawesi Selatan", "Sulawesi Tenggara", "Gorontalo",
        "Sulawesi Barat", "Maluku", "Maluku Utara", "Papua Barat", "Papua"
    ]
    
    specializations = [
        "Nutritionist", "Community Health", "Food Science", "Maternal & Child Nutrition",
        "Public Health", "Dietetics", "Health Education", "Food Security"
    ]
    
    # Create empty list to hold all placement opportunities
    opportunities = []
    
    # Generate placement opportunities for each province
    for province in provinces:
        # Determine number of opportunities per province (more for high-need areas)
        if province in ["Papua", "Papua Barat", "Maluku", "Nusa Tenggara Timur", "Aceh"]:
            num_opportunities = np.random.randint(30, 50)
        elif province in ["DKI Jakarta", "Jawa Barat", "Jawa Timur", "Jawa Tengah"]:
            num_opportunities = np.random.randint(15, 30)
        else:
            num_opportunities = np.random.randint(10, 25)
            
        for i in range(num_opportunities):
            opportunities.append({
                "province": province,
                "district": f"District {i+1} {province}",
                "specialization": np.random.choice(specializations),
                "positions_available": np.random.randint(1, 5),
                "priority_level": np.random.randint(1, 6),  # 1-5 priority level (5 being highest)
                "remote_area": np.random.choice([True, False], p=[0.3, 0.7]),
                "housing_provided": np.random.choice([True, False], p=[0.7, 0.3]),
                "latitude": np.random.uniform(-10, 6) if province in ["Papua", "Maluku", "Sulawesi Selatan"] else np.random.uniform(-8, 5),
                "longitude": np.random.uniform(95, 140),
                "stipend_level": np.random.choice(["Basic", "Medium", "Enhanced"], p=[0.2, 0.6, 0.2])
            })
    
    # Convert to DataFrame
    df = pd.DataFrame(opportunities)
    
    return df

@st.cache_data
def load_private_sector_opportunities():
    """
    Load private sector collaboration opportunities
    """
    collaboration_types = [
        "Training & Development", "Nutritional Product Supply", "Research Partnership",
        "Technology Support", "Funding Program", "Community Outreach", 
        "Infrastructure Development", "Healthcare Service Provision"
    ]
    
    target_regions = [
        "Indonesia Barat", "Indonesia Tengah", "Indonesia Timur", "Nasional"
    ]
    
    # Create collaboration opportunities
    opportunities = []
    
    for i in range(20):
        opportunities.append({
            "id": i+1,
            "collaboration_type": np.random.choice(collaboration_types),
            "description": f"Program kerjasama {i+1} dengan sektor swasta",
            "target_region": np.random.choice(target_regions),
            "investment_level": np.random.choice(["Low", "Medium", "High"]),
            "duration_months": np.random.randint(6, 36),
            "benefits": np.random.randint(3, 8),
            "requirements": np.random.randint(2, 6)
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(opportunities)
    
    return df

@st.cache_data
def load_eligibility_criteria():
    """
    Load eligibility criteria and application resources for SPPI program
    """
    eligibility = {
        "general_requirements": [
            "Warga Negara Indonesia (WNI)",
            "Lulusan S1/D4 dari perguruan tinggi terakreditasi",
            "IPK minimal 3.00 dari skala 4.00",
            "Usia maksimal 27 tahun pada saat mendaftar",
            "Sehat jasmani dan rohani",
            "Tidak sedang menempuh pendidikan lain",
            "Bersedia ditempatkan di seluruh wilayah Indonesia"
        ],
        "nutrition_specialization_requirements": [
            "Gelar sarjana di bidang Gizi, Kesehatan Masyarakat, Kedokteran, atau bidang terkait",
            "Pengalaman kerja/magang di bidang kesehatan gizi menjadi nilai tambah",
            "Memiliki pengetahuan tentang isu kesehatan gizi di Indonesia",
            "Kemampuan komunikasi yang baik untuk edukasi masyarakat"
        ],
        "application_process": [
            "Pendaftaran online melalui portal SPPI",
            "Seleksi administrasi",
            "Tes potensi akademik dan bahasa",
            "Tes bidang kesehatan gizi",
            "Wawancara dan simulasi",
            "Pemeriksaan kesehatan",
            "Pengumuman hasil seleksi"
        ],
        "documents_required": [
            "Scan KTP asli",
            "Scan ijazah dan transkrip nilai",
            "Pas foto terbaru",
            "Surat keterangan sehat dari dokter",
            "Surat rekomendasi (opsional)",
            "Portofolio kegiatan terkait kesehatan/gizi (jika ada)"
        ],
        "timeline": {
            "registration_start": "Januari 2025",
            "registration_end": "Maret 2025",
            "selection_process": "April - Mei 2025",
            "announcement": "Juni 2025",
            "placement_start": "Agustus 2025"
        },
        "resources": [
            {
                "name": "Portal Resmi SPPI",
                "url": "https://sppi.kemdikbud.go.id",
                "description": "Situs resmi untuk informasi dan pendaftaran program SPPI"
            },
            {
                "name": "Panduan Persiapan Seleksi",
                "url": "https://sppi.kemdikbud.go.id/panduan",
                "description": "Materi dan tips untuk menghadapi proses seleksi"
            },
            {
                "name": "FAQ Program SPPI",
                "url": "https://sppi.kemdikbud.go.id/faq",
                "description": "Jawaban untuk pertanyaan yang sering diajukan"
            },
            {
                "name": "Grup Telegram Pendaftar SPPI",
                "url": "https://t.me/sppi2025",
                "description": "Komunitas untuk berbagi informasi antarPendaftar"
            }
        ]
    }
    
    return eligibility
