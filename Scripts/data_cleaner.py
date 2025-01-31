import os
import pandas as pd

# Set paths 
home_path = os.path.dirname(os.getcwd())
data_path = home_path+r'\Data'

df = pd.read_csv(data_path+r'\STREAMLIT SAMPLE.csv', encoding='utf-8')

# Clean df for Streamlit 

# Remove unnecessary columns 
df = df[['report_num', 'status', 'ref_date', 'filed_date', 'notfiled_date', 'notfiled_reason', 'disposed_date', 'disposed_reason', 'court_num', 'agency']]
df.columns = [
    'Police Report Number',
    'Case Status',
    'Date Received',
    'Date Filed',
    'Date Not Filed',
    'Reason Not Filed',
    'Date Disposed',
    'Disposed Outcome',
    'Court Number',
    'agency'
]

df['Report Number Length'] = df['Police Report Number'].str.len()
df = df[df['Report Number Length'] >= 5]
"""df['Report Number Length'].value_counts()

len(df['Police Report Number']) # 59,778
len(df['Police Report Number'].unique()) # 53,292"""


# Map Police Agency dict 
agency = pd.read_csv(home_path+r'\Helper Files\PD Agency.csv', encoding='utf-8')
agency_dict = dict(zip(agency['Agency'],agency['PD NAME']))

df['Submitting Agency'] = df['agency'].map(agency_dict)

df = df[[
    'Police Report Number',
    'Case Status',
    'Date Received',
    'Date Filed',
    'Date Not Filed',
    'Reason Not Filed',
    'Date Disposed',
    'Disposed Outcome',
    'Court Number',
    'Submitting Agency'
]]

# Export df 

df.to_csv("JCPAO Data_01312025.csv", index=False, encoding="utf-8")
