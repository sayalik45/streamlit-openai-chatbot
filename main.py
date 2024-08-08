import streamlit as st
from chatbot import get_bot_response

st.title("Medical Assistant Chatbot")

if 'messages' not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Enter your message:")
submit_button = st.button("Send")

if submit_button and user_input:
    st.session_state.messages.append(f"User: {user_input}\n")
    bot_response = get_bot_response(message = user_input, previous_messages=st.session_state.messages)
    st.session_state.messages.append(f"Assistant: {bot_response}\n")

# Display chat history
for message in st.session_state.messages:
    if message.startswith("User:"):
        st.markdown(f"**{message.strip()}**")
    else:
        st.markdown(f"{message.strip()}")
