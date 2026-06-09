import pandas as pd

scheme = pd.read_csv(
    "data/processed/cleaned_scheme_performance.csv"
)

def recommend_funds(risk):

    return (
        scheme[
            scheme["risk_grade"] == risk
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

print(recommend_funds("Moderate"))