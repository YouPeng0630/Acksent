import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import streamlit as st

# 假设之前的代码已经处理好了CSV文件，并将结果存入progress_counts
# 这里直接加载数据并计算 'Y' 的数量
record_dir = 'example_data/record'

if not os.path.exists(record_dir):
    raise ValueError(f"The directory {record_dir} does not exist.")

record_file_paths = {filename: os.path.join(record_dir, filename) 
                     for filename in os.listdir(record_dir) 
                     if filename.endswith('.csv')}

# Function to count 'Y' in Progress column
def count_y_in_progress(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Reading file: {file_path}")  # 添加打印信息
        print(df.head())  # 打印前几行，确认内容
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

# 创建 progress_counts 字典
progress_counts = {}
for name, file_path in record_file_paths.items():
    count = count_y_in_progress(file_path)
    name = name.replace('.csv', '')  # 去除文件扩展名
    print(f"{name}: {count}")  # 打印每个文件的计数结果
    if name in progress_counts:
        progress_counts[name] += count
    else:
        progress_counts[name] = count

print("Final progress counts:", progress_counts)  # 最终结果

def display_grouped_horizontal_bar_chart():
    # 定义数据，确保使用正确的键
    groups = {
        'Group 1': [int(progress_counts.get('record_Sophie', 0)), int(progress_counts.get('record_Manika', 0))],
        'Group 2': [int(progress_counts.get('record_Jigyashu', 0)), int(progress_counts.get('record_Nikhil', 0))],
        'Group 3': [int(progress_counts.get('record_Manali', 0)), int(progress_counts.get('record_Satyam', 0))],
        'Group 4': [int(progress_counts.get('record_Amreentaj', 0)), int(progress_counts.get('record_Haley', 0))],
        'Group 5': [int(progress_counts.get('record_Nicholas', 0)), int(progress_counts.get('record_Atharv', 0))],
        'Group 6': [int(progress_counts.get('record_Tina', 0)), int(progress_counts.get('record_Shariq', 0))]
    }

    print("Groups data for plotting:", groups)  # 打印用于绘图的数据

    names = [
        ('log/log_Sophie.txt', 'log/log_Manika.txt'),
        ('log/log_Jigyashu.txt', 'log/log_Nikhil.txt'),
        ('log/log_Manali.txt', 'log/log_Satyam.txt'),
        ('log/log_Amreentaj.txt', 'log/log_Haley.txt'),
        ('log/log_Nicholas.txt', 'log/log_Atharv.txt'),
        ('log/log_Tina.txt', 'log/log_Shariq.txt')
    ]

    # 提取数据
    labels = list(groups.keys())
    data1 = [values[0] for values in groups.values()]
    data2 = [values[1] for values in groups.values()]

    y = np.arange(len(labels))  # 标签位置

    # 创建横向柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    rects1 = ax.barh(y, [-d for d in data1], 0.4, color='skyblue')  # 向左延伸
    rects2 = ax.barh(y, data2, 0.4, color='salmon')  # 向右延伸

    # 添加标签和标题
    ax.set_xlabel('Numbers')
    ax.set_ylabel('Groups')
    ax.set_title('Number Relations in Each Group')
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # 反转Y轴使得组从上到下

    # 添加名字标签
    for i, (name1, name2) in enumerate(names):
        name1_clean = name1.replace('log/log_', '').replace('.txt', '')
        name2_clean = name2.replace('log/log_', '').replace('.txt', '')
        ax.text(-data1[i] - 0.5, y[i] - 0.2, name1_clean, ha='right', va='center', color='black')
        ax.text(data2[i] + 0.5, y[i] + 0.2, name2_clean, ha='left', va='center', color='black')

    # 添加网格
    ax.grid(True, linestyle='--', alpha=0.7)

    # 保存并显示图表
    fig.savefig('grouped_horizontal_bar_chart.png')
    plt.show()

    # 在 Streamlit 中显示图片
    st.image('grouped_horizontal_bar_chart.png')

# 在 Streamlit 中调用这个函数
if __name__ == '__main__':
    display_grouped_horizontal_bar_chart()
