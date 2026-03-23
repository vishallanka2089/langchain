import tiktoken

# Choose model (important)
encoding = tiktoken.encoding_for_model("gpt-4o-mini")

text = "Checking how many tokens!"

# Convert text → tokens
tokens = encoding.encode(text)

print("Tokens:", tokens)
print("Number of tokens:", len(tokens))