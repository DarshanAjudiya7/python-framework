import streamlit as st
from datetime import date

st.title("Age alculator")
st.subheader("Calculate your age with using this calculator")
st.write("Enter your birth date...")

date_selected = st.date_input(
    "Pick a date :",
    min_value=date(2001, 1, 1),
)

today = date.today()  
date_display = today - date_selected

st.write("Today's date:", date.today())
st.write("You selected:", date_selected)
st.write("You are", date_display.days, "days old")

date_display = date.today() - date_selected
minutes_old = date_display.total_seconds() / 60
hours_old = date_display.total_seconds() / 3600

st.write("You are", int(hours_old), "hours old")
st.write("You are", int(minutes_old), "minutes old")

