import os
import django
import requests
import streamlit as st
from myapp.models import SearchHistory

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
if st.button("Home"):
  st.switch_page("Main_Page.py")
st.divider()

#get City or ZIP code to gather information
st.subheader("Please enter both Cities or ZIP Codes below!", text_alignment="center")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
	location_input_first = st.text_input("City 1", placeholder="Omaha", label_visibility="visible")
	appid = "7be3619db7fadee15790446e998a140f"
	url1 = f"https://api.openweathermap.org/data/2.5/weather?q={location_input_first}&units=imperial&APPID={appid}"

with col3:
	location_input_second = st.text_input("City 2", placeholder="Lincoln", label_visibility="visible")
	appid = "7be3619db7fadee15790446e998a140f"
	url2 = f"https://api.openweathermap.org/data/2.5/weather?q={location_input_second}&units=imperial&APPID={appid}"

st.write("")
b_col1, b_col2, b_col3 = st.columns([1, 1, 1])

with b_col2:
	submit = st.button("Get weather!", type="primary", use_container_width=True)

if submit:
	response1 = requests.get(url1)
	response2 = requests.get(url2)
	with col1:
		if response1.status_code == 200:
			data = response1.json()
			#assign information
			location1 = data["name"]
			temp_min1 = data["main"]["temp_min"]
			temp_max1 = data["main"]["temp_max"]
			condition1 = data["weather"][0]["main"]

			#display information
			st.subheader(f"Weather in {location1}", text_alignment="center", anchor=False)
			st.subheader(f"Condition is {condition1}", text_alignment="center", anchor=False)
			st.subheader(f"With a high of {temp_max1}°F, and a low of {temp_min1}°F",text_alignment="center", anchor=False)

			#save to Django
			try:
				SearchHistory.objects.create(
					location=location1,
					temp_min=temp_min1,
					temp_max=temp_max1,
					condition=condition1,
        		)
			except Exception as e:
				st.error(f"Failed to save City 1 to database: {e}")

		else:
			st.error("City 1 not found.")

	with col3:
		if response2.status_code == 200:
			data = response2.json()
			#assign information
			location2 = data["name"]
			temp_min2 = data["main"]["temp_min"]
			temp_max2 = data["main"]["temp_max"]
			condition2 = data["weather"][0]["main"]

			#display information
			st.subheader(f"Weather in {location2}", text_alignment="center", anchor=False)
			st.subheader(f"Condition is {condition2}", text_alignment="center", anchor=False)
			st.subheader(f"With a high of {temp_max2}°F, and a low of {temp_min2}°F",text_alignment="center", anchor=False)

			#save to Django
			try:
				SearchHistory.objects.create(
					location=location2,
					temp_min=temp_min2,
					temp_max=temp_max2,
					condition=condition2,
        		)
			except Exception as e:
				st.error(f"Failed to save City 2 to database: {e}")

		else:
			st.error("City 2 not found.")
			