import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os

def count_y_in_progress(file_path):
    try:
        df = pd.read_csv(file_path)
        return df['Progress'].value_counts().get('Y', 0)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0
    except pd.errors.EmptyDataError:
        print(f"Empty data file: {file_path}")
        return 0
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return 0

def generate_progress_chart():
    record_dir = 'example_data/record'

    if not os.path.exists(record_dir):
        raise ValueError(f"The directory {record_dir} does not exist.")

    record_file_paths = {filename: os.path.join(record_dir, filename) 
                         for filename in os.listdir(record_dir) 
                         if filename.endswith('.csv')}

    progress_counts = {}
    for name, file_path in record_file_paths.items():
        count = count_y_in_progress(file_path)
        progress_counts[name] = count

    groups = {
        'Group 1': [int(progress_counts.get('record_Sophie.csv', 0)), int(progress_counts.get('record_Manika.csv', 0))],
        'Group 2': [int(progress_counts.get('record_Jigyashu.csv', 0)), int(progress_counts.get('record_Nikhil.csv', 0))],
        'Group 3': [int(progress_counts.get('record_Manali.csv', 0)), int(progress_counts.get('record_Satyam.csv', 0))],
        'Group 4': [int(progress_counts.get('record_Amreentaj.csv', 0)), int(progress_counts.get('record_Haley.csv', 0))],
        'Group 5': [int(progress_counts.get('record_Nicholas.csv', 0)), int(progress_counts.get('record_Atharv.csv', 0))],
        'Group 6': [int(progress_counts.get('record_Tina.csv', 0)), int(progress_counts.get('record_Shariq.csv', 0))]
    }

    labels = list(groups.keys())
    data1 = [-values[0] for values in groups.values()] 
    data2 = [values[1] for values in groups.values()]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=labels,
        x=data1,
        name='First Member',
        orientation='h',
        marker=dict(color='skyblue'),
        text=None  
    ))

    fig.add_trace(go.Bar(
        y=labels,
        x=data2,
        name='Second Member',
        orientation='h',
        marker=dict(color='salmon'),
        text=None  
    ))

    fig.update_layout(
        barmode='relative',
        title='Number Relations in Each Group',
        xaxis_title='',
        yaxis_title='Groups',
        template='plotly_white',
        xaxis=dict(showticklabels=False, showgrid=True, gridwidth=0.5, gridcolor='LightGrey', zeroline=True, zerolinewidth=1, zerolinecolor='Black'),
        width=1000,  
        margin=dict(l=20, r=30, t=40, b=20), 
        showlegend=False  
    )

    return fig

if __name__ == '__main__':
    fig = generate_progress_chart()
    st.plotly_chart(fig, config={'displayModeBar': False}) 
