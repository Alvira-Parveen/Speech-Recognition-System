from gtts import gTTS
from pydub import AudioSegment
import os

# Create folder if it doesn't exist

os.makedirs("data", exist_ok=True)

# Generate sample audio (mp3)

tts = gTTS("Hello, this is a test for speech recognition.")
tts.save("data/sample.mp3")

# Convert mp3 → wav using pydub\

audio = AudioSegment.from_mp3("data/sample.mp3")
audio.export("data/sample.wav", format="wav")

print("✅ Sample audio generated at data/sample.wav")
