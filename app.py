import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")

# Navbar
st.sidebar.title("Growth Mindset Challenge")
menu = st.sidebar.radio("Navigation", ["Home", "About Growth Mindset", "Tips", "Contact Us"])

# Home Page
if menu == "Home":
    st.title("Welcome to Growth Mindset Challenge 🌱")
    st.write("Discover how adopting a growth mindset can transform your personal and academic life.")
    st.image("https://source.unsplash.com/featured/?success,motivation", use_column_width=True)

# About Page
elif menu == "About Growth Mindset":
    st.title("What is a Growth Mindset?")
    st.write("""
    A *Growth Mindset* is the belief that abilities can be developed through hard work, learning, and dedication.
    This concept was introduced by *Carol Dweck*.
    """)

# Tips Page
elif menu == "Tips":
    st.title("How to Develop a Growth Mindset?")
    st.write("""
    - Embrace Challenges
    - Learn from Mistakes
    - Stay Positive
    - Celebrate Effort
    - Seek Feedback
    """)

# Contact Page
elif menu == "Contact Us":
    st.title("Contact Us")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Submit"):
        st.success(f"Thank you {name}! We'll get back to you soon.")