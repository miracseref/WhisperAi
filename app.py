import streamlit as st
import whisper

st.title("WhisperAi WebApp")

model_size = st.selectbox("Select model size", [
                          'tiny', 'base', 'small', 'medium', 'large'])

model = whisper.load_model(model_size)

sample = st.radio("Choose audio file", [
                  'Example 1', 'Example 2', 'Example 3', "Specific Url"])

audio = False
ex_1 = "https://datasets-server.huggingface.co/assets/google/fleurs/--/en_us/train/12/audio/audio.mp3"
ex_2 = "https://datasets-server.huggingface.co/assets/google/fleurs/--/en_us/train/14/audio/audio.mp3"
ex_3 = "https://datasets-server.huggingface.co/assets/google/fleurs/--/en_us/train/24/audio/audio.mp3"

if sample == "Example 1":
    audio = ex_1
elif sample == "Example 2":
    audio = ex_2
elif sample == "Example 3":
    audio = ex_3
elif sample == "Specific Url":
    audio = st.text_input("Paste your audio file's url")

if audio:
    # Display audio
    st.audio(audio, format='audio/wav')

    # Run the model and show the result
    output = model.transcribe(audio)
    if output:
        st.json(output)
