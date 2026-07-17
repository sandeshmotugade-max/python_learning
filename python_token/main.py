import tiktoken

encode= tiktoken.get_encoding("cl100k_base")
text = input("Enter text to generate tokens:")

tokens = encode.encode(text)

print("Text:", text)
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))