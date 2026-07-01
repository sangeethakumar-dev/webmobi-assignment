from jiwer import wer, cer
from src.utils import normalize_text


def evaluate(df):
    ground_truths = [normalize_text(x) for x in df["ground_truth"]]
    predictions = [normalize_text(x) for x in df["prediction"]]

    wer_score = wer(ground_truths, predictions)
    cer_score = cer(ground_truths, predictions)

    metrics = {
        "num_samples": len(df),
        "average_latency": df["latency"].mean(),
        "wer": wer_score,
        "cer": cer_score
    }

    return metrics