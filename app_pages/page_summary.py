import streamlit as st

def page_summary_body():
    st.write("---")
    st.write("## Quick Project Summary")
    st.write("---")

    st.info(
        f"### General Information"

        f"\n Powdery mildew is a fungal disease caused by Podosphaera "
        f"clandestina that affects cherry trees. The fungus causes the "
        f"leaves to curl up, and may appear as white powdery patches on the "
        f"leaves. \n"
        f"The disease has to be visually identified, which can take an "
        f"employee up to half an hour per tree, however the treatment only takes a "
        f"minute if necessary.\n"
        f"Using this machine learning system, an employee can accurately identify "
        f"infected trees quickly, to make the inspection process possible within "
        f"the time limitations."
    )

    st.warning(
        f"### Project Dataset\n\n"
        f"The dataset, available on [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves), "
        f"contains over 4000 images of cherry tree leaves. Half the leaves are "
        f"infected with powdery mildew, and the other half are healthy."
    )

    st.success(
        f"### The Project has two business requirements:\n"
        f"1 - The client wants to conduct a study to visually differentiate "
        f"between healthy cherry leaves and leaves infected with powdery mildew.\n\n"
        f"2 - The client wants to accurately predict whether a cherry leaf is healthy"
        f"or contains powdery mildew."
    )

    st.write(
        f"For additional information about this project, please visit and read the "
        f"[Project README file](https://github.com/Rochilaz123/mildew-detection-in-cherry-leaves/blob/main/README.md)"
    )

