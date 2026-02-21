import streamlit as st
import datetime
import os

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Student Performance Tracker",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------------------------
# Custom CSS Styling
# -------------------------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }

    .title {
        text-align: center;
        color: #2c3e50;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #34495e;
        font-size: 18px;
    }

    .stButton>button {
        background: linear-gradient(90deg, #4CAF50, #2ecc71);
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #2ecc71, #27ae60);
        color: white;
    }

    .report-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Title Section
# -------------------------------------------------
st.markdown('<div class="title">🎓 Student Performance Tracker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter student details to generate report</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# Input Section
# -------------------------------------------------
name = st.text_input("👤 Student Name")

col1, col2, col3 = st.columns(3)

with col1:
    math = st.number_input("📘 Maths", min_value=0, max_value=100, step=1)

with col2:
    science = st.number_input("🔬 Science", min_value=0, max_value=100, step=1)

with col3:
    english = st.number_input("📖 English", min_value=0, max_value=100, step=1)

st.divider()

# -------------------------------------------------
# Generate Report Button
# -------------------------------------------------
if st.button("Generate Report 🚀"):

    if name.strip() == "":
        st.error("⚠ Please enter student name")
    else:
        average = (math + science + english) / 3

        if average >= 40:
            result_ui = "Pass ✅"
            result_file = "Pass"
            st.success("Student Passed Successfully!")
        else:
            result_ui = "Fail ❌"
            result_file = "Fail"
            st.error("Student Failed!")

        now = datetime.datetime.now()

        file_name = "Students.txt"

        # -------------------------------------------------
        # Save to File (UTF-8 FIX APPLIED HERE)
        # -------------------------------------------------
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"\nReport Generated: {now}\n")
            file.write(f"Name of Student : {name}\n")
            file.write(f"Maths : {math}\n")
            file.write(f"Science : {science}\n")
            file.write(f"English : {english}\n")
            file.write(f"Average : {average:.2f}\n")
            file.write(f"Result : {result_file}\n")
            file.write("_" * 80 + "\n")

        # -------------------------------------------------
        # Display Report Card UI
        # -------------------------------------------------
        st.markdown("## 📄 Report Card")

        st.markdown('<div class="report-card">', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("📊 Average", f"{average:.2f}")
            st.metric("🎯 Result", result_ui)

        with col2:
            st.metric("📘 Maths", math)
            st.metric("🔬 Science", science)
            st.metric("📖 English", english)

        st.markdown('</div>', unsafe_allow_html=True)

        st.balloons()

        st.success("Record Saved Successfully! 🎉")