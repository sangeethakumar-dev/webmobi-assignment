# Speech Model Evaluation Report

## Model Used
- openai/whisper-small

## Dataset Used
- hf-internal-testing/librispeech_asr_dummy
- Split: validation

## Number of Samples
- 20

## Evaluation Metrics
- Word Error Rate (WER): <value>
- Character Error Rate (CER): <value>
- Average Latency: <value> seconds

## Summary
The Whisper-small model performed well on speech recognition tasks. Predictions were largely accurate with minor differences in punctuation, capitalization, and abbreviations.

## Observations
- Model handled English speech well.
- Minor transcription differences occurred.
- Latency depends on audio duration and compute resources.

## Limitations
- Windows environment had FFmpeg dependency issues.
- Project was tested in Google Colab.