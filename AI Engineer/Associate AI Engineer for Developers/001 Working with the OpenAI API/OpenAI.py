from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    # Write your prompt
    prompt="Simply and concisely, explain why learning about the OpenAI API is important for developers.",
    max_tokens=200
)

print(response.choices[0].text)