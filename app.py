import os
from dotenv import load_dotenv
from elevenlabs import generate, set_api_key
from elevenlabs.api import Voices
import streamlit as st

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

# Import the 'generate' and 'play' functions from the 'elevenlabs' module
from elevenlabs import generate, play

set_api_key(ELEVENLABS_API_KEY)

# Define a text to be converted into speech
text_to_convert = "¡Hola! Mi nombre es Arnold, encantado de conocerte. Soy un apasionado de la tecnología y siempre estoy buscando formas innovadoras de mejorar la vida cotidiana. Mi interés por la informática comenzó desde una edad temprana, cuando desarmaba y volvía a armar dispositivos electrónicos solo por diversión. A medida que crecí, esta curiosidad se transformó en una verdadera pasión por aprender sobre programación y desarrollo de software. Me emociona la posibilidad de crear soluciones útiles y eficientes a través del código, ya sea diseñando aplicaciones que simplifiquen tareas o contribuyendo a proyectos de código abierto.."

# Specify the voice to be used for text-to-speech conversion
selected_voice = "n1Vh9dBauiqn81Oc1jRs"

# Specify the text-to-speech model to be used
selected_model = 'eleven_multilingual_v1'

# Generate the audio data from the given text, using the specified voice and model
audio = generate(text=text_to_convert, voice=selected_voice, model=selected_model)

# Play the generated audio in a notebook environment
play(audio, notebook=True)

st.audio(audio)
