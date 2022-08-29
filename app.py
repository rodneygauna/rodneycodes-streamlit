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
    ":office: LinkedIn": "https://linkedin.com/in/rodneygauna",
    "👩‍💻 GitHub": "https://github.com/rodneygauna",
    ":bird: Twitter": "https://twitter.com/rodneygauna"
}
SKILLS = [
    ":office: Product Management: Research customer needs, product vision and roadmap, strategy for development, creating sales and marketing objectives, leading and coaching a team of Product Managers",
    ":ambulance: Medical: Electronic Health Records (EHRs), Healthcare Information Technology",
    "👩‍💻 Programming: HTML, CSS, JavaScript, Python, SQL, FHIR, HL7, ANSI X12",
    ":file_cabinet: Databases: Postgres, MongoDB, MySQL"
]
USECASES = {
    ":crystal_ball: Business Case - An Example":
        "#",
    ":floppy_disk: UX Use Case - Blizzard Gear Store":
        "https://docs.google.com/presentation/d/15o32SFDuWYTgCX5ahUk_ibQCqxTLapxIOE4D4LRWGmk/edit?usp=sharing",
    ":floppy_disk: UX Use Case - Coco's Luxury Cat Toys":
        "https://docs.google.com/document/d/1WKCbLjCHyGs83yE2qIdn-sraVplyhbK7Xrqfj2NOl6s/edit?usp=sharing"
}
ACCOMPLISHMENETS = {
    ":small_red_triangle: Certified Product Owner":
        "https://media-exp1.licdn.com/dms/image/C512DAQFV8fQ4aSpgbw/profile-treasury-document-cover-images_480/0/1583708695510?e=1662415200&v=beta&t=yEBVBpwsqOC5lJuh9eL4gy5vtnLrC6V6XZQ7jL7AHMc",
    ":small_red_triangle: Certified Scrum Master":
        "https://media-exp1.licdn.com/dms/image/C512DAQEIMcvV8WzIEQ/profile-treasury-document-cover-images_480/0/1583843187002?e=1662415200&v=beta&t=rfOq6VSDuY1czhL95eyooUZzntUxiVv5voXYt3Qm7Cs",
    ":small_red_triangle: Certification of User Experience Design":
        "https://media-exp1.licdn.com/dms/image/C512DAQFEj40dc7q4rw/profile-treasury-document-cover-images_480/0/1583994385423?e=1662415200&v=beta&t=zag2GA-6mPkvNoA8KYkeLjsBgOLP8jxl5YCGnBYrgeY",
    ":small_red_triangle:Front End Web Development Certification":
        "https://media-exp1.licdn.com/dms/image/C512DAQFxwPORwcGL3g/profile-treasury-document-cover-images_480/0/1583991883746?e=1662415200&v=beta&t=3dTO9Wf3zgESQ4nzB-wA0tJC8pd1wX2kcxOoGcB-e_o",
    ":small_red_triangle: National Registry - Emergency Medical Technician":
        "https://media-exp1.licdn.com/dms/image/C512DAQGLqGtYHUtzgg/profile-treasury-document-cover-images_480/0/1583498727443?e=1662415200&v=beta&t=Njt0tdudexyuspVVnNyI5YZ9UvFAKTUF8ytExi3oK8A"
}
PROJECTS = {
    ":small_orange_diamond: This Website":
        "https://github.com/rodneygauna/rodneycodes-streamlit",
    ":small_orange_diamond: Originial rodney.codes Website":
        "https://github.com/rodneygauna/RodneyCodes",
    ":small_orange_diamond: WebDevAble Website":
        "https://github.com/rodneygauna/WebDevAble",
    ":small_orange_diamond: Learning SQL":
        "https://github.com/rodneygauna/palomar-CSIT150-IntroToSQL",
    ":small_orange_diamond: Learing Python":
        "https://github.com/rodneygauna/palomar-CSIT175-Python",
    ":small_orange_diamond: Skeevy - Open Source Pet Medication Tracking Web-App":
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
        label=" 📄 Download Resume",
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
for skill in SKILLS:
    st.write(f"{skill}")


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
# Business and Use Cases
# ------------------------------------------------------------------------------
st.write("#")
st.subheader("Business & Use Cases")
st.write("---")
for usecase, link in USECASES.items():
    st.write(f"[{usecase}]({link})")

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
