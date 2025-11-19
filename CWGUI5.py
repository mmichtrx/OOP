import streamlit as st
from PIL import Image

col1, col2 = st.columns((4, 5))

with col1:
    st.title("My Resume")
    st.header("Michael Manning")

with col2:
    image = Image.open('Js-2025.jpg')
    st.image(image,width=200)


st.markdown("**About Me**")
st.text("I am a Freshman Cybersecurity Student.")
st.text("I have no prior experience in coding.")
st.divider()
st.text("I am a high school graduate who plans to graduate form JBU in May 2029.")
st.text("I have worked for an IT job for 3 summers at my local high schools, the things we did ranged from general repairs to building networking.")
st.text("My hobbies include; walking, being with friends, and playing games.")
st.divider()
st.markdown("**Contact Me:**")
st.text_input("Your Name: ")
st.text_input("Email ID: ")
message = st.text_area("Your Message")
st.button("Send Message")