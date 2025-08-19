import torch
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Load processor and model

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Load and resample audio to 16kHz

audio_input, sample_rate = librosa.load("data/sample.wav", sr=16000)

# Process audio

inputs = processor(audio_input, sampling_rate=16000, return_tensors="pt", padding=True)

# Run model

with torch.no_grad():
    logits = model(inputs.input_values).logits

# Decode transcription

predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)

print("🎤 Transcription:\n", transcription[0])
