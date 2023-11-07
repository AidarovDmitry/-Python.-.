text = list(input())
text[0] = text[0].upper()
for letter in range(len(text) - 1):
    if text[letter] in '.?!':
        text[letter + 2] = text[letter + 2].upper()
print(''.join(text))
