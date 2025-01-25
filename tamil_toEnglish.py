import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

def tamil_to_english_translator():
    st.title("Tamil to English Translator and Audio Generator")

    # UI for input and instructions
    st.write("This app translates Tamil speech to English text and generates an audio clip.")

    if st.button("Start Listening"):
        st.write("Adjusting for ambient noise... Please wait.")
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source, duration=2)
                st.write("Listening for Tamil speech. Speak now!")

                # Record the audio
                audio = recognizer.listen(source)
                st.write("Processing your input...")

                # Recognize speech using Google Web Speech API
                tamil_text = recognizer.recognize_google(audio, language="ta-IN")
                st.write("You said (in Tamil):", tamil_text)

                # Translate Tamil text to English
                translated_text = GoogleTranslator(source="auto", target="en").translate(tamil_text)
                st.write("Translated to English:", translated_text)

                # Convert translated text to speech
                tts = gTTS(text=translated_text, lang="en")
                audio_file = "translated_audio.mp3"
                tts.save(audio_file)

                # Display audio playback option
                st.audio(audio_file, format="audio/mp3")

            except sr.UnknownValueError:
                st.error("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    tamil_to_english_translator()
