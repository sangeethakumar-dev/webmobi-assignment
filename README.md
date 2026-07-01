# Webmobi Assignment - Speech Model Inference & Evaluation Pipeline

This project implements a reproducible inference and evaluation pipeline using a pretrained speech recognition model from Hugging Face.

## Objective

The goal of this assignment is to:

- Understand a speech recognition model
- Run inference on speech/audio samples
- Evaluate performance using standard ASR metrics
- Build a reproducible pipeline

---

## Project Structure

```bash
webmobi-assignment/
│
├── README.md
├── requirements.txt
├── run.py
│
├── src/
│   ├── inference.py
│   ├── evaluate.py
│   └── utils.py
│
└── results/
    ├── predictions.csv
    ├── metrics.json
    └── report.md
```

---

## Model

Selected Model: `openai/whisper-small`

This model is used for Automatic Speech Recognition (ASR).

---

## Dataset

Dataset used:
- LibriSpeech / Common Voice (to be updated)

---

## Evaluation Metrics

The model is evaluated using:

- Word Error Rate (WER)
- Character Error Rate (CER)
- Average Inference Latency
- Number of Processed Samples

---

## Output Files

Results are saved in:

- `results/predictions.csv`
- `results/metrics.json`
- `results/report.md`

---

## Run Project

```bash
python run.py
```

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Status

Project setup in progress.
