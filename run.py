import json
from src.inference import run_inference
from src.evaluate import evaluate


def main():
    df = run_inference()

    df.to_csv("results/predictions.csv", index=False)

    metrics = evaluate(df)

    with open("results/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("Assignment completed successfully!")


if __name__ == "__main__":
    main()