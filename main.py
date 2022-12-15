# necessary imports
import secrets
import string
import streamlit as st


def generator(len):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    # fix password length
    pwd_length = int(len)
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd



st.title("PASSWORD GENERATOR")
st.text("")
start = '<p "font-size:42px;">Length of password:</p>'
st.markdown(start, unsafe_allow_html=True)

pwd_len = st.text_input('', label_visibility='collapsed', placeholder="Length in numbers..")

pwd = ''
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3:
    center_button = st.button('Generate')

try:
    if center_button:
        pwd = generator(pwd_len)
except ValueError:
    st.error("Enter valid number", icon='😊')

text = '<p "font-size:42px;">Generated Password:</p>'
st.markdown(text, unsafe_allow_html=True)
st.write(pwd)

