import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import individual app modules
# Assuming these modules (home, add_expenses, account, view_expenses, about, dashboard) are implemented separately
import home, add_expenses, account, view_expenses, about, dashboard

st.set_page_config(
    page_title="Financial Planning Hub",
    layout="wide"
)

# Add custom CSS for styling
st.markdown(
    """
    <style>
    :root {
        --primary-color: #4CAF50;
        --secondary-color: #f1f1f1;
        --font-color: #333;
        --accent-color: #2196F3;
    }

    body {
        font-family: Arial, sans-serif;
        background-color: var(--secondary-color);
        color: var(--font-color);
    }

    .css-18e3th9 {
        background-color: var(--secondary-color) !important;
        color: var(--font-color) !important;
    }

    .css-1d391kg {
        background-color: var(--secondary-color) !important;
        color: var(--font-color) !important;
    }

    [data-testid="stSidebar"] {
        background-color: #ebebe0 !important;
    }

    [data-testid="stSidebar"] .css-1d0tddo {
        color: black !important;
        font-weight: bold !important;
        font-size: 28px !important;
    }

    h1, h2 {
        color: var(--primary-color) !important;
        font-weight: bold !important;
    }

    /* Specific styling for Add Expenses section */
    .add-expenses-title {
        color: black !important;  /* Set title to black */
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Google Analytics (if applicable)
st.markdown(
    f"""
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{os.getenv('analytics_tag')}');
        </script>
    """,
    unsafe_allow_html=True
)

# Define the MultiApp class
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Add an app to the list."""
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        """Run the selected app."""
        # Sidebar with app options
        with st.sidebar:
            st.markdown("<h2 style='color: black; font-weight: bold; font-size: 28px;'>📊 Financial Planning Hub</h2>", unsafe_allow_html=True)
            app = option_menu(
                menu_title='',  # Sidebar title is handled with custom HTML
                options=[app["title"] for app in self.apps],
                icons=['house-fill', 'person-circle', 'plus-circle', 'list', 'graph-up', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": '#ebebe0'},
                    "icon": {"color": "black", "font-size": "23px"},
                    "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#ccccb3"},
                    "nav-link-selected": {"background-color": "#ccccb3"},
                }
            )

        # Execute the selected app
        for app_obj in self.apps:
            if app == app_obj["title"]:
                if app_obj["title"] == "Add Expenses":
                    # Add specific title styling for Add Expenses (only once)
                    st.markdown("<h2 class='add-expenses-title'>Add Expenses</h2>", unsafe_allow_html=True)
                app_obj["function"]()
                break

# Create an instance of the MultiApp class and add applications
multi_app = MultiApp()
multi_app.add_app("Home", home.app)
multi_app.add_app("Account", account.app)
multi_app.add_app("Add Expenses", add_expenses.app)
multi_app.add_app("View Expenses", view_expenses.app)
multi_app.add_app("Dashboard", dashboard.app)
multi_app.add_app("About", about.app)

# Run the app
if __name__ == "__main__":
    multi_app.run()
