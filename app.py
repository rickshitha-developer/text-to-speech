import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
import base64

# Page config
st.set_page_config(page_title="Translate & Speak", page_icon="🌍", layout="centered")

# 🎨 Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #667eea, #764ba2);
}
.main {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
}
.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #4A4A4A;
}
.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}
.stButton>button {
    background-color: #667eea;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}
.stButton>button:hover {
    background-color: #5a67d8;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌍 Translate & Speak</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert any text into your language + voice 🎙️</div>', unsafe_allow_html=True)

# Input
text = st.text_area("✍️ Enter your text here", height=150)

# Language selection
languages = {
    "🇮🇳 Hindi": "hi",
    "🇮🇳 Tamil": "ta",
    "🇬🇧 English": "en",
    "🇫🇷 French": "fr"
}
target_lang = st.selectbox("🌐 Select output language", list(languages.keys()))

# Convert
if st.button("🚀 Translate & Speak"):
    if text.strip():
        try:
            # Translate
            translated_text = GoogleTranslator(
                source='auto',
                target=languages[target_lang]
            ).translate(text)

            st.markdown("### 📝 Translated Text")
            st.success(translated_text)

            # Speech
            tts = gTTS(text=translated_text, lang=languages[target_lang])
            tts.save("output.mp3")

            audio = open("output.mp3", "rb").read()
            st.audio(audio)

            # Download
            b64 = base64.b64encode(audio).decode()
            st.markdown(
                f'<a href="data:audio/mp3;base64,{b64}" download="speech.mp3">📥 Download Audio</a>',
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter text first")
