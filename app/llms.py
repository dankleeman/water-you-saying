from openai import OpenAI

DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."
DEFAULT_USER_PROMPT = "Give me a short one-liner that's a weird thing to say in a Counter Strike 2 lobby. Only give me the one-liner text and nothing else."


def get_open_ai_response(user_prompt=None, system_prompt=None, model="gpt-4o-mini"):
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt or DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt or DEFAULT_USER_PROMPT},
        ],
    )
    return completion.choices[0].message.content.strip('"')
