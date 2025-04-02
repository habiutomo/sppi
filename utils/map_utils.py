import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import numpy as np
from folium.plugins import MarkerCluster, HeatMap

def generate_indonesia_coordinates():
    """
    Generate approximate coordinates for Indonesian provinces for the map
    In a real application, these would be actual coordinates
    """
    provinces = {
        "Aceh": [4.695135, 96.749397],
        "Sumatera Utara": [2.1153547, 99.5450974],
        "Sumatera Barat": [-0.7399397, 100.8000051],
        "Riau": [0.2933469, 101.7068294],
        "Jambi": [-1.4851831, 102.4380581],
        "Sumatera Selatan": [-3.3194374, 103.914399],
        "Bengkulu": [-3.5778471, 102.3463875],
        "Lampung": [-4.5585849, 105.4068079],
        "Kepulauan Bangka Belitung": [-2.7410513, 106.4405872],
        "Kepulauan Riau": [3.9456514, 108.1428669],
        "DKI Jakarta": [-6.1744651, 106.822745],
        "Jawa Barat": [-6.8895721, 107.6400872],
        "Jawa Tengah": [-7.1562833, 110.1402594],
        "DI Yogyakarta": [-7.7955798, 110.3694896],
        "Jawa Timur": [-7.5360639, 112.2384017],
        "Banten": [-6.4058172, 106.0640179],
        "Bali": [-8.4095178, 115.188916],
        "Nusa Tenggara Barat": [-8.6529334, 117.3616476],
        "Nusa Tenggara Timur": [-8.6573819, 121.0793705],
        "Kalimantan Barat": [-0.2787808, 111.4752851],
        "Kalimantan Tengah": [-1.6814878, 113.3823545],
        "Kalimantan Selatan": [-3.0926415, 115.2837585],
        "Kalimantan Timur": [0.5386586, 116.419389],
        "Kalimantan Utara": [3.0730929, 116.0413889],
        "Sulawesi Utara": [0.6246932, 123.9750018],
        "Sulawesi Tengah": [-1.4300254, 121.4456179],
        "Sulawesi Selatan": [-3.6687994, 119.9740534],
        "Sulawesi Tenggara": [-4.14491, 122.174605],
        "Gorontalo": [0.6999372, 122.4467238],
        "Sulawesi Barat": [-2.8441371, 119.2320784],
        "Maluku": [-3.2384616, 130.1452734],
        "Maluku Utara": [1.5709993, 127.8087693],
        "Papua Barat": [-1.3361154, 133.1747162],
        "Papua": [-4.269928, 138.0803529]
    }
    
    return provinces

def create_placement_map(opportunities_df):
    """
    Create an interactive map showing SPPI placement opportunities across Indonesia
    
    Parameters:
    - opportunities_df: Pandas DataFrame with placement opportunities data
    
    Returns:
    - folium map object
    """
    # Create a base map centered on Indonesia
    m = folium.Map(location=[-2.5, 118], zoom_start=5, tiles="OpenStreetMap")
    
    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(m)
    
    # Generate province coordinates (in a real app, this would be more accurate data)
    province_coords = generate_indonesia_coordinates()
    
    # Add markers for each placement opportunity
    for province in opportunities_df['province'].unique():
        # Filter data for this province
        province_data = opportunities_df[opportunities_df['province'] == province]
        
        # Get coordinates (use actual coordinates if available, otherwise use province center)
        if province in province_coords:
            base_lat, base_lon = province_coords[province]
        else:
            # Default to center of Indonesia if province not found
            base_lat, base_lon = -2.5, 118
            
        for _, row in province_data.iterrows():
            # Add some randomness to avoid all markers being in the same spot
            lat_offset = np.random.uniform(-0.5, 0.5)
            lon_offset = np.random.uniform(-0.5, 0.5)
            
            lat = base_lat + lat_offset
            lon = base_lon + lon_offset
            
            # Create popup content
            popup_html = f"""
            <div style="min-width: 200px">
                <h4>{row['district']}, {row['province']}</h4>
                <b>Specialization:</b> {row['specialization']}<br>
                <b>Positions Available:</b> {row['positions_available']}<br>
                <b>Priority Level:</b> {row['priority_level']} (of 5)<br>
                <b>Remote Area:</b> {'Yes' if row['remote_area'] else 'No'}<br>
                <b>Housing Provided:</b> {'Yes' if row['housing_provided'] else 'No'}<br>
                <b>Stipend Level:</b> {row['stipend_level']}
            </div>
            """
            
            # Determine icon color based on priority level
            if row['priority_level'] >= 4:
                icon_color = 'red'
            elif row['priority_level'] >= 3:
                icon_color = 'orange'
            else:
                icon_color = 'blue'
                
            # Create marker with popup
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(folium.Html(popup_html, script=True), max_width=300),
                tooltip=f"{row['district']}, {row['province']} - {row['specialization']}",
                icon=folium.Icon(color=icon_color, icon='info-sign')
            ).add_to(marker_cluster)
    
    # Add a Layer Control panel
    folium.LayerControl().add_to(m)
    
    return m

def create_nutrition_heatmap(nutrition_data):
    """
    Create a heatmap showing nutrition priority areas across Indonesia
    
    Parameters:
    - nutrition_data: Pandas DataFrame with nutrition data by province
    
    Returns:
    - folium map object
    """
    # Create a base map centered on Indonesia
    m = folium.Map(location=[-2.5, 118], zoom_start=5, tiles="OpenStreetMap")
    
    # Generate province coordinates
    province_coords = generate_indonesia_coordinates()
    
    # Prepare data for heatmap
    heat_data = []
    
    for _, row in nutrition_data.iterrows():
        province = row['province']
        # Use stunting percentage as the weight for the heatmap
        weight = row['stunting_percentage']
        
        if province in province_coords:
            lat, lon = province_coords[province]
            # Add multiple points for higher weights to create a stronger heatmap effect
            intensity = int(weight / 5)  # Normalize the weight
            for _ in range(intensity):
                # Add some randomness to spread the points
                lat_offset = np.random.uniform(-0.3, 0.3)
                lon_offset = np.random.uniform(-0.3, 0.3)
                heat_data.append([lat + lat_offset, lon + lon_offset, weight / 100])
    
    # Add the heatmap layer
    HeatMap(heat_data, radius=15, blur=10, gradient={0.4: 'blue', 0.65: 'lime', 0.8: 'yellow', 1: 'red'}).add_to(m)
    
    # Add markers for each province with popup showing nutrition data
    for province, row in nutrition_data.set_index('province').iterrows():
        if province in province_coords:
            lat, lon = province_coords[province]
            
            # Create popup content
            popup_html = f"""
            <div style="min-width: 200px">
                <h4>{province}</h4>
                <b>Stunting:</b> {row['stunting_percentage']:.1f}%<br>
                <b>Wasting:</b> {row['wasting_percentage']:.1f}%<br>
                <b>Obesity:</b> {row['obesity_percentage']:.1f}%<br>
                <b>Anemia:</b> {row['anemia_percentage']:.1f}%<br>
                <b>Exclusive Breastfeeding:</b> {row['exclusive_breastfeeding']:.1f}%<br>
                <b>Food Security Score:</b> {row['food_security_score']:.1f}/100<br>
                <b>Priority Level:</b> {row['priority_level']} (of 5)
            </div>
            """
            
            # Create marker with popup
            folium.CircleMarker(
                location=[lat, lon],
                radius=8,
                popup=folium.Popup(folium.Html(popup_html, script=True), max_width=300),
                tooltip=province,
                color='black',
                fill=True,
                fill_color='white',
                fill_opacity=0.7
            ).add_to(m)
    
    return m

def display_map_with_filters(opportunities_df, key_prefix="placement"):
    """
    Display a map with various filters for SPPI placement opportunities
    
    Parameters:
    - opportunities_df: Pandas DataFrame with placement opportunities
    - key_prefix: String prefix for session state keys to avoid conflicts
    """
    st.subheader("Peta Peluang Penempatan SPPI 2025")
    
    # Sidebar for filters
    st.sidebar.header("Filter Peta")
    
    # Region/Province filter
    provinces = sorted(opportunities_df['province'].unique())
    selected_provinces = st.sidebar.multiselect(
        "Pilih Provinsi",
        options=provinces,
        default=[],
        key=f"{key_prefix}_province_filter"
    )
    
    # Specialization filter
    specializations = sorted(opportunities_df['specialization'].unique())
    selected_specializations = st.sidebar.multiselect(
        "Pilih Spesialisasi",
        options=specializations,
        default=[],
        key=f"{key_prefix}_spec_filter"
    )
    
    # Priority level filter
    min_priority = st.sidebar.slider(
        "Tingkat Prioritas Minimum",
        min_value=1,
        max_value=5,
        value=1,
        key=f"{key_prefix}_priority_filter"
    )
    
    # Remote area filter
    remote_filter = st.sidebar.radio(
        "Area Terpencil",
        options=["Semua", "Hanya Area Terpencil", "Kecuali Area Terpencil"],
        index=0,
        key=f"{key_prefix}_remote_filter"
    )
    
    # Housing filter
    housing_filter = st.sidebar.radio(
        "Akomodasi Disediakan",
        options=["Semua", "Ya", "Tidak"],
        index=0,
        key=f"{key_prefix}_housing_filter"
    )
    
    # Apply filters
    filtered_df = opportunities_df.copy()
    
    if selected_provinces:
        filtered_df = filtered_df[filtered_df['province'].isin(selected_provinces)]
        
    if selected_specializations:
        filtered_df = filtered_df[filtered_df['specialization'].isin(selected_specializations)]
        
    filtered_df = filtered_df[filtered_df['priority_level'] >= min_priority]
    
    if remote_filter == "Hanya Area Terpencil":
        filtered_df = filtered_df[filtered_df['remote_area'] == True]
    elif remote_filter == "Kecuali Area Terpencil":
        filtered_df = filtered_df[filtered_df['remote_area'] == False]
        
    if housing_filter == "Ya":
        filtered_df = filtered_df[filtered_df['housing_provided'] == True]
    elif housing_filter == "Tidak":
        filtered_df = filtered_df[filtered_df['housing_provided'] == False]
    
    # Display map
    if not filtered_df.empty:
        st.write(f"Menampilkan {len(filtered_df)} peluang penempatan berdasarkan filter yang dipilih")
        m = create_placement_map(filtered_df)
        folium_static(m)
    else:
        st.warning("Tidak ada peluang penempatan yang sesuai dengan filter yang dipilih")
        
    # Show stats about the filtered opportunities
    if not filtered_df.empty:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_positions = filtered_df['positions_available'].sum()
            st.metric("Total Posisi", f"{total_positions}")
            
        with col2:
            total_districts = filtered_df['district'].nunique()
            st.metric("Total Kabupaten/Kota", f"{total_districts}")
            
        with col3:
            avg_priority = filtered_df['priority_level'].mean()
            st.metric("Rata-rata Prioritas", f"{avg_priority:.1f}/5")
