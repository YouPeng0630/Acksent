import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from collections import Counter
import re
import pandas as pd

def create_dashboard_figure():
    log_files = [
        'example_data/logs/log_Atharv.txt',
        'example_data/logs/log_Tina.txt',
        'example_data/logs/log_Jigyashu.txt',
        'example_data/logs/log_Manali.txt',
        'example_data/logs/log_Nicholas.txt',
        'example_data/logs/log_Nikhil.txt',
        'example_data/logs/log_Pengfei.txt',
        'example_data/logs/log_Shariq.txt',
        'example_data/logs/log_Haley.txt',
        'example_data/logs/log_Sophie.txt',
        'example_data/logs/log_Satyam.txt',
        'example_data/logs/log_Manika.txt'
    ]

    date_pattern = r'\d{4}-\d{2}-\d{2}'
    upload_pattern = re.compile(r'upload the coding result of \d+ at \d{4}-\d{2}-\d{2}')

    dates = []

    for log_file in log_files:
        with open(log_file, 'r') as file:
            for line in file:
                if upload_pattern.search(line):
                    match = re.search(date_pattern, line)
                    if match:
                        dates.append(match.group(0))

    date_counts = Counter(dates)

    df = pd.DataFrame(list(date_counts.items()), columns=['Date', 'Count'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    start_date = df['Date'].min()
    end_date = df['Date'].max()
    all_dates = pd.date_range(start=start_date, end=end_date, freq='D')

    df_all_dates = pd.DataFrame(all_dates, columns=['Date'])
    df = pd.merge(df_all_dates, df, on='Date', how='left')
    df['Count'] = df['Count'].fillna(0).astype(int)

    if len(df) > 1:
        last_day_count = df.iloc[-2]['Count']
        previous_day_count = df.iloc[-3]['Count']
        difference = last_day_count - previous_day_count
        yesterday = df.iloc[-2]['Count']
    else:
        difference = 0
    
    return df, difference, yesterday

def find_indiv(name):
    log_file = f'log/log_{name}.txt'
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    upload_pattern = re.compile(r'upload the coding result of \d+ at \d{4}-\d{2}-\d{2}')

    dates = []

    with open(log_file, 'r') as file:
        for line in file:
            if upload_pattern.search(line):
                match = re.search(date_pattern, line)
                if match:
                    dates.append(match.group(0))

    date_counts = Counter(dates)

    df = pd.DataFrame(list(date_counts.items()), columns=['Date', 'Count'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    start_date = df['Date'].min()
    end_date = df['Date'].max()
    all_dates = pd.date_range(start=start_date, end=end_date, freq='D')

    df_all_dates = pd.DataFrame(all_dates, columns=['Date'])
    df = pd.merge(df_all_dates, df, on='Date', how='left')
    df['Count'] = df['Count'].fillna(0).astype(int)
    
    return df

def create_combined_plot(selected_user):
    df_team, difference, yesterday = create_dashboard_figure()
    df_individual = find_indiv(selected_user)
    
    # Create a combined plot
    fig = go.Figure()

    # Add team data
    fig.add_trace(go.Scatter(
        x=df_team['Date'], y=df_team['Count'],
        mode='lines+markers',
        marker=dict(size=8, color='rgb(31, 119, 180)'),
        line=dict(width=2, color='rgb(31, 119, 180)'),
        name='Team',
        text=df_team['Count'],
        textposition='top center'
    ))

    # Add individual data
    fig.add_trace(go.Scatter(
        x=df_individual['Date'], y=df_individual['Count'],
        mode='lines+markers',
        marker=dict(size=8, color='rgb(255, 99, 71)'),
        line=dict(width=2, color='rgb(255, 99, 71)'),
        name=selected_user,
        text=df_individual['Count'],
        textposition='top center'
    ))

    # Update layout
    fig.update_layout(
        title=f'Daily Upload Counts (Team vs {selected_user})',
        xaxis_title='Date',
        yaxis_title='Number of Uploads',
        plot_bgcolor='#f9f9f9',
        hovermode='x unified',
        font=dict(family='Arial, sans-serif', size=12, color='#000'),
        title_font=dict(size=20, color='rgb(31, 119, 180)', family='Arial, sans-serif'),
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
        yaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
    )

    fig.update_xaxes(tickformat='%Y-%m-%d', tickangle=45)

    annotations = []
    for i in range(len(df_team)):
        annotations.append(dict(x=df_team['Date'][i], y=df_team['Count'][i],
                                text=f'{df_team["Count"][i]}',
                                xanchor='center', yanchor='bottom',
                                showarrow=False, font=dict(size=12, color='rgb(31, 119, 180)')))
    for i in range(len(df_individual)):
        annotations.append(dict(x=df_individual['Date'][i], y=df_individual['Count'][i],
                                text=f'{df_individual["Count"][i]}',
                                xanchor='center', yanchor='bottom',
                                showarrow=False, font=dict(size=12, color='rgb(255, 99, 71)')))

    fig.update_layout(annotations=annotations)

    return fig



def create_combined_plot1(input_number):
    df_team, difference, yesterday = create_dashboard_figure()
    
    # 创建一个新的 DataFrame 来表示修改后的数据
    df_modified = df_team.copy()
    df_modified['Count'] = 0
    df_modified.at[df_team.index[-1], 'Count'] = input_number
    
    # 创建合并后的图表
    fig = go.Figure()

    # 添加团队数据
    fig.add_trace(go.Scatter(
        x=df_team['Date'], y=df_team['Count'],
        mode='lines+markers',
        marker=dict(size=8, color='rgb(31, 119, 180)'),
        line=dict(width=2, color='rgb(31, 119, 180)'),
        name='Team',
        text=df_team['Count'],
        textposition='top center'
    ))

    # 添加修改后的数据
    fig.add_trace(go.Scatter(
        x=df_modified['Date'], y=df_modified['Count'],
        mode='lines+markers',
        marker=dict(size=8, color='rgb(255, 99, 71)'),
        line=dict(width=2, color='rgb(255, 99, 71)'),
        name='Modified Data',
        text=df_modified['Count'],
        textposition='top center'
    ))

    # 更新布局
    fig.update_layout(
        title='Daily Upload Counts (Team vs Modified Data)',
        xaxis_title='Date',
        yaxis_title='Number of Uploads',
        plot_bgcolor='#f9f9f9',
        hovermode='x unified',
        font=dict(family='Arial, sans-serif', size=12, color='#000'),
        title_font=dict(size=20, color='rgb(31, 119, 180)', family='Arial, sans-serif'),
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
        yaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
    )

    fig.update_xaxes(tickformat='%Y-%m-%d', tickangle=45)

    # 添加注释
    annotations = []
    for i in range(len(df_team)):
        annotations.append(dict(x=df_team['Date'][i], y=df_team['Count'][i],
                                text=f'{df_team["Count"][i]}',
                                xanchor='center', yanchor='bottom',
                                showarrow=False, font=dict(size=12, color='rgb(31, 119, 180)')))
    for i in range(len(df_modified)):
        annotations.append(dict(x=df_modified['Date'][i], y=df_modified['Count'][i],
                                text=f'{df_modified["Count"][i]}',
                                xanchor='center', yanchor='bottom',
                                showarrow=False, font=dict(size=12, color='rgb(255, 99, 71)')))

    fig.update_layout(annotations=annotations)

    return fig
fig = create_combined_plot1(1)
st.write(fig)