import pandas as pd
import os
import streamlit as st


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
        return df['Progress'].value_counts().get('Y', 0)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0
    except pd.errors.EmptyDataError:
        #print(f"Empty data file: {file_path}")
        return 0
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return 0

# Extract names and store counts in a dictionary for record files
progress_counts = {}
for name, file_path in record_file_paths.items():
    count = count_y_in_progress(file_path)
    if name in progress_counts:
        progress_counts[name] += count
    else:
        progress_counts[name] = count

# 输出结果
print("Progress Counts:", progress_counts)
