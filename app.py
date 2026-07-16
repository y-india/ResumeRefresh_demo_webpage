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
    background: rgba(0, 0, 0, 0.45);
    z-index: -1;
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
<style>

/* ------------------------------------------------ */
/* Hide Streamlit UI */
/* ------------------------------------------------ */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stStatusWidget"] {
    display: none;
}

/* ------------------------------------------------ */
/* Remove default Streamlit spacing */
/* ------------------------------------------------ */

.block-container {
    padding-top: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
    max-width: 100%;
}

[data-testid="stAppViewContainer"] > .main {
    padding-top: 0rem;
}

/* ------------------------------------------------ */
/* Title */
/* ------------------------------------------------ */

.title-container {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 18px;
    margin-bottom: 30px;
}

.title {
    color: #000;
    font-size: 72px;
    font-weight: 900;
    font-family: Arial, Helvetica, sans-serif;
    letter-spacing: 1px;

    /* Thick white outline */
    text-shadow:
        -3px -3px 0 #fff,
         3px -3px 0 #fff,
        -3px  3px 0 #fff,
         3px  3px 0 #fff,
         0px -3px 0 #fff,
         0px  3px 0 #fff,
        -3px  0px 0 #fff,
         3px  0px 0 #fff,
        -2px -2px 0 #fff,
         2px -2px 0 #fff,
        -2px  2px 0 #fff,
         2px  2px 0 #fff;
}
/* ------------------------------------------------ */
/* Information Box */
/* ------------------------------------------------ */
.info-box {
    width: 82%;
    margin: auto;

    /* More transparent */
    background: rgba(0, 0, 0, 0.28);

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    border: 1px solid rgba(255,255,255,0.20);
    border-radius: 20px;

    padding: 35px 40px;

    color: white;

    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
}

.info-box h2{
    margin-top:0;
    margin-bottom:20px;
    text-align:center;
    font-size:34px;
    color:white;
}

.info-box p{
    font-size:19px;
    line-height:1.8;
    text-align:justify;
    color:#F5F5F5;
}


            /* ------------------------------------------------ */
/* Video */
/* ------------------------------------------------ */

.video-container {
    width: 82%;
    height: 600px;
    margin: 35px auto 50px auto;

    background: rgba(0,0,0,0.25);
    backdrop-filter: blur(18px);

    border-radius: 20px;
    overflow: hidden;

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
}

.video-container iframe {
    width: 100%;
    height: 100%;
    border: none;
}

/* ------------------------------------------------ */
/* Sign In Button */
/* ------------------------------------------------ */

.button-container {
    width: 82%;
    margin: 40px auto 70px auto;
    display: flex;
    justify-content: center;
}

.signin-btn {
    display: inline-flex;
    justify-content: center;
    align-items: center;

    width: 33%;
    min-width: 320px;
    height: 70px;

    text-decoration: none;

    background: rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(18px);

    border: 2px solid white;
    border-radius: 18px;

    color: white;
    font-size: 24px;
    font-weight: 700;
    font-family: Arial, Helvetica, sans-serif;

    transition: all 0.25s ease;
}

.signin-btn:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: scale(1.03);
    box-shadow: 0 0 20px rgba(255,255,255,0.35);
}    

.footer {
    text-align: center;
    color: rgba(255, 255, 255, 0.75);
    font-size: 15px;
    padding: 30px 0 15px 0;
    font-family: Arial, Helvetica, sans-serif;
}
            
/* ------------------------------------------------ */
/* Responsive */
/* ------------------------------------------------ */

@media (max-width:900px){

.title{
    font-size:46px;
}

.info-box{
    width:94%;
    padding:25px;
}

.info-box p{
    font-size:16px;
}

}

</style>

<div class="title-container">
    <div class="title">
        ResumeRefresh
    </div>
</div>

<div class="info-box">

<h2>About ResumeRefresh</h2>

<p>
<strong>ResumeRefresh</strong> is a Chrome extension that updates your resume for every job application in just a few seconds. It uses your full education and career details, including your school, college, degree, certificates, skills, work experience, and projects.
</p>

<p>
Just paste the job description, and ResumeRefresh will update your resume to match the job. This saves you from editing your resume manually for every application.
</p>

<p>
The extension also shows your old and new resumes side by side, so you can easily see every change. If you want to keep, remove, or edit any change, you can do it instantly before downloading your resume.
<p>
            
<p>
It also includes a built in ATS score checker. You can quickly check the ATS score of both your original and updated resumes before applying.
</p>

</div>

            
""", unsafe_allow_html=True)




st.markdown("""
<div class="video-container">
    <iframe
        src="https://drive.google.com/file/d/1iRTUmA8HIrFFF0e5GPoR8Gl6voH3RJ-7/preview"
        allow="autoplay"
        allowfullscreen>
    </iframe>
</div>
""", unsafe_allow_html=True)



st.markdown("""
<div class="info-box">

<h2>🚀 How to Use ResumeRefresh</h2>

<p>1️⃣ <strong>Sign in</strong> to the ResumeRefresh Chrome extension.</p>

<p>2️⃣ <strong>Complete the chat interview</strong> by sharing your LinkedIn profile, latest resume, and other requested details.</p>

<p>3️⃣ <strong>Open a job application</strong> and copy the job description.</p>

<p>4️⃣ <strong>Paste</strong> the job description into the extension. 📋</p>

<p>5️⃣ <strong>Upload</strong> your latest resume. 📄</p>

<p>6️⃣ Click the <strong>Submit</strong> button. ⚡</p>

<p>7️⃣ Review your optimized resume, side by side comparison, and ATS score. 🎉</p>

</div>
""", unsafe_allow_html=True)




if st.button(
    "🔑 Sign In to ResumeRefresh",
    key="signin_bottom",
    use_container_width=True,
):
    st.switch_page("pages/1_Sign_Up.py")







col10, col11, col12 = st.columns([1, 2, 1])

with col11:
    st.markdown(
        """
        <div class="footer">
            © 2026 ResumeRefresh • Built by Yuvraj
        </div>
        """,
        unsafe_allow_html=True,
    )