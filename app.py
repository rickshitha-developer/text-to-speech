import streamlit as st
from gtts import gTTS
import os

st.title("🔊 Text to Speech Converter")

text = st.text_area("Enter text")

if st.button("Convert to Speech"):
    if text:
        tts = gTTS(text)
        tts.save("output.mp3")

        audio_file = open("output.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

        st.success("Converted successfully!")
    else:
        st.warning("Please enter some text")
