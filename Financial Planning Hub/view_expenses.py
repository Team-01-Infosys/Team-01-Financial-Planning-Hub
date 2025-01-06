import streamlit as st
import sqlite3
import pandas as pd

# Set custom background color for the entire app
st.markdown(
    """
    <style>
    body {
        background-color: #ff3333;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Create or connect to an SQLite database
conn = sqlite3.connect('expenses.db', check_same_thread=False)
c = conn.cursor()

def app():
    # Check if the user is logged in
    if 'username' not in st.session_state or st.session_state['username'] == '':
        st.warning('Please login first to view your expenses.')
        return 

    # Display title
    st.title('View Expenses - ' + st.session_state['username'])

    try:
        # Fetch expense data from database
        c.execute('SELECT id, category, amount, description, date FROM expenses')
        expenses = c.fetchall()

        if len(expenses) > 0:
            # Create a dataframe from the fetched data
            df = pd.DataFrame(expenses, columns=['ID', 'Category', 'Amount', 'Description', 'Date'])

            # Display expenses in a table
            st.dataframe(df)

            # Dropdown to select expense to delete
            expense_to_delete = st.selectbox('Select an expense to delete:', df['ID'])

            # Button to delete the selected expense
            if st.button('Delete Selected Expense'):
                c.execute('DELETE FROM expenses WHERE id = ?', (expense_to_delete,))
                conn.commit()
                st.success(f'Expense with ID {expense_to_delete} has been deleted.')

                # Refresh the expense list after deletion
                c.execute('SELECT id, category, amount, description, date FROM expenses')
                expenses = c.fetchall()
                df = pd.DataFrame(expenses, columns=['ID', 'Category', 'Amount', 'Description', 'Date'])
                st.dataframe(df)
        else:
            st.warning('No expenses found.')

    except Exception as e:
        # Handle errors
        st.error(f"An error occurred: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    app()
