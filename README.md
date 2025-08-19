# 🎙️ Speech Recognition System (Wav2Vec2)

A **basic speech-to-text system** that transcribes short audio clips using a **pre-trained Wav2Vec2** model (Hugging Face Transformers + PyTorch).  
Works **offline**, no API keys required.

> **Demo file:** `data/sample.wav` 

---

## ✨ Why this project?

- ✅ **Meets assignment** :- Uses **pre-trained models** (Wav2Vec2) to **transcribe short clips**.
- ✅ **Offline & private** :- No cloud upload, no API keys.
- ✅ **Simple to run** :- One command to generate a demo audio, one to transcribe.

---

## 🔁 How this differs from my earlier project

I previously built a repository using **`SpeechRecognition` (Google Web Speech API)**.  
This project is **different and stronger** in several ways :

| Aspect | Earlier Project (Google API) | This Project (Wav2Vec2) |
|---|---|---|
| Internet | Required | **Not required** |
| Privacy | Audio sent to Google | **Local-only** |
| Model | Cloud recognizer | **Pre-trained DL model** (Hugging Face) |
| Languages | Depends on API | English (this checkpoint); can swap models |
| Robustness | Good in clean audio | **Better with accents / noisy audio** (often) |
| Dependencies | Fewer | PyTorch + Transformers (heavier, but offline) |

This shows clear **progress**: from an API-based script to a **model-based** offline system.

---

## 🚀 Quickstart

### 1) Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip

### 2) Install dependencies

pip install -r requirements.txt

If you plan to regenerate the sample audio from text, you’ll also need :
- System tool: ffmpeg (macOS: brew install ffmpeg)
- Python packages: gTTS and pydub

### 3) Generate synthetic audio (no need to record your voice)

python src/generate_audio.py

- This creates a clean data/sample.wav (16 kHz) for the demo.

### 4) Run transcription

python src/speech_to_text_wav2vec.py

---

##🧠 How it works (brief)

- Load pre-trained facebook/wav2vec2-base-960h (ASR model).

- Ensure audio is mono, 16 kHz.

- Extract features → run model → decode tokens to text.

---

##⚠️ Notes & Tips

If you see a warning about Wav2Vec2Tokenizer being deprecated, it’s fine; the code uses the recommended Wav2Vec2Processor version.

If you get a sampling rate error, resample to 16 kHz (the demo scripts already handle this).

Keep your repo clean: only ship data/sample.wav (delete sample.mp3 / temp.mp3).

---

## 👩‍💻 Author

**Name** : ALVIRA PARVEEN  
🔗 [LinkedIn](https://www.linkedin.com/in/alvira-parveen-78022536b)  
🌐 [GitHub](https://github.com/Alvira-Parveen)