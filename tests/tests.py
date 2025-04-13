"""
Tests for ../app.py

Run from the project directory (not the tests directory) with the invocation `pytest tests/tests.py`
"""
import streamlit as st
from streamlit.testing.v1 import AppTest

def test_button_increments_counter():
    """Test that the counter increments when the button is clicked."""
    at = AppTest.from_file("app.py").run()

    # Initialize the session state.
    # Note that we use at.session_state, not st.session_state. This is the testing session_state object.
    at.session_state.count = 1

    # Click the button
    at.button(key="increment").click().run()

    # Assert that the counter has been incremented
    assert at.session_state.count == 2

def test_button_decrements_counter():
    # TODO test that the decrement button works
    
    """Test that the counter decrements when the button is clicked."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 2
    at.button(key="decrement").click().run()
    assert at.session_state.count == 1

def test_button_increments_counter_ten_x():
    # TODO test that the increment button works in ten_x mode
    """Test that the counter increments by 10 when ten_x mode is on."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 5
    at.session_state.ten_x = True
    at.checkbox(key="ten_x").check().run()  # ensure checkbox is checked in UI
    at.button(key="increment").click().run()
    assert at.session_state.count == 15 


def test_button_decrements_counter_ten_x():
    # TODO test that the decrement button works in ten_x mode
    """Test that the counter decrements by 10 when ten_x mode is on."""
    at = AppTest.from_file("app.py").run()
    at.session_state.count = 20
    at.session_state.ten_x = True
    at.checkbox(key="ten_x").check().run()
    at.button(key="decrement").click().run()
    assert at.session_state.count == 10

def test_output_text_correct():
    """Test that the text shows the correct value."""
    at = AppTest.from_file("app.py").run()

    # Initialize session state
    at.session_state.count = 0
    at.session_state.ten_x = False

    # Increment once at 1x, once at 10x.
    at.button(key="increment").click().run()
    at.checkbox(key="ten_x").check().run()
    at.button(key="increment").click().run()

    # Check text value
    assert at.markdown[0].value == "Total count is 11"