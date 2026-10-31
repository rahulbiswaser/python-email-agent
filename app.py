import streamlit as st
from ageny import draft_email

st.set_page_config(page_title="Email Drafting Assistant", page_icon="📧")
st.title("Email Drafting Assistant")

st.write("Enter your requirements and generate "
    "a professional email.")

#USER Input
recipient = st.text_input(
    "Who is the recipient?")
purpose = st.text_input(
    "What is the purpose of the email?")
tone = st.selectbox(
    "What is the tone of the email?",
    ["Formal", "Concise", "Friendly", "Professional"]
)

if st.button("Generate Email"):
    if not recipient.strip() or not purpose.strip():
        st.warning(
            "Please enter the recipient and purpose."
        )
    else:
        try:
            email_draft = draft_email(purpose, tone, recipient)
            st.write("Generated Email:")
            st.text_area("Email Draft", email_draft, height=300)
        except Exception as e:
            st.error(f"An error occurred: {e}")