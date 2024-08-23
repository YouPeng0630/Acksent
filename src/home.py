import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide"
)


st.markdown(
    """
    <style>
    .custom-text {
        font-weight: bold;
        font-family: 'Arial', sans-serif;
        color: #333;
   z }
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

st.write("# Welcome to the AckSent demo app! 👋")
st.markdown(
    """
    This is a multipage Streamlit app demo.
    **👈 Select a page from the sidebar** to see different pages.
    
    This is a demo version of the actual app designed seperately for the Acksent project. We tried our best to replicate all the features, tabs, pages, and buttons.
    We used a very small subset of the data published on Zenodo  [https://doi.org/10.5281/zenodo.13293333](https://doi.org/10.5281/zenodo.13293333) for demo purpose. This app does not save the entries you select in qualitative coding and consensus tabs.
    """)
tab1,tab2,tab3 = st.tabs(['Introduction','Usage','Codebook'])

with tab1:
    st.markdown(
    """
    # Acknowledgments
    
    This application provides access to the data presented in the “Acksent: Human Annotated Dataset of Support and Sentiments in Dissertation Acknowledgments” paper. The article and its accompanying appendix discuss in detail the methodology used to collect and code the data in the dataset.
    The full dataset is also available in .csv format on Zenodo at [https://doi.org/10.5281/zenodo.13293333](https://doi.org/10.5281/zenodo.13293333). Any questions should be directed to [manika@ou.edu](mailto:manika@ou.edu).


    ## License & Citation

    Downloads from this dataset may be used in accordance with the terms of the Creative Commons Attribution-NonCommercial-ShareAlike license (see details at [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

    ## Suggested Citation

    Authors. (2024). Acksent Demo App.([acksent-demo.streamlit.app](#))

    """
)
with tab2:
    st.markdown(
    """
    # **Usage**

    The app is divided into four tabs: **Hello (you are here)**, **Qualitative Coding**, **Consensus**, and **Progress Analytics**.

    ## **Qualitative Coding**
    In this tab, users can view the sentences they need to tag. There are options for **Support** and **Sentiment** tags available for each sentence. A note input box is also provided for adding notes to the sentences. Once users complete coding the current part of sentences, they can upload the tagged sentences to Firebase Storage by clicking the **Save** button on the sidebar.

    - The **Skip** button is for sentences where the user is not sure. It will not upload the record to the server and will show the skipped ETD again the next time the user logs in.
    - The **Back** button allows the user to return to the last ETD they just uploaded. If the user finds something they uploaded is incorrect, they can click it multiple times to go back multiple ETDs.

    ## **Consensus**
    In this tab, users can view sentences that were tagged differently by themselves and another team member. A dropdown box is provided to select the **Support** or **Sentiment** coding task. 

    - This page displays sentences labeled differently for each group member, one sentence at a time.
    - Group members can communicate on this page, select the tags they agree on, and upload them to the server using the **Save** button.
    - As with Qualitative Coding, there is a **Back** button to return to the previous step.

    ## **Progress Analytics**
    The Dashboard dynamically displays the user's progress in a task, which is updated in real-time by reading Firebase log records. 

    - This dashboard reads different log files and visualizes the data, which can help users and administrators quickly understand data trends, such as performance in coding tasks.
    """
    )
    
with tab3:
    
    st.markdown(
    """
    # Support Tags

    <table>
        <tr>
            <th>Tag</th>
            <th>Definition</th>
            <th>Examples</th>
        </tr>
        <tr>
            <td><b>Academic Support</b></td>
            <td>Teaching/co-teaching/TA-ing for a professor; getting feedback or research help from other professors; getting lab experience in an academic setting; interactions with professors</td>
            <td>
                • Thanks also to Professors Matalon and Geubelle for their contributions to the topological derivative work and Professor Gioia for enjoyable and seamless interaction while teaching for him.<br>
                • Specifically, Dr. Mauro R. Sardela, Jr. trained me to run a successful X-ray diffraction texture scan and use the X’pert XRD.<br>
                • First and foremost, I would like to sincerely thank Professor Keh-Yung Cheng for giving me the opportunity to work in his lab as an undergraduate and graduate student.<br>
                • The author would like to thank Dr. Howard V. Malmstadt for his guidance and encouragement throughout this research project.
            </td>
        </tr>
        <tr>
            <td><b>Affiliation Groups (Academic or Student)</b></td>
            <td>Any group that has a defined name that is related to student organizations/club involvement. This also encompasses research groups/college programs/lab teams/departments students are a part of</td>
            <td>
                • First, I acknowledge the support and intellect of the Community College Executive Leadership cohort of 2001 and interlopers, as well as the Second Saturday Club.<br>
                • Thanks also to the rest of the i-acoma group — past and present — for the discussion (whether research-related or not) and the occasional levity.<br>
                • I wish to thank the College of Engineering, the Department of Mechanical Science and Engineering, and my advisor, Professor Chia-Fon Lee, for their work in locating sources of funding for students such as myself.<br>
                • I am also thankful to faculty, staff, and students of the Department of Agricultural and Biological Engineering for providing resources and motivation for my research.
            </td>
        </tr>
        <tr>
            <td><b>Access to Data</b></td>
            <td>Provision of assistance or support in obtaining the necessary information or datasets; involves facilitating the acquisition, retrieval, or permission to use specific data sets, enabling individuals or organizations to gather relevant information for analysis, research, or other purposes. It also includes obtaining participants for research and taking notes/conducting interviews</td>
            <td>
                • I would like to extend my warmest appreciation to the participants of this study at both sites who so graciously gave of their time and who hosted me so kindly during my research at their campuses.
            </td>
        </tr>
        <tr>
            <td><b>Comfort Support</b></td>
            <td>Thanking any institution or person who provides food/nutrition/water and/or other basic necessities, includes pets and playing games</td>
            <td>
                • I should also thank those who have made these past few years more pleasant; the list includes eateries that have fed me and people who have been extremely kind to me.<br>
                • As an aside, I would like to thank my beloved Cubbies and Bears for their disappointing ballplay that allowed me to concentrate on the completion of this manuscript.
            </td>
        </tr>
        <tr>
            <td><b>Cultural and Community Support</b></td>
            <td>It is used to express gratitude towards ethnic communities, cultural groups, or community organizations</td>
            <td>
                • My sincere thanks go to the African community, friends, and my fellow graduate students at the University of Illinois at Urbana-Champaign who provided advice, encouragement, and support over the years.<br>
                • I am especially indebted to the Arapahoe Business Council and the members of the Arapahoe tribe, who gave so generously of their friendship and who patiently endeavored to answer my many questions.
            </td>
        </tr>
        <tr>
            <td><b>Financial Support</b></td>
            <td>Funding agencies or universities that help researchers complete their academic theses/projects. This support involves monetary contributions that cover various expenses associated with research, education, or specific project needs</td>
            <td>
                • Funding for this work was provided by various grants from the National Institutes of Health (R21 GM075930-01 and R01 GM086727), including an NIH Kirschstein Predoctoral Fellowship (F31 EB008330) and a critical research initiative grant (Campus Research Board).
            </td>
        </tr>
        <tr>
            <td><b>Friends/Family Support</b></td>
            <td>Encompasses encouragement and comfort provided by friends, family, and even teachers/professors in private settings. This form of support is typically expressed using first names of friends & family and serves to uplift and strengthen individuals emotionally during challenging times</td>
            <td>
                • I am also in debt to all the dedicated teachers who have encouraged and motivated me throughout my 23 years in the public education system.<br>
                • Finally, I would like to thank all other people that have accompanied me through the years, including professors and colleagues in the Newmark building and friends from the badminton and volleyball courts.<br>
                • Finally, I like to thank my personal mentor and former teacher Mr. Errol Clarke for all his guidance and advice.
            </td>
        </tr>
        <tr>
            <td><b>Government and Institutional Support</b></td>
            <td>Refers to assistance, aid, or resources provided by governmental entities (such as federal, state, or local governments) to individuals, organizations, or sectors within society, including legislators, lawmakers, fellowships, industry, and publishers</td>
            <td>
                • Thanks to John Foreman, editor of the News Gazette, to the Illinois Press Association, legislators Barbara Flynn Currie, Laurel Prussing, and Penny Severns.<br>
                • A special thanks goes out to the personnel of the Matica Iseljenika Srbije, to the staff of Atlas Tourism in Dubrovnik, and to the personnel of the U.S. Embassy in Beograd.<br>
                • The U.S. Fulbright Program allowed my work with Prof. Visser to begin, and for that I will always be thankful.<br>
                • One of us (J.R.) acknowledges travel support by NATO.<br>
                • The support received from the Malawi Government and the various institutions is greatly appreciated.<br>
                • I sincerely thank everyone at the ECE Publications Office, who have been so kind and helpful to me.
            </td>
        </tr>
        <tr>
            <td><b>Library Support</b></td>
            <td>Refers to the assistance provided by libraries and librarians to help individuals complete searches, tasks, or research endeavors. This support may involve guidance on navigating library resources, locating relevant materials, and utilizing research tools effectively to enhance the quality and efficiency of the information retrieval process</td>
            <td>
                • The initial stages of this study were begun at the Deutscher Sprachatlas, Marburg am Lahn where Ludwig E. Schmitt made available to me the very helpful resources of the Sprachatlas library.<br>
                • I would like to acknowledge the staffs of the various manuscript collections used in this project, especially those at the Lilly Library in Bloomington, Indiana, the Louis A. Pelletier Library in Meadville, Pennsylvania, and the Baker Library in Hanover, New Hampshire, for the assistance they gave in this project.
            </td>
        </tr>
        <tr>
            <td><b>Peer Support</b></td>
            <td>Refers to assistance and encouragement provided by fellow students or colleagues studying at the same or different university or department. This support can involve helping with experiments, coding, teaching, and other collaborative activities aimed at mutual academic or professional growth</td>
            <td>
                • In coming to the end of the long journey that has produced this dissertation, I sincerely wish to thank those who shared its path with me, in particular, my fellow graduate students Dale Kitchen and Pedram Roushan with whom I acquired the majority of the data presented here.<br>
                • I am also indebted to the help of an undergraduate researcher, Eryn Finke, who performed several of the experiments that make up this thesis.<br>
                • Thanks to my mentees who I brought to the lab with me many times to help keep me company (Alandis & Freddie).
            </td>
        </tr>
        <tr>
            <td><b>Religious Support</b></td>
            <td>It involves drawing on quotes from religious texts and making references to the names of deities or higher powers for inspiration, guidance, or comfort. This form of support often includes expressions rooted in faith and spirituality to provide strength and solace in various situations</td>
            <td>
                • Most importantly, I will thank and acknowledge my Lord and Savior Jesus Christ in giving me the wherewithal and strength to complete this thesis research.<br>
                • I want to begin by thanking, first and foremost, my spiritual master, Dae-Hang Keun-Seunim, who has awakened me to the importance of holding faith in my inner foundation as the guide for my life.
            </td>
        </tr>
        <tr>
            <td><b>Staff Support</b></td>
            <td>Staff support refers to assistance, guidance, and administrative help provided by graduate school advisors (distinct from thesis advisors) and departmental staff. This support may include advising on academic matters, navigating administrative procedures, and facilitating student needs within the academic and departmental context</td>
            <td>
                • Many thanks to the staff of the Computer Science department, including but not limited to: Barb Cicone, Donna Coleman, Mark Faust, Shirley Finke, Mary Beth Kelley, David E. Mussulman, and Joshua Stone for their prompt help and support at multiple junctures of my PhD studies.<br>
                • I also thank my undergraduate academic advisor, Professor Ron Cytron.
            </td>
        </tr>
        <tr>
            <td><b>Technical Support</b></td>
            <td>It involves providing access to physical spaces such as laboratories, as well as offering specific tools, assistance, and resources related to technical aspects. This support is not limited to any particular provider and may be offered by professors, staff, or other relevant personnel. It encompasses all forms of technical assistance required for academic or research activities</td>
            <td>
                • The use of Micro-Nano-Mechanical Systems and Micro and Nanotechnology Laboratory cleanrooms allowed the fabrication of all the cantilever devices described in this dissertation, while the BioNano Laboratory within Micro and Nanotechnology Laboratory provided the equipment and space for some of the measurements.<br>
                • I am indebted to Dr. Ken Christensen for the use of his water tunnel facility and to Kent Elam for his technical support with the facility.
            </td>
        </tr>
        <tr>
            <td><b>Thesis Advisor and Committee Members Support</b></td>
            <td>Refers to guidance, feedback, and assistance provided by thesis advisors and committee members</td>
            <td>
                • In particular, I would like to thank my adviser, Prof. Umberto Ravaioli, for his support, his great flexibility, and most importantly his intellectual guidance and his unique and broad vision of science.
            </td>
        </tr>
        <tr>
            <td><b>Writing Support</b></td>
            <td>It involves assistance and feedback in composing a thesis, including help from peers, colleagues, or professors other than the thesis advisor. This support encompasses receiving feedback on drafts, guidance on structure and clarity, and assistance with proofreading and editing to enhance the quality of the written work</td>
            <td>
                • I would also like to acknowledge Scott Cromar who has contributed significantly to Chapter 3 and who has also been a great sounding board for new ideas.<br>
                • Paul Adamczyk provided comments not only on this dissertation, but also on politics, history, geography and philosophy in general.
            </td>
        </tr>
        <tr>
            <td><b>Unknown Support</b></td>
            <td>It refers to assistance mentioned in acknowledgments where an organization or individual is listed with a vague or unclear subject name, making it uncertain what type of support they provided</td>
            <td>
                • My special thanks to many without whom this project would not have happened: Utah Chapter, National Alliance of the Mentally Ill (NAMI).<br>
                • Paul Adamczyk provided comments not only on this dissertation, but also on politics, history, geography and philosophy in general.
            </td>
        </tr>
        <tr>
            <td><b>Unspecified Contributor</b></td>
            <td>It refers to any instance where there is a grammatical subject present (e.g., they, he, she, me, we, you), but it is unclear who the person or organization is. Despite the ambiguity, it indicates that some kind of support was provided</td>
            <td>
                • The intellect and care they brought to bear on this process is remarkable.<br>
                • I deeply value their friendship as well as their insight.<br>
                • This project would not be possible without the support of many people.<br>
                • I would have never made it to this stage of Ph.D. study without the help and support from many people.
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    
    
    st.markdown("""
    # Additional Tags

    <table>
        <tr>
            <th>Tag</th>
            <th>Definition</th>
            <th>Examples</th>
        </tr>
        <tr>
            <td><b>Descriptive Sentence</b></td>
            <td>A sentence lacking a grammatical subject in which no clear support seems to be suggested</td>
            <td>
                • There have been frequent storms and encounters with rough seas with only brief periods of smooth sailing.<br>
                • As I engaged in that process, I occasionally discerned parallels between the participants.<br>
                • It's been terrible, but it will be fine, in nostalgic retrospect.<br>
                • His comprehensive and wide view towards research has opened my eyes to see the areas where I (still) need to grow.
            </td>
        </tr>
        <tr>
            <td><b>Incomplete Sentence</b></td>
            <td>Refers to segments of text that do not form complete grammatical structures or lack essential elements such as subjects or predicates, making them incomplete in terms of standard syntax. These kinds of sentences were generated due to OCR error</td>
            <td>
                • Foremost, I must thank my ad?<br>
                • I would like to take this opportunity to thank those who have con...?
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
        
    

    st.markdown("""
    # Sentiment Tags

    <table>
        <tr>
            <th>Tag</th>
            <th>Definition</th>
            <th>Examples</th>
        </tr>
        <tr>
            <td><b>Very Positive</b></td>
            <td>A sentence where the author is thanking another entity, with elaboration. This may include flowery language, extensive flattery, and 2 or more salient adjectives that describes that entity</td>
            <td>• To my mother Geetha, I cannot express in words how much I appreciate your unconditional love and support all through the years, and for the sacrifices you made to give me the best opportunities in life.</td>
        </tr>
        <tr>
            <td><b>Positive</b></td>
            <td>A sentence where the author is thanking another entity, with some elaboration. This may include adjectives that are vague, or less salient to describe the entity</td>
            <td>• First and foremost, I thank my advisor Prof. Roy Campbell for his faith in my abilities and for always finding the financial resources to fund my research.</td>
        </tr>
        <tr>
            <td><b>Neutral</b></td>
            <td>A sentence where the author is simply thanking another entity, without any elaboration or further description</td>
            <td>• This work was supported by a Bell Labs Graduate Research Fellowship.</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)
