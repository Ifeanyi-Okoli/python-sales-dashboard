import pandas as pd


def clean_data(
    df,
    remove_duplicates=False,
    fill_missing=False,
    drop_missing_rows=False,
):
    cleaned_df = df.copy()

    if remove_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()

    if fill_missing:
        numeric_cols = cleaned_df.select_dtypes(include=["number"]).columns
        cleaned_df[numeric_cols] = (
            cleaned_df[numeric_cols]
            .fillna(cleaned_df[numeric_cols].mean())
        )

        text_cols = cleaned_df.select_dtypes(include=["object"]).columns

        for col in text_cols:
            if not cleaned_df[col].mode().empty:
                cleaned_df[col] = (
                    cleaned_df[col]
                    .fillna(cleaned_df[col].mode()[0])
                )

    if drop_missing_rows:
        cleaned_df = cleaned_df.dropna()

    return cleaned_df