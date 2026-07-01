# WebMobi Assignment – Speech Model Inference & Evaluation Pipeline

This project is developed as part of the WebMobi ML internship assignment.

The goal is to build a reproducible inference and evaluation pipeline using a publicly available speech model from Hugging Face.

---

# Project Objective

This project demonstrates:

- Understanding of speech AI models
- Loading pretrained models from Hugging Face
- Running inference on speech datasets
- Evaluating predictions using ASR metrics

---

# Model Used

**Model:** `openai/whisper-small`

Whisper is an automatic speech recognition (ASR) model developed by OpenAI for:

- Speech-to-text transcription
- Multilingual transcription
- Speech translation

---

# Dataset Used

**Dataset:** `hf-internal-testing/librispeech_asr_dummy`

This dataset contains sample speech audio and corresponding ground truth transcriptions.

---

# Project Structure

```bash
webmobi-assignment/
│
├── report/
│   └── whisper_summary.md
│
├── results/
│   ├── predictions.csv
│   ├── metrics.json
│   └── report.md
│
├── src/
│   ├── inference.py
│   ├── evaluate.py
│   └── utils.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

---

# Pipeline Workflow

## Step 1: Load Model
- Load Whisper model from Hugging Face

## Step 2: Load Dataset
- Load speech dataset from Hugging Face datasets

## Step 3: Run Inference
- Process 20 audio samples
- Generate predictions

## Step 4: Save Predictions
- Save outputs in CSV format

## Step 5: Evaluate Model
Metrics computed:
- Word Error Rate (WER)
- Character Error Rate (CER)
- Average Inference Latency
- Number of Processed Samples

---

# Evaluation Metrics

## Word Error Rate (WER)
Measures word-level transcription errors.

Lower value = better performance

## Character Error Rate (CER)
Measures character-level transcription errors.

Lower value = better performance

## Inference Latency
Measures time taken for prediction.

---

# Results

Final outputs are stored in:

- `results/predictions.csv`
- `results/metrics.json`
- `results/report.md`

---

# Dependencies

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python run.py
```

---

# Important Note

This project was fully validated in Google Colab.

Due to local Windows system restrictions (Device Guard policy blocking FFmpeg execution), complete audio inference could not be executed locally in VS Code.

However, the pipeline runs successfully in:
- Google Colab
- Linux systems
- macOS
- Windows systems without FFmpeg restrictions

---

# Assignment Components Covered

## Part 1 – Research
- Whisper paper summary completed

## Part 2 – Hugging Face Integration
- Model loading completed
- Dataset loading completed
- Inference completed

## Part 3 – Evaluation
- WER computed
- CER computed
- Latency measured
- Results saved

## Part 4 – Reproducibility
- Project structured for reproducible execution

---

# Author

**Sangeetha Kumar**  
Machine Learning / AI Enthusiast
