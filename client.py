from openai import OpenAI

client = OpenAI(
    api_key = "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",
)

completion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)