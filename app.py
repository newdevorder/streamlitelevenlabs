import os
from dotenv import load_dotenv
from elevenlabs import generate, set_api_key
from elevenlabs.api import Voices

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

# Import the 'generate' and 'play' functions from the 'elevenlabs' module
from elevenlabs import generate, play

# Define a text to be converted into speech
text_to_convert = "¡Hola! Mi nombre es Allison, encantado de conocerte. Soy un apasionado de la tecnología y siempre estoy buscando formas innovadoras de mejorar la vida cotidiana. Mi interés por la informática comenzó desde una edad temprana, cuando desarmaba y volvía a armar dispositivos electrónicos solo por diversión. A medida que crecí, esta curiosidad se transformó en una verdadera pasión por aprender sobre programación y desarrollo de software. Me emociona la posibilidad de crear soluciones útiles y eficientes a través del código, ya sea diseñando aplicaciones que simplifiquen tareas o contribuyendo a proyectos de código abierto. Además de mi amor por la tecnología, disfruto explorando la naturaleza, leyendo sobre diferentes culturas y experimentando con nuevas recetas en la cocina. Creo que cada día brinda oportunidades emocionantes para aprender algo nuevo y estoy emocionado de compartir este viaje con personas afines. Siempre estoy abierto a conversaciones estimulantes y colaboraciones emocionantes que puedan enriquecer mi vida y la de los demás. ¡Espero poder conocerte mejor y descubrir las muchas formas en que podemos crecer juntos!"

# Specify the voice to be used for text-to-speech conversion
selected_voice = "Allison"

# Specify the text-to-speech model to be used
selected_model = 'eleven_multilingual_v1'

# Generate the audio data from the given text, using the specified voice and model
audio = generate(text=text_to_convert, voice=selected_voice, model=selected_model)

# Play the generated audio in a notebook environment
play(audio, notebook=True)
