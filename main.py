import streamlit as st
from Home import show_home
from Profile import show_profile
from Student import show_student

st.set_page_config(page_title="Multipage App", page_icon="📝")

st.sidebar.title("เลือกหน้า")
page = st.sidebar.radio("ไปที่หน้า", ["Home", "Profile", "Student"])

if page == "Home":
    show_home()
elif page == "Profile":
    show_profile()
elif page == "Student":
    show_student()
