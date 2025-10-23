import streamlit as st
import json
import os

PROFILE_FILE = "profiles.json"

def load_profiles():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def show_home():
    st.set_page_config(page_title="Home", page_icon="🏠")
    st.title("ยินดีต้อนรับสู่ Multipage App 🎉")
    
    profiles = load_profiles()
    if not profiles:
        st.warning("ยังไม่มีข้อมูลนักศึกษา กรุณาไปสร้างโปรไฟล์ที่หน้า Profile")
        return
    
    student_ids = list(profiles.keys())
    selected_id = st.selectbox("เลือกนักศึกษา", student_ids)
    
    if selected_id:
        st.session_state['selected_student'] = profiles[selected_id]
    
    if 'selected_student' in st.session_state:
        student = st.session_state['selected_student']
        
        st.markdown(
            f"""
            <div style="background-color:#cce6ff; padding:20px; border-radius:10px; box-shadow: 2px 2px 5px #aaa; color:#000;">
                <h2>{student.get('name','')} 👋</h2>
                <p><b>กำลังศึกษาอยู่ที่:</b> {student.get('school','')}</p>
                <p><b>เรื่องที่สนใจ:</b> {student.get('favorite_subject','ยังไม่ได้ระบุ')}</p>
                <p><b>เบอร์โทรศัพท์:</b> {student.get('phone','')}</p>
                <p><b>Email:</b> {student.get('email','')}</p>
                <p><b>ที่อยู่:</b> {student.get('address','')}</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.info("สามารถไปที่หน้า Subject เพื่อบันทึกเรื่องที่สนใจ หรือแก้ไขข้อมูลในหน้า Student")
