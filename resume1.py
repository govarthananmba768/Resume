import streamlit as st
from pathlib import Path
from PIL import Image

 # Directionary 
current_dir = Path(__file__).parent if "__file__ " in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"    
profile_pic = current_dir / "asserts" / "profile_pic.jpeg"
resume_file = current_dir / "asserts" / "Govarthanan's Resume (S).pdf"
 

PAGE_TITLE = "Digital Resume | Govarthanan "
PAGE_ICON = ":wave"
NAME = "GOVARTHANAN KS"
DESCRIPTION =""" 
Data Scientist || Machine learning || Data Analyst || Power BI Developer
"""
EMAIL= "govarthananmba768@gmail.com"
PHONE_NUMBER ="8248013321"
SOCIAL_MEDIA = {
    "LINKED IN":"www.linkedin.com/in/govarthananks",
    "GITHUB"   :"https://github.com/govarthananmba768"

}
PROJECTS ={
    " Customer Conversion Prediction Using Machine Learning" :"https://github.com/govarthananmba768/Customer-conversion-",
    "Movie recommandation":"https://github.com/govarthananmba768/Movie_Recommendation"
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello Govar")


# load css file , pdf 

with open(css_file) as  f:
    st.markdown("<style>{}</style>". format(f.read()),unsafe_allow_html=True)

with open(resume_file , "rb") as  pdf_file:
    PDFbyte = pdf_file.read()
profile_pic1 = Image.open(profile_pic)



# Hero section

col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic1, width =230)


with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("", EMAIL)
    st.write("", PHONE_NUMBER)


# social links 
st.write("#")

cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform, link) in enumerate (SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}] ({link})")



# Experience 

st.write("#")
st.subheader("Experience & Qualification")
st.write(
    """
 - 1+ year experience in Process associate role in Congruent Solution Pvt
 - Done 8 months data science course in GUVI
 - MBA in Gandhigram Rural Institute
 - B.Sc Mathematics in GTN Arts and science college

"""
)

# Skills
st.write("#")
st.subheader("Key skills")
st.write(
    """
- Programming language : Python , SQL 
- Data Visualization   : Power BI , Excel , Tableau
- Model                : Machine learning 
- Deployment           : Streamlit, Render 


"""
)


# work history
st.write("---")
st.subheader("Process associate")
st.write(
    """
-Verified completeness and accuracy of data input by performing quality assurance checks on 500+ transactions
daily; identified and resolved 20+ transactional errors, saving the company $15k in costs.

-Conducted daily quality assurance checks on transactions and account actions to ensure compliance with regulatory
standards; maintained a 90 percentage accuracy rate and reduced compliance violations by 45%.

-Assessed business processes and communicate identified ways to boost improvement.

-Skills Excel, Power point, ASC, VM Ware, Communication, collaborate to work, continuous learning


"""
)

# Project details 
st.write("#")
st.subheader("Project ")

for projects,link in PROJECTS.items():
    st.write(f"[{projects}]({link})")

