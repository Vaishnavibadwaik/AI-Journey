import streamlit as st
import random

st.set_page_config(
    page_title="RuleBot",
    page_icon="🤖"
)

st.title("🤖 RuleBot")
st.write("A Simple Rule-Based Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    user_text = user_input.lower()

    # Bot Logic
    if user_text == "help":
        response = """
Available Commands:
- hello / hi
- how are you
- joke
- fact
- your name
- bye
"""

    elif user_text in ["hello", "hi", "hey"]:
        response = random.choice([
            "Hello!",
            "Hi there!",
            "Hey!",
            "Nice to meet you!"
        ])

    elif "how are you" in user_text:
        response = "I am fine. Thanks for asking! 😊"

    elif "joke" in user_text:
        response = "Why do programmers prefer dark mode? Because light attracts bugs! 😄"

    elif "fact" in user_text:
        response = "Python is one of the most popular programming languages."

    elif "your name" in user_text:
        response = "I am RuleBot 🤖"

    elif "bye" in user_text:
        response = "Goodbye! Have a great day 😊"

    else:
        response = "Sorry, I don't understand that."

    # Show bot message
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )