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
# Custom CSS Styling (Improved)
# -------------------------------------------------
st.markdown("""
    <style>
    /* Background for whole page */
    .main {
        background: linear-gradient(135deg, #e0f7fa, #80deea);
        min-height: 100vh;
        padding: 2rem 1rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title styling */
    .title {
        text-align: center;
        color: #00796b;
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 0.1rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }

    /* Subtitle styling */
    .subtitle {
        text-align: center;
        color: #004d40;
        font-size: 20px;
        margin-bottom: 2rem;
        font-weight: 600;
    }

    /* Style for buttons */
    .stButton > button {
        background: linear-gradient(90deg, #00796b, #004d40);
        color: #e0f2f1;
        border-radius: 15px;
        height: 3.2em;
        width: 100%;
        font-size: 20px;
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 8px rgba(0,121,107,0.4);
        transition: background 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #004d40, #00251a);
        box-shadow: 0 6px 12px rgba(0,77,64,0.7);
    }

    /* Container for report cards */
    .report-card {
        background-color: #ffffffcc;
        padding: 25px 30px;
        border-radius: 25px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.12);
        margin-top: 1.5rem;
        color: #004d40;
        font-weight: 600;
        line-height: 1.5;
    }

    /* Input boxes styling */
    div[data-baseweb="input"] > input {
        border-radius: 15px !important;
        border: 2px solid #004d40 !important;
        padding: 12px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #004d40 !important;
        background-color: #e0f2f1 !important;
        transition: border-color 0.3s ease;
    }

    div[data-baseweb="input"] > input:focus {
        border-color: #00796b !important;
        outline: none !important;
        box-shadow: 0 0 10px #00796b88 !important;
    }

    /* Divider styling */
    .css-1emrehy.egzxvld1 {
        border-top: 2px solid #004d40 !important;
        margin: 2rem 0 !important;
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
