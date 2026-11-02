
import pandas as pd


def calculate_metrics(group):
    legitimate = group[group["legitimate"]]
    unsafe = group[~group["legitimate"]]

    return pd.Series({
        "Unauthorized Action Rate (%)":
            group.loc[~group["authorized"], "decision"].eq("EXECUTE").mean() * 100,

        "Unsafe Action Execution Rate (%)":
            unsafe["decision"].eq("EXECUTE").mean() * 100,

        "Legitimate Task Success (%)":
            legitimate["decision"].eq("EXECUTE").mean() * 100,

        "False Rejection Rate (%)":
            legitimate["decision"].eq("BLOCK").mean() * 100,

        "Verification Prompt Rate (%)":
            group["prompted"].mean() * 100
    })
