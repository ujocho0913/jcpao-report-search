import streamlit as st
import pandas as pd
import os

# Set paths
home_path = os.getcwd()
logo_path = home_path+r'\Logos'


st.image("Logos\jcpo logo_medium.png")
st.title("Police Report Search Tool")
st.caption("Jackson County Prosecuting Attorney's Office")

df = pd.read_csv("STREAMLIT SAMPLE.csv", encoding='utf-8')

report_number = st.text_input("Enter your Police Report Number")

if st.button("Search"):
    result = df[df['report_num'].str.contains(report_number, case=False, na=False)]
    if not result.empty:
        total_cases = len(result)
        st.write(f"We found {total_cases} case(s) associated with Police Report *#{report_number}*:")
        for i, row in result.iterrows():
            
            st.write(f"Case {i} has a status of :red[**{row['status'].upper()}**]")
        
        st.dataframe(result)
    else:
        st.write("We could not match your Police Report Number with any cases submitted to our Office. This means that (a) the reported incident is still under investigation and has yet to be submitted to our Office or (b) the incident has been submitted to another jurisdiction (e.g., municipal or federal court).")

st.write("If your case was filed by our Office, you can find the latest information regarding the case on CaseNet [here](https://www.courts.mo.gov/cnet/caseNoSearch.do).")
