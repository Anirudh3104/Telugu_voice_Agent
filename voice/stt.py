# voice/stt.py

import torch
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import librosa
from transformers import (
    SeamlessM4Tv2ForSpeechToText,
    SeamlessM4TFeatureExtractor,
    SeamlessM4TTokenizer
)

# Load model ONCE
model = SeamlessM4Tv2ForSpeechToText.from_pretrained(
    "ai4bharat/indic-seamless"
)
processor = SeamlessM4TFeatureExtractor.from_pretrained(
    "ai4bharat/indic-seamless"
)
tokenizer = SeamlessM4TTokenizer.from_pretrained(
    "ai4bharat/indic-seamless"
)

def listen(seconds=8):
    fs = 16000
    print("🎙️ మాట్లాడండి...")

    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write("temp.wav", fs, audio)

    waveform, sr = sf.read("temp.wav")
    waveform = waveform.squeeze()

    if sr != 16000:
        waveform = librosa.resample(waveform, sr, 16000)

    inputs = processor(
        waveform,
        sampling_rate=16000,
        return_tensors="pt"
    )

    with torch.no_grad():
        tokens = model.generate(**inputs, tgt_lang="tel")

    text = tokenizer.decode(tokens[0], skip_special_tokens=True)
    return text

