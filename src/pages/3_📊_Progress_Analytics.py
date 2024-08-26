import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import os
import random

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


# from src.components.charts import create_combined_plot1,make_donut, generate_progress_chart,create_dashboard_figure
from src.components.charts.combine_plot import create_combined_plot1
from src.components.charts.test_plot import generate_progress_chart
from src.components.charts.dount_chart import make_donut
from src.components.charts.progress_plot import create_dashboard_figure






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


    st.set_page_config(
        page_title="Progress_Analytics",
        page_icon="📊",
        layout="wide"
    )
    if 'download' not in st.session_state:
        nltk.download('punkt')
        nltk.download('punkt_tab')
        st.session_state.download = True
    st.title('Progress Analytics')

    support_df = pd.read_csv('example_data/consensus/Support_A.csv')
    sentiment_df = pd.read_csv('example_data/consensus/Sentiment_A.csv')
    record_df = pd.read_csv('example_data/record/record_demo_user.csv')


    support_length = len(support_df)
    sentiment_length = len(sentiment_df)
    record_length = len(record_df)

    support_none = support_df['Consensus'].isna().sum()
    sentiment_none = sentiment_df['Consensus'].isna().sum()
    record_none = record_df['Progress'].isna().sum()

    st.session_state.user = 'demo_user'

    file_paths = [
        'example_data/record/record_Atharv.csv',
        'example_data/record/record_Manika.csv',
        'example_data/record/record_Jigyashu.csv',
        'example_data/record/record_Manali.csv',
        'example_data/record/record_Nicholas.csv',
        'example_data/record/record_Nikhil.csv',
        'example_data/record/record_Amreentaj.csv',
        'example_data/record/record_Shariq.csv',
        'example_data/record/record_Haley.csv',
        'example_data/record/record_Sophie.csv',
        'example_data/record/record_Satyam.csv',
        'example_data/record/record_Tina.csv'
    ]


    current_user = 'demo_user'

    if 'i' not in st.session_state:
        st.session_state.i = 0

    csv_file = 'example_data/record/record_' + current_user + '.csv'
    
    record = pd.read_csv(csv_file)


    if 'i' not in st.session_state:
        st.session_state.i = 0
    while record['Progress'][st.session_state.i] in ['Y', 'skip']:
        st.session_state.i += 1    

    PMID = int(record['handle'][st.session_state.i])

    file_name_ac = str(PMID) + ".txt"

    #path_for_acknowledgement = "example_data/ack_files/" + str(file_name_ac) 


    file_contents = []
    base_path = r'example_data/ack_files'
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

    def count_handle_Y(file_path):
        try:
            df = pd.read_csv(file_path)
            return df['Progress'].value_counts().get('Y', 0)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return 0
        except KeyError:
            print(f"Column 'handle' not found in: {file_path}")
            return 0
        
    tab1 , tab2 = st.tabs(['Qualitative Coding','Consensus'])
    
    with tab1:  
        col = st.columns((1, 3, 3), gap='medium')
        with col[0]:
            counts = {}

            # Calculate the total count for each file
            for file_path in file_paths:
                counts[file_path] = count_handle_Y(file_path)

            # Calculate the total count across all files
            total_count_Y = int(sum(counts.values()))
            st.markdown('#### Progress')
            fig, difference, yesterday = create_dashboard_figure()
            # st.metric(label="Yesterday's Upload Count", value=yesterday, delta=str(difference))
            st.metric(label="Yesterday's Upload Count", value=0, delta=str(0))
            st.markdown('#### Qualitative Coding')
            percentage = 100 * ((record_length-record_none) /record_length)
            percentage = round(percentage, 1)
            donut_chart_total = make_donut(percentage, 'green')

            st.altair_chart(donut_chart_total, use_container_width=True)
            

        with col[1]:
            st.markdown('#### Team Progress VS Time Chart')
            st.plotly_chart(create_combined_plot1(record_length-record_none), use_container_width=True)

        with col[2]:
            st.markdown('#### Group Progress')
            fig2 = generate_progress_chart()
            st.plotly_chart(fig2)
    with tab2:
        col = st.columns((1,4),gap = 'medium')
        with col[0]:
            percentage_consensus = round(100 *((support_length+sentiment_length)-(support_none+sentiment_none))/(sentiment_length+support_length),1)
            dount_chart_consensus = make_donut(percentage_consensus,'green')
            st.markdown('####     Consensus')
            st.altair_chart(dount_chart_consensus, use_container_width=True)
        with col[1]:
            st.markdown('#### Team Progress VS Time Chart')
            st.plotly_chart(create_combined_plot1((support_length+sentiment_length-support_none-sentiment_none)), use_container_width=True)          
if __name__ == "__main__":
    main()
