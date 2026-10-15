import os
import django
from myapp.models import SearchHistory
import requests
import streamlit as st

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weatherApp.settings")
try:
  django.setup()
except Exception:
  pass

#removes sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#home button
if st.button("Home", type="primary"):
  st.switch_page("Main_Page.py")
st.divider()

#get City or ZIP code to gather information
st.subheader("Want to know the weather?", text_alignment="center", anchor=False)
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    location_input = st.text_input("Please enter a City or ZIP Code below!", placeholder="Omaha", label_visibility="visible")

    if st.button("Get weather!", type="primary"):
        appid = "7be3619db7fadee15790446e998a140f"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location_input}&units=imperial&APPID={appid}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            #assign information
            location = data["name"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            condition = data["weather"][0]["main"]

            #display information
            st.subheader(f"Weather in {location}", text_alignment="center", anchor=False)
            st.subheader(f"Condition is {condition}", text_alignment="center", anchor=False)
            st.subheader(f"With a high of {temp_max}°F, and a low of {temp_min}°F",text_alignment="center", anchor=False)

            #save to DJango Database
            try:
                SearchHistory.objects.create(
                    location=location,
                    temp_min=temp_min,
                    temp_max=temp_max,
                    condition=condition,
            )
            except Exception as e:
                st.error(f"Failed to save to database: {e}")

        else:
            st.error("City not found. Please check the spelling.")
