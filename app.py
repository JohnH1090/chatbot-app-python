import streamlit as st
from groq import Groq


# creates groq client

client = Groq(api_key=st.secrets.get("GROQ_API_KEY"))

# page header
st.title("Chatbot")
st.write("Chatbot powered by Groq")
st.divider()

# sidebar
st.sidebar.title("Chats")

# session state
if "default_model" not in st.session_state:
    st.session_state["default_model"] = "llama-3.1-8b-instant"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

print(st.session_state)

# display the messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# add messages via chat input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display new message
    with st.chat_message("user"):
        st.markdown(prompt)

    # display the ai response from the model
    with st.chat_message("assistant"):
        # placeholder for response
        response_text = st.empty()

        # call the groq api
        completion = client.chat.completions.create(
            model=st.session_state.default_model,
            messages = [
                {"role": } for m in st.session_state.messages
            ]
        )
