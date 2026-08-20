import streamlit as st

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ResumeRefresh",
    layout="wide",
    initial_sidebar_state="collapsed",
)



st.markdown(
    """
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-W79K4X5CLT"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-W79K4X5CLT');
    </script>
    """,
    unsafe_allow_html=True,
)






BG = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80"

VIDEO = "https://drive.google.com/file/d/1iRTUmA8HIrFFF0e5GPoR8Gl6voH3RJ-7/preview"

BENEFITS = [
    (
        "⚡",
        "Tailored Resume in Seconds",
        "Generate a resume customized for every job description within seconds without manually editing your resume."
    ),
    (
        "🧠",
        "AI Career Profile",
        "Store your education, projects, certifications, skills, achievements and work experience once and reuse them forever."
    ),
    (
        "📈",
        "ATS Score Checker",
        "Instantly compare the ATS compatibility score of your original resume and your optimized resume before applying."
    ),
    (
        "🔍",
        "Side-by-Side Comparison",
        "Review every AI modification with your old and updated resumes displayed together for complete transparency."
    ),
    (
        "💡",
        "Transparent AI Changes",
        "Every keyword, project, skill and resume section updated by the AI is explained so you always know why changes were made."
    ),
    (
        "🎉",
        "Completely Free",
        "ResumeRefresh is completely free to use, allowing you to create job-specific resumes without paying subscription fees."
    ),
]
CSS = f"""
<style>

.stApp{{
background:url('{BG}') center/cover fixed;
}}

.stApp:before{{
content:'';
position:fixed;
inset:0;
background:rgba(0,0,0,.45);
z-index:-1;
}}

#MainMenu,header,footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"]{{
display:none;
}}

.block-container{{
padding:2rem 4rem;
}}

.glass{{
background:rgba(255,255,255,.08);
padding:25px;
border-radius:18px;
backdrop-filter:blur(12px);
border:1px solid rgba(255,255,255,.15);
margin-bottom:25px;
}}

.badge{{
display:inline-block;
padding:8px 18px;
background:#16a34a;
color:white;
border-radius:30px;
font-weight:bold;
}}

h1,h2,h3,p,li{{
color:white;
}}

.footer{{
text-align:center;
opacity:.7;
padding:25px;
}}

iframe{{
width:100%;
height:600px;
border:none;
border-radius:18px;
}}

</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def get_resumerefresh(key):
    if st.button(
        "⬇️ Get ResumeRefresh",
        key=key,
        use_container_width=True,
    ):
        st.switch_page("pages/2_Get_ResumeRefresh.py")



def signin(key):
    if st.button(
        "🔑 Sign In to ResumeRefresh",
        key=key,
        use_container_width=True,
    ):
        st.switch_page("pages/1_Sign_Up.py")


def video():
    st.markdown(
        f"""
        <iframe
        src="{VIDEO}"
        allow="autoplay"
        allowfullscreen>
        </iframe>
        """,
        unsafe_allow_html=True,
    )


def card(icon, title, text):
    with st.container(border=True):
        st.markdown(f"### {icon} {title}")
        st.write(text)


# --------------------------------------------------
# TOP OF PAGE
# --------------------------------------------------

get_resumerefresh("top_get_resumerefresh")

st.markdown("""
<style>
.title{
    text-align:center;
    font-size:68px;
    font-weight:900;
    font-family:Arial,Helvetica,sans-serif;
    color:#000;
    margin-bottom:8px;

    text-shadow:
        -3px -3px 0 #fff,
         3px -3px 0 #fff,
        -3px  3px 0 #fff,
         3px  3px 0 #fff,
         0px -3px 0 #fff,
         0px  3px 0 #fff,
        -3px  0px 0 #fff,
         3px  0px 0 #fff;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">ResumeRefresh</div>',
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='badge'>🎉 100% FREE Chrome Extension</div>",
    unsafe_allow_html=True,
)

st.write("")

video()


# --------------------------------------------------
# ABOUT
# --------------------------------------------------

st.markdown("## About ResumeRefresh")

with st.container(border=True):
    st.markdown("""
ResumeRefresh is a **100% FREE Chrome extension** that automatically tailors
your resume for every job application.

Instead of editing your resume manually for every application, simply upload
your latest resume, paste the job description, and let AI optimize your resume
using your complete career profile.

You'll be able to:

- Compare your original and optimized resumes side by side.
- Review every AI change before downloading.
- Check your ATS compatibility score.
- Create job-specific resumes in seconds.
""")

st.write("")

# --------------------------------------------------
# BENEFITS
# --------------------------------------------------

st.markdown("## Why Use ResumeRefresh?")

cols = st.columns(2)

for i, benefit in enumerate(BENEFITS):
    icon, title, text = benefit
    with cols[i % 2]:
        card(icon, title, text)

st.write("")
st.divider()

# --------------------------------------------------
# HOW TO USE
# --------------------------------------------------

st.markdown("## 🚀 How to Use")

steps = [
    "Sign in to ResumeRefresh.",
    "Complete your AI Career Profile.",
    "Open a job application.",
    "Copy the complete job description.",
    "Paste the job description into ResumeRefresh.",
    "Upload your latest resume.",
    "Click Submit and let AI optimize your resume.",
    "Review the optimized resume, compare ATS scores, and download it."
]

for i, step in enumerate(steps, 1):
    st.markdown(f"**{i}.** {step}")

st.write("")
st.divider()

st.write("")
get_resumerefresh("bottom_get_resumerefresh")
st.write("")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
<div class="footer">
© 2026 ResumeRefresh • Built by Yuvraj
</div>
""",
    unsafe_allow_html=True,
)




