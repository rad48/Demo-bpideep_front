import streamlit as st
import pages.search
import pages.performers
import pages.home

PAGES = {
    "Home": pages.home,
    "Search company": pages.search,
    "Monthly report": pages.performers,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        page.write()

    st.sidebar.title("About this demo")
    st.sidebar.info(
        """
        This app is a demo version that was developped by [Antoine Planchon](https://www.linkedin.com/in/antoine-planchon-295503118/), \
        [Nicolas Rousselet](https://www.linkedin.com/in/nicolas-rousselet-188158b0/), \
        [Nicolas Tournaud](https://www.linkedin.com/in/nicolastournaud/) and \
        [Alexandre Huet](https://www.linkedin.com/in/alexandre-huet-5a0563127/).\n
        This 10-days project concludes a Data Science Bootcamp at Le Wagon.\n
        Special thanks to BPI France for the resources and great advices, and to the wonderful team of teachers and TAs at Le Wagon.
    """
    )


if __name__ == "__main__":
    main()
