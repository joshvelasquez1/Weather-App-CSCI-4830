import os
import django
import pandas as pd
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

if st.button("Home"):
  st.switch_page("Main_Page.py")
st.divider()

st.subheader("Search History", text_alignment="center", anchor=False)

history = SearchHistory.objects.all().order_by("-searched_at").values()
if history:
  df = pd.DataFrame(history)
  if "id" in df.columns:
    df = df.drop(columns=["id"])
  df = df.rename(
    columns={
      "location": "Location",
      "temp_min": "Min Temp °F)",
      "temp_max": "Max Temp (°F)",
      "condition": "Condition",
      "searched_at": "Date Searched",
    }
  )

  st.dataframe(df, use_container_width=True, hide_index=True)
else:
  st.info("No search history found yet. Go search for a city!")