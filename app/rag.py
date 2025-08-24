import openai
import os

def generate_answer(query, contexts):
    context_text = "\n".join([f"Page {c['page']} ({c['source']}): {c['text']}" for c in contexts])
    prompt = f"Answer the following question using ONLY the provided context.\n\nContext:\n{context_text}\n\nQuestion: {query}\nAnswer:"
    openai.api_key = os.getenv("OPENAI_API_KEY", "")
    if not openai.api_key:
        return "OpenAI API key not set."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
