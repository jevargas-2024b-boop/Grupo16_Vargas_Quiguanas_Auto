import anthropic

client = anthropic.Anthropic(api_key="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")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Responde solo con: Conexión exitosa"}
    ]
)

print(message.content[0].text)