import streamlit as st
import requests

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbyuVZuWUlZQTOkDyp4NlDwUTmAsj23ny5zofsF6i6GAKpqxDbhYPB5Co_cSpNaeec0z4g/exec"

st.set_page_config(
    page_title="ResumeRefresh",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BG_IMAGE_URL = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80"

st.markdown(f"""
<style>

.stApp {{
    background: url("{BG_IMAGE_URL}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.45);
    z-index: -1;
}}

#MainMenu {{
    visibility:hidden;
}}

header {{
    visibility:hidden;
}}

footer {{
    visibility:hidden;
}}

[data-testid="stToolbar"] {{
    display:none;
}}

[data-testid="stDecoration"] {{
    display:none;
}}

[data-testid="stStatusWidget"] {{
    display:none;
}}

.block-container {{
    padding-top:0rem;
    padding-left:0rem;
    padding-right:0rem;
    max-width:100%;
}}

[data-testid="stAppViewContainer"]>.main {{
    padding-top:0rem;
}}

.title-container {{
    width:100%;
    display:flex;
    justify-content:center;
    margin-top:20px;
}}

.title {{
    color:#000;
    font-size:72px;
    font-weight:900;
    font-family:Arial,Helvetica,sans-serif;
    letter-spacing:1px;

    text-shadow:
        -3px -3px 0 #fff,
         3px -3px 0 #fff,
        -3px  3px 0 #fff,
         3px  3px 0 #fff,
         0px -3px 0 #fff,
         0px  3px 0 #fff,
        -3px  0px 0 #fff,
         3px  0px 0 #fff;
}}

.free-badge {{
    width:fit-content;
    margin:18px auto 28px auto;
    padding:12px 28px;
    border-radius:50px;

    background:linear-gradient(135deg,#16a34a,#22c55e);

    color:white;
    font-size:22px;
    font-weight:800;
    font-family:Arial,Helvetica,sans-serif;

    box-shadow:0 10px 30px rgba(0,0,0,.30);
}}

.info-box {{
    width:82%;
    margin:auto;
    background:rgba(0,0,0,.28);

    backdrop-filter:blur(18px);
    -webkit-backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.20);
    border-radius:20px;

    padding:35px 40px;

    color:white;

    box-shadow:0 8px 25px rgba(0,0,0,.25);
}}

.info-box h2 {{
    margin-top:0;
    margin-bottom:20px;
    text-align:center;
    font-size:34px;
}}

.info-box p {{
    font-size:19px;
    line-height:1.8;
    text-align:justify;
    color:#F5F5F5;
}}

.video-container {{
    width:82%;
    height:600px;
    margin:35px auto;

    background:rgba(0,0,0,.25);

    backdrop-filter:blur(18px);

    border-radius:20px;

    overflow:hidden;

    border:1px solid rgba(255,255,255,.15);

    box-shadow:0 8px 25px rgba(0,0,0,.25);
}}

.video-container iframe {{
    width:100%;
    height:100%;
    border:none;
}}

.section-title {{
    text-align:center;
    color:white;
    font-size:38px;
    font-weight:800;
    margin-bottom:35px;
}}

.benefits-wrapper{{
    width:82%;
    margin:45px auto;
}}

.benefits-grid{{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:25px;
}}

.benefit-card{{
    background:rgba(255,255,255,.10);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.15);

    border-radius:20px;

    padding:28px;

    color:white;

    text-align:center;

    transition:.25s;
}}

.benefit-card:hover{{
    transform:translateY(-6px);
    background:rgba(255,255,255,.15);
}}

.benefit-icon{{
    font-size:42px;
    margin-bottom:14px;
}}

.benefit-title{{
    font-size:22px;
    font-weight:700;
    margin-bottom:12px;
}}

.benefit-text{{
    font-size:16px;
    line-height:1.7;
    color:#ECECEC;
}}

.button-container {{
    width:82%;
    margin:40px auto 70px auto;
    display:flex;
    justify-content:center;
}}

.signin-btn {{
    display:inline-flex;
    justify-content:center;
    align-items:center;

    width:33%;
    min-width:320px;
    height:70px;

    text-decoration:none;

    background:rgba(0,0,0,.35);

    backdrop-filter:blur(18px);

    border:2px solid white;

    border-radius:18px;

    color:white;

    font-size:24px;

    font-weight:700;

    transition:.25s;
}}

.signin-btn:hover{{
    background:rgba(255,255,255,.15);
    transform:scale(1.03);
}}

.footer {{
    text-align:center;
    color:rgba(255,255,255,.75);
    font-size:15px;
    padding:30px 0 15px 0;
}}

@media(max-width:900px){{

.title{{
    font-size:48px;
}}

.info-box{{
    width:94%;
    padding:25px;
}}

.video-container{{
    width:94%;
    height:320px;
}}

.benefits-wrapper{{
    width:94%;
}}

.benefits-grid{{
    grid-template-columns:1fr;
}}

}}

</style>
""", unsafe_allow_html=True)

if st.button(
    "🔑 Sign In to ResumeRefresh",
    key="signin_top",
    use_container_width=True,
):
    st.switch_page("pages/1_Sign_Up.py")

st.markdown("""
<div class="title-container">
    <div class="title">
        ResumeRefresh
    </div>
</div>

<div class="free-badge">
🎉 100% FREE Chrome Extension
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Demo Video (Moved to Top)
# ---------------------------------------------------------

st.markdown("""
<div class="video-container">
    <iframe
        src="https://drive.google.com/file/d/1iRTUmA8HIrFFF0e5GPoR8Gl6voH3RJ-7/preview"
        allow="autoplay"
        allowfullscreen>
    </iframe>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# About ResumeRefresh
# ---------------------------------------------------------

st.markdown("""
<div class="info-box">

<h2>About ResumeRefresh</h2>

<p>
<strong>ResumeRefresh</strong> is a <strong>100% FREE Chrome extension</strong> that automatically tailors your resume for every job application in just a few seconds.
</p>

<p>
Instead of editing your resume manually for every application, simply upload your latest resume, paste the job description, and let AI optimize your resume using your complete career profile, including your education, skills, certifications, projects, work experience, and achievements.
</p>

<p>
Every modification is fully transparent. ResumeRefresh displays your original and optimized resumes side by side, allowing you to review every change before downloading the final version.
</p>

<p>
The extension also provides an ATS compatibility score, helping you understand how well your resume matches the job description before you apply.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Benefits Section
# ---------------------------------------------------------

st.markdown("""
<div class="benefits-wrapper">

<h2 class="section-title">
Why Use ResumeRefresh?
</h2>

<div class="benefits-grid">

<div class="benefit-card">
<div class="benefit-icon">⚡</div>
<div class="benefit-title">
Tailored Resume in Seconds
</div>
<div class="benefit-text">
Generate a resume customized for every job description within seconds without manually editing your resume.
</div>
</div>

<div class="benefit-card">
<div class="benefit-icon">🧠</div>
<div class="benefit-title">
AI Career Profile
</div>
<div class="benefit-text">
Store your education, projects, certifications, skills, achievements and work experience once and reuse them forever.
</div>
</div>

<div class="benefit-card">
<div class="benefit-icon">📈</div>
<div class="benefit-title">
ATS Score Checker
</div>
<div class="benefit-text">
Instantly compare the ATS compatibility score of your original resume and your optimized resume before applying.
</div>
</div>

<div class="benefit-card">
<div class="benefit-icon">🔍</div>
<div class="benefit-title">
Side-by-Side Comparison
</div>
<div class="benefit-text">
Review every AI modification with your old and updated resumes displayed together for complete transparency.
</div>
</div>

<div class="benefit-card">
<div class="benefit-icon">💡</div>
<div class="benefit-title">
Transparent AI Changes
</div>
<div class="benefit-text">
Every keyword, project, skill and resume section updated by the AI is explained so you always know why changes were made.
</div>
</div>

<div class="benefit-card">
<div class="benefit-icon">🎉</div>
<div class="benefit-title">
Completely Free
</div>
<div class="benefit-text">
ResumeRefresh is completely free to use, allowing you to create job-specific resumes without paying subscription fees.
</div>
</div>

</div>

</div>
""", unsafe_allow_html=True)



# ---------------------------------------------------------
# How to Use
# ---------------------------------------------------------

st.markdown("""
<div class="info-box">

<h2>🚀 How to Use ResumeRefresh</h2>

<p>1️⃣ <strong>Sign in</strong> to the ResumeRefresh Chrome extension.</p>

<p>2️⃣ <strong>Complete your AI career profile</strong> by sharing your LinkedIn profile, latest resume, education, projects, certifications, skills and work experience.</p>

<p>3️⃣ <strong>Open any job application</strong> and copy the complete job description.</p>

<p>4️⃣ <strong>Paste</strong> the job description into ResumeRefresh.</p>

<p>5️⃣ <strong>Upload</strong> your latest resume.</p>

<p>6️⃣ Click <strong>Submit</strong> and let AI optimize your resume in seconds.</p>

<p>7️⃣ Review your original and optimized resumes side by side, check the ATS score, understand every AI change, and download your final resume.</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Bottom Sign In Button
# ---------------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button(
    "🔑 Sign In to ResumeRefresh",
    key="signin_bottom",
    use_container_width=True,
):
    st.switch_page("pages/1_Sign_Up.py")


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(
        """
        <div class="footer">
            © 2026 ResumeRefresh • Built by Yuvraj
        </div>
        """,
        unsafe_allow_html=True,
    )