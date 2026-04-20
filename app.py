import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
import base64

st.title("🌍 Translate & Speak")

text = st.text_area("Enter text")

languages = {
    "Hindi": "hi",
    "Tamil": "ta",
    "English": "en"
}

target_lang = st.selectbox("Convert to:", list(languages.keys()))

if st.button("Convert"):
    if text.strip():
        try:
            # 🌍 Translate
            translated_text = GoogleTranslator(
                source='auto',
                target=languages[target_lang]
            ).translate(text)

            st.success(translated_text)

            # 🔊 Speech
            tts = gTTS(text=translated_text, lang=languages[target_lang])
            tts.save("output.mp3")

            audio = open("output.mp3", "rb").read()
            st.audio(audio)

            # 📥 Download
            b64 = base64.b64encode(audio).decode()
            st.markdown(f'<a href="data:audio/mp3;base64,{b64}" download="speech.mp3">Download</a>', unsafe_allow_html=True)

        except Exception as e:
            st.error(e)
