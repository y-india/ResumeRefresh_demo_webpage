import streamlit as st
import requests

# -------------------------------
# Google Apps Script Web App URL
# -------------------------------
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbyuVZuWUlZQTOkDyp4NlDwUTmAsj23ny5zofsF6i6GAKpqxDbhYPB5Co_cSpNaeec0z4g/exec"

st.set_page_config(
    page_title="ResumeRefresh | Sign Up",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# Background
# -------------------------------
st.markdown("""
<style>

.stApp {
    background: url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    z-index: -1;
}

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

[data-testid="stToolbar"]{
    display:none;
}

[data-testid="stDecoration"]{
    display:none;
}

[data-testid="stStatusWidget"]{
    display:none;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# UI
# -------------------------------
st.title("ResumeRefresh")

st.markdown("### Sign Up")

with st.form("signup_form"):

    name = st.text_input("👤 Full Name")

    email = st.text_input("📧 Email Address")

    profession = st.selectbox(
        "💼 Profession",
        [
            "Student",
            "Job Seeker",
            "Working Professional",
            "Senior Professional"
        ]
    )

    watched_demo = st.radio(
        "🧐 Have you watched the demo video?",
        ["Yes", "No"]
    )

    linkedin = st.text_input("🔗 LinkedIn Profile (Optional)")

    submit = st.form_submit_button("Submit")

# -------------------------------
# Submit
# -------------------------------
if submit:

    if not name.strip() or not email.strip():

        st.error("Please fill all required fields.")

    else:

        payload = {
            "full_name": name,
            "email": email,
            "profession": profession,
            "demo_video": watched_demo,
            "linkedin": linkedin
        }

        try:

            response = requests.post(
                WEB_APP_URL,
                json=payload,
                timeout=10
            )

            if response.status_code == 200:

                st.success("✅ Details Submitted!")

                st.info("""
### ResumeRefresh is currently under development.

Thank you for your interest!

We will provide you with additional turns to convert your resume.

We are actively working on ResumeRefresh and will make it available soon.

We will notify you as soon as early access is ready.
""")

                st.balloons()

            else:

                st.error(f"Submission failed. Status Code: {response.status_code}")

        except Exception as e:

            st.error(f"Error: {e}")

# -------------------------------
# Back Button
# -------------------------------
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")