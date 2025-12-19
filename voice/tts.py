# voice/tts.py

import torch
import soundfile as sf
import sounddevice as sd
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer

device = "cuda" if torch.cuda.is_available() else "cpu"

model = ParlerTTSForConditionalGeneration.from_pretrained(
    "ai4bharat/indic-parler-tts"
).to(device)

tokenizer = AutoTokenizer.from_pretrained(
    "ai4bharat/indic-parler-tts"
)

description_tokenizer = AutoTokenizer.from_pretrained(
    model.config.text_encoder._name_or_path
)

def speak(text):
    description = (
        "Lalitha speaks in a calm, clear Telugu voice. "
        "The recording is very clear with no background noise."
    )

    prompt_inputs = tokenizer(text, return_tensors="pt").to(device)
    desc_inputs = description_tokenizer(description, return_tensors="pt").to(device)

    with torch.no_grad():
        audio = model.generate(
            input_ids=desc_inputs.input_ids,
            attention_mask=desc_inputs.attention_mask,
            prompt_input_ids=prompt_inputs.input_ids,
            prompt_attention_mask=prompt_inputs.attention_mask,
        )

    audio = audio.cpu().numpy().squeeze()
    sf.write("reply.wav", audio, model.config.sampling_rate)

    sd.play(audio, model.config.sampling_rate)
    sd.wait()
