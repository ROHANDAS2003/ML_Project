import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai_api_key = os.getenv('OPEN_AI_API_KEY')
openai.api_key = openai_api_key

def classify_with_llm(log_msg):
    prompt = f"""Classify the log message into one of these categories:
    (1) Workflow Error , (2) Depreation Warning.
    If you can't figure out the category, return "Unclaffified".
    Only return the category name. No Preamble.
    Log message: {log_msg}"""

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(classify_with_llm("System reboot initeated by user 2345."))
    print(classify_with_llm("The 'Report Generator' module will be retired in version 4.0. Please migrate to the 'AdvanceAnalyticsSuite' by 01-06-2025."))
    print(classify_with_llm("Case escalation for ticket ID 7654 failed because the assigned support agent is no longer active."))