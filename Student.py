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

def show_student():
    st.title("ข้อมูลนักศึกษา 📚")
    
    profiles = load_profiles()
    if not profiles:
        st.warning("ยังไม่มีข้อมูลโปรไฟล์")
        return
    
    # เลือกนักเรียน
    student_ids = list(profiles.keys())
    selected_id = st.selectbox("เลือกนักศึกษา", student_ids)
    
    if selected_id:
        profile = profiles[selected_id]
        
        # แสดงข้อมูลปัจจุบัน
        st.write("**ข้อมูลปัจจุบัน**")
        st.write(f"**ชื่อ:** {profile.get('name','')}")
        st.write(f"**โรงเรียน:** {profile.get('school','')}")
        st.write(f"**เรื่องที่สนใจ:** {profile.get('favorite_subject','ยังไม่ได้ระบุ')}")
        st.write(f"**เบอร์โทรศัพท์:** {profile.get('phone','')}")
        st.write(f"**Email:** {profile.get('email','')}")
        st.write(f"**ที่อยู่:** {profile.get('address','')}")
        
        st.write("---")
        st.subheader("แก้ไขข้อมูลนักศึกษา")
        new_name = st.text_input("ชื่อใหม่", value=profile.get('name',''))
        new_school = st.text_input("โรงเรียนใหม่", value=profile.get('school',''))
        new_subject = st.text_input("เรื่องที่สนใจใหม่", value=profile.get('favorite_subject',''))
        new_phone = st.text_input("เบอร์โทรศัพท์ใหม่", value=profile.get('phone',''))
        new_email = st.text_input("Email ใหม่", value=profile.get('email',''))
        new_address = st.text_area("ที่อยู่ใหม่", value=profile.get('address',''))
        
        col1, col2 = st.columns(2)
        
        # ปุ่มบันทึก
        with col1:
            if st.button("บันทึกการแก้ไข"):
                profiles[selected_id] = {
                    "name": new_name,
                    "school": new_school,
                    "favorite_subject": new_subject,
                    "phone": new_phone,
                    "email": new_email,
                    "address": new_address
                }
                save_profiles(profiles)
                st.session_state['selected_student'] = profiles[selected_id]
                st.success("แก้ไขโปรไฟล์เรียบร้อย 🎉")
        
        # ปุ่มลบแบบสองขั้นตอน
        if 'confirm_delete' not in st.session_state:
            st.session_state['confirm_delete'] = False

        with col2:
            if not st.session_state['confirm_delete']:
                if st.button("ลบโปรไฟล์"):
                    st.session_state['confirm_delete'] = True
            else:
                if st.button("ยืนยันการลบ"):
                    profiles.pop(selected_id)
                    save_profiles(profiles)
                    if 'selected_student' in st.session_state:
                        del st.session_state['selected_student']
                    st.session_state['confirm_delete'] = False
                    st.success("ลบโปรไฟล์นักศึกษานี้เรียบร้อย 🎉")
