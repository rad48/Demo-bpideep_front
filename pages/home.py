import streamlit as st

# import awesome_streamlit as ast

def write():

    # pylint: disable=line-too-long
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        st.title('Deeptech prediction project')
        st.write(
            """
    This application provides
    - A **predict** tool to predict the likehood for a start-up of being classified as Deeptech.
    - A **reporting** tool that exract start-up with the highest founding rounds of a specified.
        """
            )
    st.write('## What is a Deeptech ?')
    st.write('Understand the stacks of Deeptech through this [Bpi infographic](https://www.bpifrance.fr/A-la-une/Dossiers/Generation-Deeptech-le-futur-de-l-innovation/Une-infographie-pour-comprendre-la-deeptech-45964).')
    st.image('https://www.bpifrance.fr/var/bpifrance/storage/images/media/images/bpifrance_generation-deeptech_infographie_012019_pg8/816671-1-fre-FR/Bpifrance_GENERATION-DEEPTECH_INFOGRAPHIE_012019_PG8_imagefull.jpg')



if __name__ == "__main__":
    write()
