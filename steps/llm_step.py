import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_analysis(df, anomalies):

    summary = f"""
Dataset has {len(df)} rows and {len(df.columns)} columns.

Columns:
{list(df.columns)}

Detected anomalies:
{anomalies}
"""

    prompt = f"""
You are a data analyst.

Analyze the dataset summary and anomaly report below.

Provide 3 clear business insights.

DATA SUMMARY:
{summary}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful data analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content