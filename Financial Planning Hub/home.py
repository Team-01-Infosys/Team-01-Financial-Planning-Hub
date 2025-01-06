import streamlit as st

def app():
    # Initialize session state variable if not already set
    if 'username' not in st.session_state:
        st.session_state['username'] = ''

    # Check if user is logged in
    if st.session_state['username'] == '':
        # Prompt the user to enter their username
        st.title("Welcome to the Financial Planning Hub")
        st.write("Please log in to continue.")
        
        # Create a login form
        with st.form(key='login_form'):
            username = st.text_input("Username")
            login_button = st.form_submit_button("Login")
            
            if login_button:
                if username != '':
                    # Save the username to session state
                    st.session_state['username'] = username
                    st.success(f"Welcome, {st.session_state['username']}!")
                else:
                    st.error("Please enter a valid username.")
    else:
        # If the user is logged in, display a welcome message
        st.title(f"Welcome to the Financial Planning Hub, {st.session_state['username']}")
        
        st.write("""
            This hub allows you to manage your financial expenses and track your spending habits.
            
            You can:
            - Add Expenses
            - View Expenses
            - Track your total expenses
            - Get insights into your financial health
        """)
        
        st.markdown("### Navigate through the options on the sidebar to get started.")
        st.button("Log Out", on_click=log_out)

def log_out():
    # Clear session state and log the user out
    st.session_state['username'] = ''
    st.success("You have been logged out successfully.")
