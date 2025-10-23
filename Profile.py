import streamlit as st
import json
import os

PROFILE_FILE = "profiles.json"

def load_profiles():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_profiles(profiles):
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profiles, f, ensure_ascii=False, indent=4)

def show_profile():
    st.title("กรอกโปรไฟล์")
    
    name = st.text_input("ชื่อ")
    student_id = st.text_input("รหัสนักศึกษา")
    school = st.text_input("สถานศึกษา")
    favorite_subject = st.text_input("เรื่องที่สนใจ")
    phone = st.text_input("เบอร์โทรศัพท์")
    email = st.text_input("Email")
    address = st.text_area("ที่อยู่")  # เพิ่มช่องกรอกที่อยู่แบบหลายบรรทัด

    if st.button("บันทึกโปรไฟล์"):
        profiles = load_profiles()
        profiles[student_id] = {
            "name": name,
            "school": school,
            "favorite_subject": favorite_subject,
            "phone": phone,
            "email": email,
            "address": address
        }
        save_profiles(profiles)
        st.success("บันทึกโปรไฟล์เรียบร้อย 🎉")
