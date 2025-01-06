import streamlit as st
import firebase_admin
from firebase_admin import credentials
import json
import requests

# Only initialize the app if it's not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("firebasekey.json")
    firebase_admin.initialize_app(cred)

# Add global CSS for white text and red background
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            color: white;
            background-color: #ff3333; /* Red background for the entire app */
        }
        h1, h2, h3, h4, h5, h6 {
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50; /* Optional: Customize button color */
            color: white;
        }
        .stTextInput>div>div>input {
            color: white; 
            background-color: #40444B; /* Optional: Dark background for input fields */
        }
        .stSelectbox>div>div>div {
            color: white; 
            background-color: #40444B; /* Optional: Dark background for dropdowns */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def app():
    # Apply global CSS
    add_custom_css()

    # Title with white color and bold
    st.markdown(
        """
        <h1 style="color: white; text-align: center; font-weight: bold;">
            Welcome to Financial Planning Hub
        </h1>
        """,
        unsafe_allow_html=True
    )

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token
            }
            if username:
                payload["displayName"] = username
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            try:
                return r.json()['email']
            except:
                st.warning(r.json())
        except Exception as e:
            st.warning(f'Signup failed: {e}')

    def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        try:
            payload = {
                "returnSecureToken": return_secure_token
            }
            if email:
                payload["email"] = email
            if password:
                payload["password"] = password
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            try:
                data = r.json()
                user_info = {
                    'email': data['email'],
                    'username': data.get('displayName')  # Retrieve username if available
                }
                return user_info
            except:
                st.warning(data)
        except Exception as e:
            st.warning(f'Signin failed: {e}')

    def reset_password(email):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
            payload = {
                "email": email,
                "requestType": "PASSWORD_RESET"
            }
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            if r.status_code == 200:
                return True, "Reset email sent"
            else:
                error_message = r.json().get('error', {}).get('message')
                return False, error_message
        except Exception as e:
            return False, str(e)

    def login_user():
        try:
            userinfo = sign_in_with_email_and_password(st.session_state.email_input, st.session_state.password_input)
            st.session_state.username = userinfo['username']
            st.session_state.useremail = userinfo['email']

            st.session_state.signedout = True
            st.session_state.signout = True
        except:
            st.warning('Login failed')

    def logout_user():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''

    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    

    if not st.session_state["signedout"]:  # Show login/signup/forget password options only if user is not signed in
        choice = st.selectbox('Choose an option:', ['Sign up', 'Login', 'Forget Password'])

        if choice == 'Sign up':
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            username = st.text_input("Enter your unique username")

            if st.button('Create my account'):
                user = sign_up_with_email_and_password(email=email, password=password, username=username)
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()

        elif choice == 'Login':
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            st.session_state.email_input = email
            st.session_state.password_input = password

            if st.button('Login'):
                login_user()

        elif choice == 'Forget Password':
            email = st.text_input('Enter your email address')
            if st.button('Send Reset Link'):
                success, message = reset_password(email)
                if success:
                    st.success("Password reset email sent successfully.")
                else:
                    st.warning(f"Password reset failed: {message}")

    if st.session_state.signout:
        st.text(f'Name: {st.session_state.username}')
        st.text(f'Email id: {st.session_state.useremail}')
        st.button('Sign out', on_click=logout_user)

if __name__ == "__main__":
    app()
