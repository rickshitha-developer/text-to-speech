import streamlit as st
from gtts import gTTS
from googletrans import Translator
import base64

st.title("🌍 Translate & Speak App")

text = st.text_area("Enter text (any language)")

# Target language selection
languages = {
    "Hindi": "hi",
    "Tamil": "ta",
    "English": "en",
    "French": "fr"
}

target_lang = st.selectbox("Convert speech to:", list(languages.keys()))

if st.button("Translate & Speak"):
    if text.strip():
        try:
            translator = Translator()

            # 🌍 Translate text
            translated = translator.translate(text, dest=languages[target_lang])
            translated_text = translated.text

            st.write("📝 Translated Text:")
            st.success(translated_text)

            # 🔊 Convert to speech
            tts = gTTS(text=translated_text, lang=languages[target_lang])
            tts.save("output.mp3")

            audio = open("output.mp3", "rb").read()
            st.audio(audio)

            # 📥 Download
            b64 = base64.b64encode(audio).decode()
            href = f'<a href="data:audio/mp3;base64,{b64}" download="speech.mp3">📥 Download Audio</a>'
            st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Enter text first!")
