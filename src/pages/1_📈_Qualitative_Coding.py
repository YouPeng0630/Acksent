import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import os
import random
from datetime import datetime










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
    page_title="Qualitative Coding",
    page_icon="📈",
    layout="wide"
)
    st.title('Qualitative Coding')
    current_user = 'demo_user'
    csv_file = 'example_data/record/record_' + current_user + '.csv'
    record = pd.read_csv(csv_file)   
    if 'download' not in st.session_state:
        nltk.download('punkt')
        nltk.download('punkt_tab')
        st.session_state.download = True


    st.session_state.user = 'demo_user'
    if 'i' not in st.session_state:
        st.session_state.i = 0

    #record = pd.read_csv(csv_file)
    if st.session_state.i >= len(record)-1:
        st.title("Qualitative Coding Completed")
        st.success("Congratulations! You have completed all qualitative coding tasks!")
        st.balloons()  # Display balloon animation
    else:
        if 'i' not in st.session_state:
            st.session_state.i = 0
        while record['Progress'][st.session_state.i] in ['Y', 'skip']:
            st.session_state.i += 1    

        PMID = int(record['handle'][st.session_state.i])

        file_name_ac = str(PMID) + ".txt"

        #path_for_acknowledgement = "example_data/ack_files/" + str(file_name_ac) 

        file_contents = []
        base_path = r'example_data/ack_files/'
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
        st.title('Coding app for Thanking the World Project')
        st.write(f"ID for this ETD is {PMID}")



        
        #if 'tags_1' not in st.session_state:
        st.session_state[str(PMID)+'tags_1'] = [[] for _ in range(lines)]
        #if 'tags_2' not in st.session_state:
        st.session_state[str(PMID)+'tags_2'] = [[] for _ in range(lines)]
        st.session_state[str(PMID)+'notes'] = [''] * lines

        for i, row in df.iterrows():
            st.markdown(f"### {row['Sentence']} ({row['SentenceNumber']})")

            col1, col2, col3 = st.columns((3,3,1))

            valid_defaults_1 = [tag for tag in st.session_state[str(PMID)+'tags_1'][i] if tag in tags_group_1]
            valid_defaults_2 = [tag for tag in st.session_state[str(PMID)+'tags_2'][i] if tag in tags_group_2]

            with col1:
                selected_tags_1 = st.multiselect(
                    "Select tag(s) for Support Coding",
                    options=tags_group_1,
                    default=valid_defaults_1,
                    key=f"i1_{PMID}{i}"
                )
                if 'Custom' in selected_tags_1:
                    custom_tag_input_key = f"custom_tag_1_{i}"  
                    custom_tag_1 = st.text_input("Enter your custom tag for Support Coding", key=custom_tag_input_key)
                    
                    confirm_button_key = f"confirm_custom_{i}" 
                    confirm_custom = st.button("Confirm Custom Tag", key=confirm_button_key)

                    if confirm_custom:
                        
                        if custom_tag_1.strip():  
                        
                            if 'Custom' in selected_tags_1:
                                selected_tags_1.remove('Custom')  
                            selected_tags_1.append(custom_tag_1)  
                            st.session_state[str(PMID)+'tags_1'][i] = selected_tags_1  
                            st.success(f"Custom tag '{custom_tag_1}' added.")  
                        else:
                            st.error("Please enter a valid custom tag.")           
                st.session_state[str(PMID)+'tags_1'][i] = selected_tags_1
            with col2:
                selected_tags_2 = st.multiselect(
                    "Select tag(s) for Sentiments",
                    options=tags_group_2,
                    default=valid_defaults_2,
                    key=f"i2_{PMID}{i}"
                )
            with col3:
                note = st.text_input(
                    "Enter your notes",
                    value=st.session_state[str(PMID)+'notes'][i],
                    key=f"note_{PMID}{i}"
                )
            st.session_state[str(PMID)+'notes'][i] = note
            # update session_state to see the change
            st.session_state[str(PMID)+'tags_2'][i] = selected_tags_2

            # update DataFrame
            df.at[i, 'Support Coding'] = ', '.join(selected_tags_1)
            df.at[i, 'Tag Group 2'] = ', '.join(selected_tags_2)
            df.at[i, 'Note'] = note
        df.to_csv('my_dataframe.csv', index=False)    
        # show update dataframe
        file_name = str(PMID) +'_'+ current_user+'.txt'
        def upload_click():    
            #st.sidebar.write("Successfully uploaded to server")
            record['Progress'][st.session_state.i] = 'Y'
            record.to_csv(csv_file, index=False)
            #fire_test.upload_to_firebase_storage(csv_file, csv_file)
            # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # log_file = 'log/log_'+ current_user + '.txt'
            #local_file_path = fire_test.download_from_folder(log_file)
            # setence_save = current_user + " upload the coding result of " + str(PMID) + " at " + current_time + "\n"
            # with open(log_file, 'a') as file:
            #     file.write(setence_save)
            #fire_test.upload_to_firebase_storage(log_file, log_file)
    
        def skip_click():
            record['Progress'][st.session_state.i] = 'skip'
            record.to_csv(csv_file, index=False)
            #fire_test.upload_to_firebase_storage(csv_file, csv_file)
            # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # log_file = 'log/log_'+ current_user + '.txt'
            # #local_file_path = fire_test.download_from_folder(log_file)
            # sentence_skip = current_user + " skipped the ETD, which number is " + str(PMID) + ", at " + current_time + "\n"
            # with open(log_file, 'a') as file:
            #     file.write(sentence_skip)

            #fire_test.upload_to_firebase_storage(log_file, log_file)
        st.sidebar.button("Save",on_click=upload_click)
        st.sidebar.button("Skip",on_click=skip_click)
        st.write(st.session_state.i)
        st.write(record)
        def back_click():
            if st.session_state.i == 0:
                st.write("this is the first sentence")
            if st.session_state.i > 0:
                if record['Progress'][st.session_state.i] == 'N':
                    record['Progress'][st.session_state.i - 1] = 'N'
                    record.to_csv(csv_file)
                    st.session_state.i -= 1
                    st.write(st.session_state.i)
                # elif record['Progress'][st.session_state.i] == 'Back':
                #     record['Progress'][st.session_state.i] = 'Y'
                #     record['Progress'][st.session_state.i - 1] = 'Back'
                #     st.session_state.i -= 1
                #     st.write("step2")  
                # record.to_csv(csv_file, index=False)
                #fire_test.upload_to_firebase_storage(csv_file, csv_file)
                # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # log_file = 'log/log_'+ current_user + '.txt'
                #local_file_path = fire_test.download_from_folder(log_file)
                # sentence_skip = current_user + " use back function, the PMID is " + str(PMID) + ", at " + current_time + "\n"
                # with open(log_file, 'a') as file:
                #     file.write(sentence_skip)
                #fire_test.upload_to_firebase_storage(log_file, log_file)
        st.sidebar.button('Back', on_click = back_click)

        st.button("Save",on_click=upload_click,key = 'save1') 

        st.write(df)
        
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write("The total number of ETDs assigned is :" ,len(record)+1)
        st.write("The acknowlegement you have already finished is :" ,st.session_state.i)

if __name__ == "__main__":
    main()
