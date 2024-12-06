import os

from groq import Groq

client = Groq(
    api_key="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"
)


def process_content(content, query):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes content and answers questions based on the given information.",
            },
            {
                "role": "user",
                "content": f"Summarize the following content and answer this question: {query}\n\nContent: {content}",
            }
        ],
        model="llama-3.1-70b-versatile",
        max_tokens=500,
        temperature=0.8,
    )

    return chat_completion.choices[0].message.content