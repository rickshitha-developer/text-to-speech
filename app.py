import streamlit as st
from gtts import gTTS
import base64

st.set_page_config(page_title="TTS App", page_icon="🔊", layout="centered")

# 🎨 Custom UI Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #4A90E2;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🔊 Text to Speech Converter</div>', unsafe_allow_html=True)

# 🎙️ Input
text = st.text_area("Enter your text here", height=150)

# 🌍 Language selection
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es"
}
lang_choice = st.selectbox("Choose Language", list(languages.keys()))

# 🔊 Speed control
speed = st.radio("Select Speed", ["Normal", "Slow"])

# 🎯 Convert Button
if st.button("Convert to Speech"):
    if text.strip() != "":
        tts = gTTS(
            text=text,
            lang=languages[lang_choice],
            slow=True if speed == "Slow" else False
        )

        file_path = "output.mp3"
        tts.save(file_path)

        # 🔊 Play audio
        audio_file = open(file_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        # 📥 Download button
        b64 = base64.b64encode(audio_bytes).decode()
        href = f'<a href="data:audio/mp3;base64,{b64}" download="speech.mp3">📥 Download Audio</a>'
        st.markdown(href, unsafe_allow_html=True)

        st.success("✅ Conversion successful!")
    else:
        st.warning("⚠️ Please enter some text")
