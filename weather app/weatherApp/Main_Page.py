import os
import django
import requests
import streamlit as st

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weatherApp.settings")
try:
  django.setup()
except Exception:
  pass

from myapp.models import SearchHistory

st.title("Weather App",text_alignment="center", anchor=False)
st.subheader("Please make a selection below!", text_alignment="center", anchor=False)

#making the buttons bigger
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    div.stButton > button {
        padding: 15px 100px !important;
        border-radius: 10px !important;
    }
    div.stButton > button p {
        font-size: 24px !important;     /* Target the inner text tag */
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#buttons to switch to different page
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    if st.button(label="Weather of Location", type="primary", use_container_width=True):
        st.switch_page("pages/1_Weather_of_Location.py")

    if st.button(label="Compare the Weather", type="primary", use_container_width=True):
        st.switch_page("pages/2_Compare_the_Weather.py")

    if st.button(label="Search History", type="primary", use_container_width=True):
        st.switch_page("pages/3_Search_History.py")
