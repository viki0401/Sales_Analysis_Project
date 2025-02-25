import streamlit as st
# Define the navigation menu
pg = st.navigation([
      st.Page("pages/page.py", title="notes", icon="🔸")
])

# Run the navigation system
pg.run()