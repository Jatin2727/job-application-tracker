import streamlit as st
import datetime
import os

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Job Application Tracker",
    page_icon="📂",
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
        background: linear-gradient(90deg, #3498db, #2980b9);
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #2980b9, #1f618d);
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
st.markdown('<div class="title">📂 Job Application Tracker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Store and Search Candidate Applications</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# Input Section
# -------------------------------------------------
candidate_id = st.text_input("🆔 Candidate ID")
name = st.text_input("👤 Candidate Name")
email = st.text_input("📧 Email")
position = st.text_input("💼 Applied Position")

st.divider()

# -------------------------------------------------
# Save Application
# -------------------------------------------------
if st.button("Save Application 📥"):

    if candidate_id.strip() == "" or name.strip() == "":
        st.error("⚠ Candidate ID and Name are required!")
    else:
        now = datetime.datetime.now()
        file_name = "Applications.txt"

        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"\nApplication Date: {now}\n")
            file.write(f"Candidate ID : {candidate_id}\n")
            file.write(f"Name : {name}\n")
            file.write(f"Email : {email}\n")
            file.write(f"Position : {position}\n")
            file.write("_" * 80 + "\n")

        st.success("Application Saved Successfully! 🎉")
        st.balloons()

st.divider()

# -------------------------------------------------
# Search Candidate by ID
# -------------------------------------------------
search_id = st.text_input("🔍 Search Candidate by ID")

if st.button("Search 🔎"):

    file_name = "Applications.txt"

    if not os.path.exists(file_name):
        st.error("No applications found!")
    else:
        found = False
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for i in range(len(lines)):
            if f"Candidate ID : {search_id}" in lines[i]:
                found = True
                st.markdown("## 📄 Candidate Details")
                st.markdown('<div class="report-card">', unsafe_allow_html=True)
                for j in range(i, i + 6):
                    if j < len(lines):
                        st.write(lines[j].strip())
                st.markdown('</div>', unsafe_allow_html=True)
                break

        if not found:
            st.error("Candidate ID not found ❌")
