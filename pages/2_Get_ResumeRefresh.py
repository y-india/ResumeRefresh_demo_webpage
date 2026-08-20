import streamlit as st

st.set_page_config(
    page_title="Get ResumeRefresh",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(
    """
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-W79K4X5CLT"></script>

    <script>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }

        gtag('js', new Date());
        gtag('config', 'G-W79K4X5CLT');
    </script>
    """,
    unsafe_allow_javascript=True,
)


# --------------------------------------------------
# CONFIG
# --------------------------------------------------

BG = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80"

DOWNLOAD_URL = (
    "https://github.com/y-india/ResumeRefresh_Distribution/"
    "raw/refs/heads/main/ResumeRefresh_Distribution_AltShiftY.zip"
)

# --------------------------------------------------
# BACKGROUND + SIMPLE STYLING
# --------------------------------------------------

st.markdown(
    f"""
    <style>

    .stApp {{
        background: url('{BG}') center/cover fixed;
    }}

    .stApp:before {{
        content: '';
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,.48);
        z-index: -1;
    }}

    #MainMenu,
    header,
    footer,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {{
        display: none;
    }}

    .block-container {{
        max-width: 900px;
        padding: 40px 30px 60px 30px;
    }}

    h1, h2, h3, p, li {{
        color: white;
    }}

    .subtitle {{
        color: #e2e8f0;
        font-size: 20px;
        line-height: 1.5;
    }}

    .box {{
        background: rgba(255,255,255,.09);
        padding: 22px;
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,.15);
        margin-bottom: 15px;
        backdrop-filter: blur(8px);
    }}

    .box h3 {{
        margin-top: 0;
    }}

    .box p {{
        color: #e2e8f0;
        line-height: 1.5;
    }}

    .code {{
        background: rgba(0,0,0,.4);
        padding: 10px 14px;
        border-radius: 7px;
        font-family: monospace;
        color: white;
        display: inline-block;
    }}

    .center {{
        text-align: center;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown(
    """
    <div class="center">

    <h1 style="
        font-size:56px;
        font-weight:900;
        color:#000;
        text-shadow:
            -3px -3px 0 #fff,
             3px -3px 0 #fff,
            -3px  3px 0 #fff,
             3px  3px 0 #fff;
    ">
        ResumeRefresh is Ready
    </h1>

    <p class="subtitle">
        Create a personalized resume for every job application
        without manually rewriting your resume every time.
    </p>

    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")


# --------------------------------------------------
# DOWNLOAD BUTTON
# --------------------------------------------------

st.link_button(
    "⬇️ Download ResumeRefresh",
    DOWNLOAD_URL,
    use_container_width=True,
)

st.markdown(
    """
    <p class="center" style="color:#cbd5e1;">
        Free demo • Chrome Extension • Takes about 2 minutes to set up
    </p>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# BENEFITS
# --------------------------------------------------

st.header("Why Use ResumeRefresh?")

benefits = [
    (
        "1. Personalized Resume in Seconds",
        "Give ResumeRefresh your resume and a job description. It creates a version tailored to that specific job."
    ),
    (
        "2. Save Hours",
        "Stop manually editing your resume for every job application. ResumeRefresh handles the repetitive work."
    ),
    (
        "3. Better Job Description Alignment",
        "ResumeRefresh helps align your resume with relevant skills, terminology and keywords from the job description."
    ),
    (
        "4. Resume History Coming Soon",
        "A resume history system is planned for a future version so you can keep track of your customized resumes."
    ),
    (
        "5. A Working Demo",
        "This is a usable demo of ResumeRefresh. Install it and try it with a real job posting."
    ),
]

for title, description in benefits:
    st.markdown(
        f"""
        <div class="box">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# INSTALLATION
# --------------------------------------------------

st.header("How to Use ResumeRefresh")

steps = [
    (
        "Step 1: Download the ZIP",
        f"""
        Click the download button above to download ResumeRefresh.
        """
    ),
    (
        "Step 2: Extract the ZIP",
        """
        Extract the downloaded ZIP file.

        You will get a folder called
        <span class="code">ResumeRefresh</span>.
        """
    ),
    (
        "Step 3: Open Chrome Extensions",
        """
        Open Chrome and go to:

        <br><br>

        <span class="code">chrome://extensions/</span>

        <br><br>

        Turn on <b>Developer mode</b> in the upper-right corner.
        """
    ),
    (
        "Step 4: Load ResumeRefresh",
        """
        Click <b>Load unpacked</b>.

        <br><br>

        Select the <b>ResumeRefresh</b> folder you extracted.
        """
    ),
    (
        "Step 5: Find a Job",
        """
        Open a job posting you want to apply for
        and copy the complete job description.
        """
    ),
    (
        "Step 6: Open ResumeRefresh",
        """
        Press:

        <br><br>

        <span class="code">Alt + Shift + Y</span>

        <br><br>

        Sign in, paste the job description and provide your resume.
        """
    ),
    (
        "Step 7: Get Your Personalized Resume",
        """
        Wait around 2 to 3 minutes.

        <br><br>

        ResumeRefresh will generate a personalized resume
        based on the job description.
        """
    ),
]

for title, description in steps:
    st.markdown(
        f"""
        <div class="box">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# FINAL CTA
# --------------------------------------------------

st.write("")

st.markdown(
    """
    <div class="center">
        <h2>Ready to try ResumeRefresh?</h2>
        <p class="subtitle">
            Download the demo and create your first personalized resume.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.link_button(
    "⬇️ Download ResumeRefresh",
    DOWNLOAD_URL,
    use_container_width=True,
)

st.write("")

st.markdown(
    """
    <p class="center" style="color:#cbd5e1;">
        © 2026 ResumeRefresh • Built by Yuvraj
    </p>
    """,
    unsafe_allow_html=True,
)