input_text = input()
output_texts = []
opening_quotes = []
closing_quotes = []
for i in range(len(input_text) - 1):
    if input_text[i] == '(':
        opening_quotes.append(input_text.find('(', i, i + 1))
    elif  input_text[i] == ')':
        closing_quotes.append(input_text.find(')', i, i + 1))
for i in range(len(opening_quotes)):
    output_texts.append(input_text[opening_quotes[i] + 1 : closing_quotes[i]])
for text in output_texts:
    print(text)
