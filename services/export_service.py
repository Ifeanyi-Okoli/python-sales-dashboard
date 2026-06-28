def convert_df_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


def generate_insights_report(insights):
    report = "BUSINESS INSIGHTS REPORT\n"
    report += "=" * 40 + "\n\n"

    for i, item in enumerate(insights, 1):
        report += f"{i}. {item}\n"

    return report