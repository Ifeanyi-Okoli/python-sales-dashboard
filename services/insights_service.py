def generate_insights(df):
    insights = []

    missing = df.isnull().sum().sum()

    if missing > 0:
        insights.append(
            f"Dataset contains {missing} missing values."
        )

    numeric_cols = df.select_dtypes(include=["number"]).columns

    for col in numeric_cols:
        insights.append(
            f"{col}: minimum = {df[col].min()}, maximum = {df[col].max()}"
        )

    insights.append(
        f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns."
    )

    return insights