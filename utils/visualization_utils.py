import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_utils import load_nutrition_data

def create_regional_nutrition_comparison(data, metric):
    """
    Create a bar chart comparing nutrition metrics across regions
    
    Parameters:
    - data: Pandas DataFrame with nutrition data
    - metric: string, the metric to display
    
    Returns:
    - Plotly figure
    """
    # Group by region and calculate mean
    regional_data = data.groupby('region')[metric].mean().reset_index()
    
    # Define color scheme based on metric
    if 'stunting' in metric or 'wasting' in metric or 'anemia' in metric:
        color_scale = px.colors.sequential.Reds
    elif 'obesity' in metric:
        color_scale = px.colors.sequential.Blues
    else:
        color_scale = px.colors.sequential.Greens
    
    # Create the bar chart
    fig = px.bar(
        regional_data, 
        x='region', 
        y=metric,
        color=metric,
        color_continuous_scale=color_scale,
        title=f'{metric.replace("_", " ").title()} by Region',
        labels={
            'region': 'Region',
            metric: metric.replace('_', ' ').title()
        }
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title='Region',
        yaxis_title=metric.replace('_', ' ').title(),
        height=500
    )
    
    return fig

def create_provincial_nutrition_map(data, metric):
    """
    Create a choropleth map of nutrition metrics by province
    
    Parameters:
    - data: Pandas DataFrame with nutrition data
    - metric: string, the metric to display
    
    Returns:
    - Plotly figure
    """
    # Note: In a real application, this would use GeoJSON data for Indonesia's provinces
    # For this example, we'll create a simplified scatter map
    
    # Create scatter map (since we don't have actual GeoJSON)
    fig = px.scatter_geo(
        data,
        lat=data['province'].apply(lambda x: -6 + (hash(x) % 10) / 10),  # Simulate coordinates
        lon=data['province'].apply(lambda x: 107 + (hash(x[::-1]) % 25) / 10),
        color=metric,
        hover_name='province',
        size=data[metric],
        size_max=25,
        title=f'{metric.replace("_", " ").title()} by Province',
        color_continuous_scale=px.colors.sequential.Viridis
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
    
    return fig

def create_nutrition_indicators_radar(data):
    """
    Create a radar chart of nutrition indicators for selected provinces
    
    Parameters:
    - data: Pandas DataFrame with nutrition data
    
    Returns:
    - Plotly figure
    """
    # Select a few provinces to compare
    selected_provinces = ["DKI Jakarta", "Papua", "Jawa Barat", "Nusa Tenggara Timur", "Sulawesi Selatan"]
    
    # Metrics to include in radar chart
    metrics = ['stunting_percentage', 'wasting_percentage', 'obesity_percentage', 
              'anemia_percentage', 'exclusive_breastfeeding', 'food_security_score']
    
    # Filter data
    filtered_data = data[data['province'].isin(selected_provinces)]
    
    # Create radar chart
    fig = go.Figure()
    
    for province in selected_provinces:
        province_data = filtered_data[filtered_data['province'] == province]
        if not province_data.empty:
            fig.add_trace(go.Scatterpolar(
                r=province_data[metrics].values.flatten().tolist(),
                theta=[m.replace('_', ' ').title() for m in metrics],
                fill='toself',
                name=province
            ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Nutrition Indicators Comparison by Province",
        height=600
    )
    
    return fig

def create_priority_level_distribution(data):
    """
    Create a pie chart showing the distribution of priority levels
    
    Parameters:
    - data: Pandas DataFrame with nutrition data
    
    Returns:
    - Plotly figure
    """
    # Count provinces by priority level
    priority_counts = data['priority_level'].value_counts().reset_index()
    priority_counts.columns = ['Priority Level', 'Count']
    
    # Create pie chart
    fig = px.pie(
        priority_counts, 
        values='Count', 
        names='Priority Level',
        title='Distribution of Provinces by Nutrition Priority Level',
        color_discrete_sequence=px.colors.sequential.RdBu,
        hole=0.4
    )
    
    # Update layout
    fig.update_layout(
        height=500,
        annotations=[dict(text='Priority<br>Levels', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    
    return fig

def create_correlation_heatmap(data):
    """
    Create a heatmap showing correlations between different nutrition metrics
    
    Parameters:
    - data: Pandas DataFrame with nutrition data
    
    Returns:
    - Matplotlib figure
    """
    # Select numeric columns for correlation
    numeric_cols = ['stunting_percentage', 'wasting_percentage', 'obesity_percentage', 
                    'anemia_percentage', 'exclusive_breastfeeding', 'food_security_score',
                    'nutrition_centers', 'health_workers_per_1000', 'priority_level']
    
    # Calculate correlation matrix
    corr_matrix = data[numeric_cols].corr()
    
    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create heatmap
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        cmap='coolwarm', 
        vmin=-1, 
        vmax=1, 
        center=0,
        linewidths=0.5,
        ax=ax
    )
    
    # Set title
    ax.set_title('Correlation Between Nutrition Indicators', fontsize=14)
    
    return fig

def create_specialization_distribution(data):
    """
    Create a horizontal bar chart showing the distribution of positions by specialization
    
    Parameters:
    - data: Pandas DataFrame with placement opportunities
    
    Returns:
    - Plotly figure
    """
    # Group by specialization and sum positions available
    spec_distribution = data.groupby('specialization')['positions_available'].sum().reset_index()
    spec_distribution = spec_distribution.sort_values('positions_available', ascending=True)
    
    # Create horizontal bar chart
    fig = px.bar(
        spec_distribution,
        y='specialization',
        x='positions_available',
        orientation='h',
        color='positions_available',
        color_continuous_scale=px.colors.sequential.Viridis,
        title='Distribution of Available Positions by Specialization',
        labels={
            'specialization': 'Specialization',
            'positions_available': 'Number of Positions'
        }
    )
    
    # Update layout
    fig.update_layout(
        yaxis_title='',
        xaxis_title='Number of Positions',
        height=500
    )
    
    return fig

def create_collaboration_types_chart(data):
    """
    Create a bar chart showing the distribution of private sector collaboration types
    
    Parameters:
    - data: Pandas DataFrame with collaboration opportunities
    
    Returns:
    - Plotly figure
    """
    # Count collaboration types
    collab_counts = data['collaboration_type'].value_counts().reset_index()
    collab_counts.columns = ['Collaboration Type', 'Count']
    
    # Create bar chart
    fig = px.bar(
        collab_counts,
        x='Collaboration Type',
        y='Count',
        color='Count',
        color_continuous_scale=px.colors.sequential.Plasma,
        title='Types of Private Sector Collaboration Opportunities',
        labels={
            'Collaboration Type': 'Type of Collaboration',
            'Count': 'Number of Opportunities'
        }
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title='',
        yaxis_title='Number of Opportunities',
        height=500,
        xaxis={'categoryorder':'total descending'}
    )
    
    # Update x-axis to have rotated labels
    fig.update_xaxes(tickangle=45)
    
    return fig
