import streamlit as st

pages = {
    "Police Report Search Tool": [
        st.Page("search_tool.py", title="Check Your Report Status Here")
    ],
    "Resources": [
        st.Page("more_info.py", title="For More Information"),
        st.Page("glossary.py", title="Glossary"),
        st.Page("jcpao_info.py", title="About the JCPAO")
    ],
}

pg = st.navigation(pages)
pg.run()