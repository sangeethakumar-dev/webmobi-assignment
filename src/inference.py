from transformers import pipeline
from datasets import load_dataset
import time
import pandas as pd


def run_inference():
    print("Loading Whisper model...")

    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-small"
    )

    dataset = load_dataset(
        "hf-internal-testing/librispeech_asr_dummy",
        "clean",
        split="validation"
    )

    results = []

    for i in range(20):
        sample = dataset[i]
        audio = sample["audio"]["array"]

        start = time.time()
        prediction = pipe(audio)
        end = time.time()

        results.append({
            "audio_id": sample["id"],
            "ground_truth": sample["text"],
            "prediction": prediction["text"],
            "latency": end - start
        })

        print(f"Completed sample {i+1}/20")

    return pd.DataFrame(results)