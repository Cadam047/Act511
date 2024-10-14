import streamlit as st
from streamlit.testing.v1 import AppTest

def test_button_increments_counter():
    """Test that the counter increments when the button is clicked."""
    
    # Initialize the session state
    st.session_state.count = 0

    # Click the button
    st.button[0].click().run()

    # Assert that the counter has been incremented
    assert st.session_state.count == 1