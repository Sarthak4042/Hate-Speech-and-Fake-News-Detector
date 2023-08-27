
import streamlit as st
from PIL import Image, ImageDraw
import json
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
     page_title="The Truth Project",
     page_icon="Hello"
)

# # Load the image
# img = Image.open('4.PNG')

# # Add a circular mask to the image
# mask = Image.new('L', img.size, 0)
# draw = ImageDraw.Draw(mask)
# draw.ellipse((0, 0) + img.size, fill=255)
# img.putalpha(mask)

# # Display the image in the sidebar
# st.sidebar.image(img, use_column_width=True)

# st.sidebar.header('THE TRUTH PROJECT')
# st.sidebar.text('Hate Speech and Fake News Detector.')

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


lottie_coding = load_lottiefile("newhello.json")
st_lottie(
    lottie_coding,
    height=400,
)


image = Image.open('8.PNG')
st.image(image)

# st.header("The Truth Project")
# st.text("The Truth Project is a software tool that uses artificial intelligence and natural")
# st.text("language processing techniques to identify instances of hate speech in written or")
# st.text("spoken language.")

# image = Image.open('3.PNG')
# st.image(image)

# st.header("Hate Speech Detector")
# st.text("Hate speech is any form of speech that targets a particular group of people based on")
# st.text("their race, ethnicity, religion, gender, sexual orientation, or other characteristic.")
# st.text("Hate speech detectors use a range of techniques, including keyword analysis,")
# st.text("sentiment analysis, and context analysis, to identify and flag instances of")
# st.text("hate speech.")

# image = Image.open("5.PNG")
# st.image(image)

# st.header("Fake News Detector")
# st.text("A fake news detector is a software tool that uses similar techniques to identify")
# st.text("instances of false or misleading information in written or spoken language.")
# st.text("Fake news is any type of news that is intentionally fabricated or misleading,")
# st.text("designed to misinform or manipulate the reader or viewer. Fake news detectors use a")
# st.text("range of techniques, including fact-checking, source analysis, and context analysis,")
# st.text("to identify and flag instances of fake news.")

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from uuid import uuid4

def get_session_state():
    # Get the session state for the current session ID
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid4())
    if st.session_state.session_id not in st.session_state:
        st.session_state[st.session_state.session_id] = {}
    return st.session_state[st.session_state.session_id]

def set_session_state(state):
    # Set the session state for the current session ID
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid4())
    if st.session_state.session_id not in st.session_state:
        st.session_state[st.session_state.session_id] = {}
    st.session_state[st.session_state.session_id] = state

def register():
    st.header("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Register"):
        if password == confirm_password:
            st.success("You have successfully registered.")
        else:
            st.error("Passwords do not match.")
            
def login():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "test" and password == "123456":
            set_session_state({"is_logged_in": True, "username": username})
            st.success("Logged in as {}".format(username))
            switch_page("homepage")

        else:
            st.error("Incorrect username or password.")

        if username == "Sarthak" and password == "123456":
            set_session_state({"is_logged_in": True, "username": username})
            st.success("Logged in as {}".format(username))
            switch_page("homepage")

        else:
            st.error("Incorrect username or password.")



def logout():
    set_session_state({"is_logged_in": False, "username": None})
    st._rerun()

# Main App
def Homepage():
    
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Select an option", menu)
    
    # Check if the user is logged in
    session_state = get_session_state()
    is_logged_in = session_state.get("is_logged_in", False)
    username = session_state.get("username", None)

    # Create a logout button container if the user is logged in
    if is_logged_in:
        logout_container = st.sidebar.container()
        with logout_container:
            st.button("Logout", on_click=logout)
    
    # Show the appropriate page based on user selection
    if choice == "Login":
        login()
    elif choice == "Register":
        register()
    elif is_logged_in:
        st.success(f"Logged in as {username}")
        

Homepage()