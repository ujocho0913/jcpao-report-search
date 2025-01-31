import streamlit as st
import pandas as pd
import os

# Set paths
home_path = os.getcwd()
logo_path = home_path+r'\Logos'


# st.image("Logos\jcpo logo_medium.png")
st.title("Enter your Police Report Number")
st.caption("Results based on system data as of 2025-01-28")

df = pd.read_csv("Data\JCPAO Data_01312025.csv", encoding='utf-8')

report_number = st.text_input("")

if st.button("Search"):
    if len(report_number) >= 5: 
        result = df[df['Police Report Number'].str.contains(report_number, case=False, na=False)]
        if not result.empty:
            total_cases = len(result)
            st.write(f"We found {total_cases} case(s) associated with Police Report *#{report_number}*:")
            for i, row in result.iterrows():
                
                st.write(f"Case {i} has a status of :red[**{row['Case Status'].upper()}**]")
            
            # st.dataframe(result)
        else:
            st.write("We could not match your Police Report Number with any cases submitted to our Office. This means the reported incident is still under investigation and has yet to be submitted to our Office or the incident has been submitted to another jurisdiction (e.g., municipal or federal court).")
    else:
        st.write("*Your report number must be at least five characters long.*")

st.write("If your case was filed by our Office, you can find the latest information regarding the case on CaseNet [here](https://www.courts.mo.gov/cnet/caseNoSearch.do).")

