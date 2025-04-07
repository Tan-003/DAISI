import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
#st.set_page_config(page_title="personalsite", layout="wide")
st.set_page_config(page_title="Tan's Personal Site", layout="wide")

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        # If you don't want to show the 'Navigation' label, you can remove the word 'Navigation' and the colon but keep the colon.
        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.radio(
            "Navigation", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")

        app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app, and you can change the order of the pages by changing the order of the add_app calls
app.add_app("Home Page", home_page)
app.add_app("Education Page", education_page)
app.add_app("Experience Page", experience_page)
app.add_app("Resume Page", resume_page)
app.add_app("Contact Page", contact_page)

# Run the app
app.run()
