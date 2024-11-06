import streamlit as st

def page_project_hypothesis_body():
    st.write("---")
    st.write("## Project Hypothesis and Validation")
    st.write("---")

    st.success(
        f"* We suspect that leaves infected with powdery mildew have clear signs, "
        f"predominantly white patches on the surface, that can differentiate them " 
        f"from healthy leaves.\n\n"
        f"* An Image Montage shows that typically an infected leaf has white patches "
        f"on the surface. "
        f"* Average Image shows that the surface of the average healthy leaf is clear, "
        f"whilst the surface of the average infected leaf has white marks."
        f"The Variability Image reveals white lines accross the centre of the average "
        f"infected leaf, whilst the centre of the average healthy leaf is clear."        
    )