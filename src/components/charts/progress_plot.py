import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from collections import Counter
import re
from PIL import Image

def create_dashboard_figure():
    # 日志文件路径列表
    log_files = [
        'example_data/logs/log_Amreentaj.txt',
        'example_data/logs/log_Tina.txt',
        'example_data/logs/log_Jigyashu.txt',
        'example_data/logs/log_Manali.txt',
        'example_data/logs/log_Nicholas.txt',
        'example_data/logs/log_Nikhil.txt',
        'example_data/logs/log_Atharv.txt',
        'example_data/logs/log_Shariq.txt',
        'example_data/logs/log_Haley.txt',
        'example_data/logs/log_Sophie.txt',
        'example_data/logs/log_Satyam.txt',
        'example_data/logs/log_Manika.txt'
    ]

    date_pattern = r'\d{4}-\d{2}-\d{2}'  # 假设日期格式为 YYYY-MM-DD
    upload_pattern = re.compile(r'upload the coding result of \d+ at \d{4}-\d{2}-\d{2}')

    dates = []

    # 解析每个日志文件，提取符合条件的日期
    for log_file in log_files:
        with open(log_file, 'r') as file:
            for line in file:
                if upload_pattern.search(line):
                    match = re.search(date_pattern, line)
                    if match:
                        dates.append(match.group(0))

    # 统计每个日期的记录数
    date_counts = Counter(dates)

    # 将数据转换为DataFrame
    df = pd.DataFrame(list(date_counts.items()), columns=['Date', 'Count'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # 生成一个完整的日期范围
    start_date = df['Date'].min()
    end_date = df['Date'].max()
    all_dates = pd.date_range(start=start_date, end=end_date, freq='D')

    # 将完整的日期范围与统计结果合并，缺少的日期填充为0
    df_all_dates = pd.DataFrame(all_dates, columns=['Date'])
    df = pd.merge(df_all_dates, df, on='Date', how='left')
    df['Count'] = df['Count'].fillna(0).astype(int)  # 确保计数是整数

    # 计算最后一天和前一天的差值
    if len(df) > 1:
        last_day_count = df.iloc[-2]['Count']
        previous_day_count = df.iloc[-3]['Count']
        difference = last_day_count - previous_day_count
        yesterday = df.iloc[-2]['Count']
    else:
        difference = 0  # 如果数据不足两天，差值为0

    # 使用 Plotly 绘制折线图并美化
    fig = go.Figure()

    # 添加阴影填充区域
    fig.add_trace(go.Scatter(
        x=df['Date'], y=df['Count'],
        mode='lines+markers',
        marker=dict(size=8, color='rgb(31, 119, 180)'),
        line=dict(width=2, color='rgb(31, 119, 180)'),
        fill='tozeroy',  # 填充到 y=0
        fillcolor='rgba(31, 119, 180, 0.2)',
        text=df['Count'],
        textposition='top center'
    ))

    # 更新图表布局
    fig.update_layout(
        title='Daily Upload Counts (All Users)',
        xaxis_title='Date',
        yaxis_title='Number of Uploads',
        plot_bgcolor='#f9f9f9',
        hovermode='x unified',
        font=dict(family='Arial, sans-serif', size=12, color='#000'),
        title_font=dict(size=20, color='rgb(31, 119, 180)', family='Arial, sans-serif'),
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
        yaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
    )

    fig.update_xaxes(
        tickformat='%Y-%m-%d',
        tickangle=45
    )

    annotations = []
    for i in range(len(df)):
        annotations.append(dict(x=df['Date'][i], y=df['Count'][i],
                                text=f'{df["Count"][i]}',
                                xanchor='center', yanchor='bottom',
                                showarrow=False, font=dict(size=12, color='rgb(31, 119, 180)')))

    fig.update_layout(annotations=annotations)
    
    return fig,difference,yesterday

def find_indiv(name):
    log_file = f'example_data/logs/log_{name}.txt'
    date_pattern = r'\d{4}-\d{2}-\d{2}'  # 假设日期格式为 YYYY-MM-DD
    upload_pattern = re.compile(r'upload the coding result of \d+ at \d{4}-\d{2}-\d{2}')

    dates = []

    # 解析日志文件，提取符合条件的日期
    with open(log_file, 'r') as file:
        for line in file:
            if upload_pattern.search(line):
                match = re.search(date_pattern, line)
                if match:
                    dates.append(match.group(0))

    # 统计每个日期的记录数
    date_counts = Counter(dates)

    # 将数据转换为DataFrame
    df = pd.DataFrame(list(date_counts.items()), columns=['Date', 'Count'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # 生成一个完整的日期范围
    start_date = df['Date'].min()
    end_date = df['Date'].max()
    all_dates = pd.date_range(start=start_date, end=end_date, freq='D')

    # 将完整的日期范围与统计结果合并，缺少的日期填充为0
    df_all_dates = pd.DataFrame(all_dates, columns=['Date'])
    df = pd.merge(df_all_dates, df, on='Date', how='left')
    df['Count'] = df['Count'].fillna(0).astype(int)  # 确保计数是整数

    # 使用 Plotly 绘制折线图并美化
    fig = go.Figure()

    # 添加阴影填充区域
    fig.add_trace(go.Scatter(
        x=df['Date'], y=df['Count'],
        mode='lines+markers',
        marker=dict(size=8, color='rgb(31, 119, 180)'),
        line=dict(width=2, color='rgb(31, 119, 180)'),
        fill='tozeroy',  # 填充到 y=0
        fillcolor='rgba(31, 119, 180, 0.2)',
        text=df['Count'],
        textposition='top center'
    ))

    # 更新图表布局
    fig.update_layout(
        title=f'Daily Upload Counts ({name})',
        xaxis_title='Date',
        yaxis_title='Number of Uploads',
        plot_bgcolor='#f9f9f9',
        hovermode='x unified',
        font=dict(family='Arial, sans-serif', size=12, color='#000'),
        title_font=dict(size=20, color='rgb(31, 119, 180)', family='Arial, sans-serif'),
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
        yaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2),
    )

    fig.update_xaxes(
        tickformat='%Y-%m-%d',
        tickangle=45
    )

    annotations = []
    for i in range(len(df)):
        annotations.append(dict(x=df['Date'][i], y=df['Count'][i],
                                text=f'{df["Count"][i]}',
                                xanchor='center', yanchor='bottom',
                                showarrow=False, font=dict(size=12, color='rgb(31, 119, 180)')))

    fig.update_layout(annotations=annotations)
    
    return fig
st.title('Dashboard')
fig,difference,yesterday = create_dashboard_figure()
st.write(find_indiv("Sophie"))