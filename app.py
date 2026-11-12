import streamlit as st
import ollama

st.set_page_config(page_title="Local Chatbot", page_icon="💬")
st.title("💬 Local LLM Chatbot")

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Settings")

    # Get the list of models installed in Ollama
    try:
        installed = [m.model for m in ollama.list().models]
    except Exception:
        installed = []

    if not installed:
        st.error("No models found. Is Ollama running?")
        st.stop()

    model = st.selectbox("Model", installed)

    system_prompt = st.text_area(
        "System prompt",
        value="You are a helpful, concise assistant.",
        height=100,
    )

    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

st.caption(f"Running {model} locally with Ollama")

# ---------- Chat history ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- New message ----------
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        def stream_reply():
            full_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages
            stream = ollama.chat(model=model, messages=full_messages, stream=True)
            for chunk in stream:
                yield chunk["message"]["content"]

        reply = st.write_stream(stream_reply())

    st.session_state.messages.append({"role": "assistant", "content": reply})