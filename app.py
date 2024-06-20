import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.io as pio

# Title of the web app
st.title('Identity Constellation Generator')

# Input values
race = st.selectbox('Select Race', list(range(1, 8))) # race
gender = st.selectbox('Select Gender', list(range(1, 8))) # gender
age = st.selectbox('Enter Age', list(range(1, 8))) # age
nationality = st.selectbox('Select Nationality', list(range(1, 8))) # nationality
education = st.selectbox('Select Education Level', list(range(1, 8))) # education

# Add a submit button
if st.button('Submit'):
    # Define color mappings for each category
    color_mappings = {
        "Race": ["#FFCC80", "#FFB74D", "#FFA726", "#FF9800", "#FB8C00", "#F57C00", "#E65100"],
        "Gender": ["#BBDEFB", "#64B5F6", "#2196F3", "#1976D2", "#1565C0", "#0D47A1", "#0D47A1"],
        "Age": ["#C8E6C9", "#A5D6A7", "#81C784", "#66BB6A", "#4CAF50", "#43A047", "#388E3C"],
        "Nationality": ["#FFCDD2", "#EF9A9A", "#E57373", "#EF5350", "#F44336", "#E53935", "#D32F2F"],
        "Education": ["#E1BEE7", "#CE93D8", "#BA68C8", "#AB47BC", "#9C27B0", "#8E24AA", "#7B1FA2"],
    }

    # Normalize ratings
    max_rating = 7
    dimensions = [
        {"name": "Race", "color": "orange", "rating": race, "x": 1, "y": 5, "normalized_rating": race / max_rating},
        {"name": "Gender", "color": "blue", "rating": gender, "x": 2, "y": 7, "normalized_rating": gender / max_rating},
        {"name": "Age", "color": "green", "rating": age, "x": 3, "y": 3, "normalized_rating": age / max_rating},
        {"name": "Nationality", "color": "red", "rating": nationality, "x": 4, "y": 8, "normalized_rating": nationality / max_rating},
        {"name": "Education", "color": "purple", "rating": education, "x": 5, "y": 2, "normalized_rating": education / max_rating},
    ]

    # Create DataFrame for Plotly
    df = pd.DataFrame(dimensions)

    # Create scatter plot with lines for a constellation effect
    fig = go.Figure()

    # Add lines between points to create constellation effect
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            fig.add_trace(go.Scatter(
                x=[df.loc[i, 'x'], df.loc[j, 'x']],
                y=[df.loc[i, 'y'], df.loc[j, 'y']],
                mode='lines',
                line=dict(color='white', width=1),
                hoverinfo='none',
                showlegend=False
            ))

    # Add scatter points with color intensities based on user input
    for i, row in df.iterrows():
        fig.add_trace(go.Scatter(
            x=[row['x']],
            y=[row['y']],
            mode='markers+text',
            marker=dict(
                size=20,  # Constant size
                color=color_mappings[row['name']][int(row['rating']) - 1],
                opacity=1  # Constant opacity
            ),
            text=row['name'],
            textposition='top center',
            hoverinfo="text"
        ))

    # Customize layout to look like a celestial map
    fig.update_layout(
        title="Identity Constellation",
        plot_bgcolor='white',  # Background color
        paper_bgcolor='white',  # Paper color
        font=dict(color='black'),  # Font color
        title_font=dict(size=24, color='black', family="Arial"),  # Title font color and size
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        showlegend=False
    )

    # Draw the connecting lines between the points
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            fig.add_trace(go.Scatter(
                x=[df.loc[i, 'x'], df.loc[j, 'x']],
                y=[df.loc[i, 'y'], df.loc[j, 'y']],
                mode='lines',
                line=dict(color='black', width=1),
                hoverinfo='none',
                showlegend=False
            ))

    # Save the graph as an image
    file_path = "identity_constellation.png"
    fig.write_image(file_path)
    
    # Save the graph as an HTML file
    html_file_path = "identity_constellation.html"
    pio.write_html(fig, file=html_file_path, auto_open=True)