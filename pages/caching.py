
import streamlit as st
import time

# Caching an expensive computation function
@st.cache_data  # Streamlit's caching decorator for caching data (works well for data-heavy computations)
def expensive_computation(n):
    """Simulate an expensive computation."""
    time.sleep(2)  # Simulate a time-consuming task
    result = n * n
    return result
