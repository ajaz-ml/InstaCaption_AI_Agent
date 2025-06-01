import streamlit as st
from caption_generator import generate_caption

st.set_page_config(page_title="InstaCaption AI", page_icon="📸", layout="centered")

st.title("📸 InstaCaption AI Agent")
st.subheader("Generate viral Instagram captions in seconds using AI 🤖")

# Input form
with st.form("caption_form"):
    topic = st.text_input("What's your post about?", placeholder="e.g. solo travel, gym vibes, sunset, food cravings")
    
    style = st.selectbox("Choose caption style:", [
        "Funny 😂", "Motivational 💪", "Romantic ❤️", "Aesthetic ✨", "Sarcastic 😏", "Witty 😎"
    ])
    
    language = st.selectbox("Language", ["English", "Hindi", "Hinglish"])
    
    submitted = st.form_submit_button("✨ Generate Caption")

# Output
if submitted:
    with st.spinner("Crafting your perfect caption..."):
        captions = generate_caption(topic, style, language)

        st.success("Here are your AI-generated captions 👇")

        if isinstance(captions, list):
            for i, line in enumerate(captions, 1):
                st.markdown(f"**{i}.** {line}")
        else:
            st.write(f"💬 {captions}")

