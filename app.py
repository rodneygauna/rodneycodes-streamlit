# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from pathlib import Path
import streamlit as st
from PIL import Image


# ------------------------------------------------------------------------------
# Path Settings
# ------------------------------------------------------------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# ------------------------------------------------------------------------------
# General Settings
# ------------------------------------------------------------------------------
PAGE_TITLE = "rodney.codes | Rodney Gauna"
PAGE_ICON = "random"
NAME = "Rodney Gauna"
DESCRIPTION = """
Product Manager Director, coaching Product Managers to becoming great by
building deep knowledge in their customers, products, data, business, and
market.
"""
EMAIL = "rodneygauna@gmail.com"
PHONE = "(760) 587-0052"
SOCIAL_MEDIA = {
    ":office_worker: LinkedIn": "https://linkedin.com/in/rodneygauna",
    ":octocat: GitHub": "https://github.com/rodneygauna",
    ":bird: Twitter": "https://twitter.com/rodneygauna"
}
ACCOMPLISHMENETS = {
    ":page_with_curl: Certification of User Experience Design":
        "https://www.linkedin.com/in/rodneygauna/overlay/1543527566606/single-media-viewer?type=DOCUMENT&profileId=ACoAAATBSb0B_v3DmI29CUPWAA-AtssfapyM1eE&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BsMU6JOOPT6ep%2BHC1EEzq2w%3D%3D",
    ":page_with_curl: Front End Web Development Certification":
        "https://www.linkedin.com/in/rodneygauna/overlay/1508459634274/single-media-viewer?type=DOCUMENT&profileId=ACoAAATBSb0B_v3DmI29CUPWAA-AtssfapyM1eE&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BFfPFt6M7RHCPCCfrLxCiZg%3D%3D",
    ":page_with_curl: Nationally Registered Emergency Medical Technician":
        "https://media-exp1.licdn.com/dms/image/C512DAQH7VNHiiLX7tg/profile-treasury-document-cover-images_480/0/1583793387778?e=1662328800&v=beta&t=BHv8qJhKKNE_FxrmQ2DO-GGiRDYlKYuE0wXK2We6JRY"
}
PROJECTS = {
    ":small_blue_diamond: This Website":
        "https://github.com/rodneygauna/rodneycodes-streamlit",
    ":small_blue_diamond: Originial rodney.codes Website":
        "https://github.com/rodneygauna/RodneyCodes",
    ":small_blue_diamond: WebDevAble Website":
        "https://github.com/rodneygauna/WebDevAble",
    ":small_blue_diamond: Learning SQL":
        "https://github.com/rodneygauna/palomar-CSIT150-IntroToSQL",
    ":small_blue_diamond: Learing Python":
        "https://github.com/rodneygauna/palomar-CSIT175-Python",
    ":small_blue_diamond: Skeevy - Open Source Pet Tracking Web-App":
        "https://github.com/rodneygauna/skeevy"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# ------------------------------------------------------------------------------
# Load CSS, PDF, and Profile Pic
# ------------------------------------------------------------------------------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# ------------------------------------------------------------------------------
# Hero Section
# ------------------------------------------------------------------------------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME, anchor=None)
    st.caption(DESCRIPTION)
    st.download_button(
        label=" :page_facing_up: Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":email:", EMAIL)
    st.write(":iphone:", PHONE)


# ------------------------------------------------------------------------------
# Social Links
# ------------------------------------------------------------------------------
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ------------------------------------------------------------------------------
# About
# ------------------------------------------------------------------------------
st.write("#")
st.subheader("About")
st.write("---")
st.write(
    """
I am a high-level and talented Technical Product Owner adept in User
Experience Design. I lead the Product Design function in an effort to develop
customer use cases, personas and scenarios, and interface design. Provide
leadership in requirements gathering, interactive design, user testing, and
rapid prototyping utilizing Front-End Development. Plan, implement, and
execute strategy while maintaining daily contact with the software
development group to refine and revise product specifications and
implementation details. Encourage the team to innovate within the
boundaries of market segments.
"""
)


# ------------------------------------------------------------------------------
# Skills
# ------------------------------------------------------------------------------
st.write("#")
st.subheader("Professional Skills")
st.write("---")
st.write(
    """
- :stethoscope: Electronic Health Records (EHRs), Healthcare Information Technology
- :man_technologist: Programming: HTML, CSS, JavaScript, Python, SQL, FHIR, HL7, ANSI X12
- :file_cabinet: Databases: Postgres, MongoDB, MySQL
"""
)


# ------------------------------------------------------------------------------
# Work History
# ------------------------------------------------------------------------------
st.write("#")
st.subheader("Work History")
st.write("---")


# JOB 1
st.write("**Product Director | ChiroTouch**")
st.write("March 2018 - Present")
st.write(
    """
- :small_blue_diamond: Manage a team of Senior Product Managers, Product Managers, and Product Owners.
- :small_blue_diamond: Manages, organizes, mentors, and leads product managers to achieve strategic goals for product portfolio(s).
- :small_blue_diamond: Roadmap definition - ensure it aligns with the overall company vision, revenue objectives, customer feedback, and market analysis. Evangelize the vision constantly to ensure all stakeholders are aligned, have context, and understand where we are going.
"""
)


# JOB 2
st.write("#")
st.write("**Product Director | ChiroTouch**")
st.write("March 2018 - Present")
st.write(
    """
- :small_blue_diamond: Manage a team of Senior Product Managers, Product Managers, and Product Owners.
- :small_blue_diamond: Manages, organizes, mentors, and leads product managers to achieve strategic goals for product portfolio(s).
- :small_blue_diamond: Roadmap definition - ensure it aligns with the overall company vision, revenue objectives, customer feedback, and market analysis. Evangelize the vision constantly to ensure all stakeholders are aligned, have context, and understand where we are going.
"""
)


# ------------------------------------------------------------------------------
# Accomplishments
# ------------------------------------------------------------------------------
st.write("#")
st.subheader("Accomplishments")
st.write("---")
for accomplishment, link in ACCOMPLISHMENETS.items():
    st.write(f"[{accomplishment}]({link})")


# ------------------------------------------------------------------------------
# Projects
# ------------------------------------------------------------------------------
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
