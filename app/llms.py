from openai import OpenAI

SYSTEM_PROMPT = "You are a helpful assistant."
USER_PROMPT = "Give me a short one-liner that's a weird thing to say in a Counter Strike 2 lobby. Only give me the one-liner text and nothing else."


def get_open_ai_response(model="gpt-4o-mini"):
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
    )
    return completion.choices[0].message.content.strip('"')
