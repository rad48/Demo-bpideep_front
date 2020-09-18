import streamlit as st

import awesome_streamlit as ast
import pages.search
import pages.performers
import pages.home

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": pages.home,
    "Search company": pages.search,
    "Top performers": pages.performers,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app was developped by Antoine Planchon, Nicolas Rousselet, Nicolas Tournaud and Alexandre Huet.\n
        This two-weeks project concludes a Data Science Bootcamp at Le Wagon.\n
        Special thanks to BPI France for the ressources and great advices, and to the wonderful team of Le Wagon.
    """
    )


if __name__ == "__main__":
    main()
