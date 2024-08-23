import streamlit as st

st.set_page_config(
    page_title="Consensus",
    page_icon="🤝",
    layout="wide"
)
st.markdown(
    """
    <style>
    .custom-text {
        font-weight: bold;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .custom-text-1 {
        font-weight: normal;
        font-family: 'Courier New', Courier, monospace;
        color: #555;
    }
    .custom-text-2 {
        font-weight: normal;
        font-family: 'Times New Roman', Times, serif;
        color: #777;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Consensus')

import pandas as pd
import fire_test
import nltk
from nltk.tokenize import sent_tokenize
import os
import random
from datetime import datetime
nltk.download('punkt')
nltk.download('punkt_tab')
st.session_state.user = 'demo_user'
# import test_plot as tp
# import progress_plot as pp
# import create_realationship_plot as crp
# import dount_chart as dc
# import fire_test
# import combine_plot as cb
# Define the file paths
file_paths = [
    'record/record_Atharv.csv',
    'record/record_Manika.csv',
    'record/record_Jigyashu.csv',
    'record/record_Manali.csv',
    'record/record_Nicholas.csv',
    'record/record_Nikhil.csv',
    'record/record_Amreentaj.csv',
    'record/record_Shariq.csv',
    'record/record_Haley.csv',
    'record/record_Sophie.csv',
    'record/record_Satyam.csv',
    'record/record_Tina.csv'

]

if 'downloaded' not in st.session_state:
    st.session_state['downloaded'] = True
    st.session_state['record_file_paths'] = {
        'Atharv': fire_test.download_from_folder('record/record_Atharv.csv'),
        'Manika': fire_test.download_from_folder('record/record_Manika.csv'),
        'Jigyashu': fire_test.download_from_folder('record/record_Jigyashu.csv'),
        'Manali': fire_test.download_from_folder('record/record_Manali.csv'),
        'Nicholas': fire_test.download_from_folder('record/record_Nicholas.csv'),
        'Nikhil': fire_test.download_from_folder('record/record_Nikhil.csv'),
        'Amreentaj': fire_test.download_from_folder('record/record_Amreentaj.csv'),
        'Shariq': fire_test.download_from_folder('record/record_Shariq.csv'),
        'Haley': fire_test.download_from_folder('record/record_Haley.csv'),
        'Sophie': fire_test.download_from_folder('record/record_Sophie.csv'),
        'Satyam': fire_test.download_from_folder('record/record_Satyam.csv'),
        'Tina': fire_test.download_from_folder('record/record_Tina.csv'),
        'Demo_user':fire_test.download_from_folder('record/record_demo_user.csv'),
        'Pengfei':fire_test.download_from_folder('record/record_Pengfei.csv')
        }
    st.session_state['log_file_paths'] = {
        'Atharv': fire_test.download_from_folder('log/log_Atharv.txt'),
        'Manika': fire_test.download_from_folder('log/log_Manika.txt'),
        'Jigyashu': fire_test.download_from_folder('log/log_Jigyashu.txt'),
        'Manali': fire_test.download_from_folder('log/log_Manali.txt'),
        'Nicholas': fire_test.download_from_folder('log/log_Nicholas.txt'),
        'Nikhil': fire_test.download_from_folder('log/log_Nikhil.txt'),
        'Amreentaj': fire_test.download_from_folder('log/log_Amreentaj.txt'),
        'Shariq': fire_test.download_from_folder('log/log_Shariq.txt'),
        'Haley': fire_test.download_from_folder('log/log_Haley.txt'),
        'Sophie': fire_test.download_from_folder('log/log_Sophie.txt'),
        'Satyam': fire_test.download_from_folder('log/log_Satyam.txt'),
        'Tina': fire_test.download_from_folder('log/log_Tina.txt'),
        'Demo_user':fire_test.download_from_folder('log/log_demo_user.txt'),
        'Demo_user':fire_test.download_from_folder('log/log_Pengfei.txt')
    }

import test_plot as tp
import progress_plot as pp
import create_realationship_plot as crp
import dount_chart as dc
import fire_test
import combine_plot as cb
# def count_handle_Y(file_path):
#     try:
#         df = pd.read_csv(file_path)
#         return df['Progress'].value_counts().get('Y', 0)
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#         return 0
#     except KeyError:
#         print(f"Column 'handle' not found in: {file_path}")
#         return 0

# import matplotlib.pyplot as plt
# import seaborn as sns



def extract_elements(input_list):
    
    random.seed(10)
    number_of_items = len(input_list) // 10 + 1 if len(input_list) % 10 else len(input_list) // 10


    if len(input_list) == 0:
        return [] 
    elif number_of_items == 0:
        number_of_items = 1
    

    extracted_items = random.sample(input_list, min(number_of_items, len(input_list)))
    
    return extracted_items

def increment_i():
    if st.session_state.i < 21:  
        st.session_state.i += 1
    else:
        st.write("Nothing left for the coding example")


def main():
    current_user = 'demo_user'

    if 'i' not in st.session_state:
        st.session_state.i = 0

    csv_file = 'record/record_' + current_user + '.csv'
    local_file_path = fire_test.download_from_folder(csv_file)
    
    record = pd.read_csv(csv_file)


    if 'i' not in st.session_state:
        st.session_state.i = 0
    while record['Progress'][st.session_state.i] in ['Y', 'skip']:
        st.session_state.i += 1    

    PMID = int(record['handle'][st.session_state.i])

    file_name_ac = str(PMID) + ".txt"

    path_for_acknowledgement = "seperate_acknowledgement/" + str(file_name_ac) 


    fire_test.download_from_folder(path_for_acknowledgement)


    file_contents = []
    base_path = r'seperate_acknowledgement'
    local_path = os.path.join(base_path, file_name_ac)

    print('this is the path' + local_path)
    with open(local_path, 'r',encoding='utf-8') as file:
        file_contents = file.read()


    
    paragraph = file_contents
    
    sentences = sent_tokenize(paragraph)
    sentences = extract_elements(sentences)
    data = {}
    numberlist = []
    for i in range(len(sentences)):
        numberlist.append(str(PMID)+str(i+1))
        
    data['Sentence'] = sentences
    data['SentenceNumber'] = numberlist
    data['Support Coding'] = [''] * len(data['Sentence'])
    data['Tag Group 2'] = [''] * len(data['Sentence'])
    data['Note'] = [''] * len(data['Sentence'])
    df = pd.DataFrame(data)
    
    # define tags
    tags_group_1 = ['Theses Advisor/Committee Members','Cultural and Community Support' ,'Descriptive Sentence','Writing Support','Academic Support','Staff Support','Comfort Support', 'Friends/Family Support', 'Financial Support', 'Technical Support','Access to Data','Religious Support','Library Support','Student Organizations/Clubs/Research Groups','Government Support','No Subject Found','Peer Support','Unknown Support','Incomplete Sentence','Custom','Not Sure']
    tags_group_2 = ['Very Positive', 'Positive', 'Neutral','Negative']
    lines = len(df)



    
    #if 'tags_1' not in st.session_state:
    st.session_state[str(PMID)+'tags_1'] = [[] for _ in range(lines)]
    #if 'tags_2' not in st.session_state:
    st.session_state[str(PMID)+'tags_2'] = [[] for _ in range(lines)]
    st.session_state[str(PMID)+'notes'] = [''] * lines

    def save_and_next():
        # Ensure data is saved before the state is incremented
        if st.session_state['support_sentiment'] == 'Support':
            target_file = 'consensus_app/Support_A.csv'
        elif st.session_state['support_sentiment'] == 'Sentiment':
            target_file = 'consensus_app/Sentiment_A.csv'
            
        consensus_df.to_csv(target_file, index=False, encoding='utf-8')  
        fire_test.upload_to_firebase_storage(target_file, target_file) 
        st.session_state.consensus_i += 1  
        st.session_state.multiselect = []
        st.session_state.back = False

    # Initialize session state
    if 'support_sentiment' not in st.session_state:
        st.session_state['support_sentiment'] = 'Not Selected Yet'
    if 'consensus_i' not in st.session_state:
        st.session_state.consensus_i = 0
    if 'back' not in st.session_state:
        st.session_state.back = False
    if 'multiselect' not in st.session_state:
        st.session_state.multiselect = []

    # Reload button for support/sentiment data
    sentimen_file = fire_test.download_from_folder('consensus_app/Sentiment_A.csv')
    support_file = fire_test.download_from_folder('consensus_app/Support_A.csv')
    # Selection box
    selected_task = st.selectbox(
        "Select Task",
        ('Support', 'Sentiment')
    )

    # Update session state based on selection
    if selected_task != "Select a task":
        st.session_state['support_sentiment'] = selected_task

    # Load data based on session state
    if st.session_state['support_sentiment'] == 'Support':
        consensus_df = pd.read_csv('consensus_app/Support_A.csv')
    elif st.session_state['support_sentiment'] == 'Sentiment':
        consensus_df = pd.read_csv('consensus_app/Sentiment_A.csv')
    # Main logic for consensus tagging
    if consensus_df['Consensus'].isna().any():
        if st.session_state.consensus_i >= len(consensus_df):
            st.session_state.consensus_i = 0
        if not st.session_state.back:    
            while st.session_state.consensus_i < len(consensus_df) and pd.notna(consensus_df.at[st.session_state.consensus_i, 'Consensus']):
                st.session_state.consensus_i += 1

        if st.session_state.consensus_i >= len(consensus_df):
            st.session_state.consensus_i = 0
            st.warning("You have reviewed all entries. Starting over.")

        if st.session_state['support_sentiment'] == 'Support':
            tags_group = [
                'Theses Advisor/Committee Members','Cultural and Community Support','Descriptive Sentence', 'Writing Support', 'Academic Support',
                'Staff Support', 'Friends/Family Support', 'Financial Support', 'Technical Support', 'Access to Data',
                'Religious Support', 'Library Support', 'Comfort Support', 'Student Organizations/Clubs/Research Groups', 'Government Support',
                'No Subject Found', 'Peer Support', 'Unknown Support', 'Incomplete Sentence', 'Custom', 'Not Sure'
            ]
        elif st.session_state['support_sentiment'] == 'Sentiment':
            tags_group = ['Very Positive', 'Positive', 'Neutral', "No Sentiment"]

        selected_options = st.multiselect("Please choose options:", tags_group, key="multiselect")

        if "Custom" in selected_options:
            custom_input = st.text_input("Please enter your custom option:")
            if custom_input:
                index_replace = selected_options.index('Custom')
                selected_options[index_replace] = custom_input

        option_str = ','.join(selected_options)
        if option_str:
            consensus_df.at[st.session_state.consensus_i, 'Consensus'] = option_str

        if 'Unnamed: 0' in consensus_df.columns:
            consensus_df = consensus_df.iloc[:, 1:]

        data = [""] * 4
        data[0] = consensus_df['Sentence'][st.session_state.consensus_i]
        data[1] = consensus_df['Manika'][st.session_state.consensus_i]
        data[2] = consensus_df['Sophie'][st.session_state.consensus_i]
        data[3] = option_str

        st.markdown(f'<div class="custom-text">{data[0]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="custom-text-1">Coder1:  {data[1]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="custom-text-1">Coder2:  {data[2]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="custom-text-2">Consensus: {data[3]}</div>', unsafe_allow_html=True)

        st.sidebar.button("Next", on_click=save_and_next)
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write("The total sentences:", len(consensus_df))
        st.write("The number of sentences your finished is", st.session_state.consensus_i)

    else:
        st.success("You have completed all the tasks for this part, congratulations!")

if __name__ == "__main__":
    main()
