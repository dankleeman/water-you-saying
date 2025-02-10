from openai import OpenAI

DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."
DEFAULT_USER_PROMPT = "Give me a short one-liner that's a weird thing to say in a Counter Strike 2 lobby. Only give me the one-liner text and nothing else."


def get_open_ai_response(user_prompt=None, system_prompt=None, model="gpt-4o-mini", enc_image_str:str | None =None):
    client = OpenAI()

    system_content = system_prompt or DEFAULT_SYSTEM_PROMPT
    if enc_image_str:
        user_content = [{"type": "text", "text": user_prompt},                 {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{enc_image_str}"},
        },]
    else:
        user_content = user_prompt or DEFAULT_USER_PROMPT

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
    )
    return completion.choices[0].message.content.strip('"')
