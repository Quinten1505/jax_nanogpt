with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("The file contains this amount of characters: ", len(text))

# Here are all the unique characters in the file
chars = sorted(list(set(text)))
vocab_size = len(chars)
print("".join(chars))
print(vocab_size)

# create a mapping from characters to indices
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encoder = lambda s: [stoi[c] for c in s]
decoder = lambda x: ''.join([itos[i] for i in x])

print(encoder('hello'))
print(decoder(encoder('hello')))