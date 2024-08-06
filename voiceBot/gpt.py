from groq import Groq
client = Groq(api_key='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')

def generate(promt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': promt,
            }
        ],
        model='llama3-8b-8192',
    )
    return chat_completion.choices[0].message
