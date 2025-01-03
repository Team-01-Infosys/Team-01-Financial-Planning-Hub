import streamlit as st

def app():
    st.subheader('About Intelligent Financial Hub')
    st.write("""
        The **Intelligent Financial Hub** is an advanced platform designed to help individuals efficiently manage their personal finances. 
        It offers a seamless experience for tracking, categorizing, and budgeting expenses while providing detailed insights into spending behavior. 
    """)

    # Add custom CSS for hover effect
    st.markdown(
        """
        <style>
        .hover-effect:hover {
            color: #4CAF50;
            text-decoration: underline;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.write("""
        ### Key Features:
        - <span class="hover-effect">**Expense Tracking**</span>: Easily log and categorize daily expenses.
        - <span class="hover-effect">**Budget Management**</span>: Set budgets for different categories (e.g., food, utilities, entertainment) and manage them.
        - <span class="hover-effect">**Financial Insights**</span>: View personalized insights into spending habits through reports and charts.
        - <span class="hover-effect">**Account Management**</span>: Secure user login and authentication via Firebase, ensuring personal data is protected.
        - <span class="hover-effect">**Real-time Updates**</span>: Get notified of your spending limits and track progress against budgets in real-time.
    """, unsafe_allow_html=True)

    st.write("""
        The **Intelligent Financial Hub** simplifies personal finance management by offering all the tools necessary to take control of your financial health. Whether you want to keep track of monthly expenses or analyze trends over time, this platform is your go-to solution for all things financial.
    """)
