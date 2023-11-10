def is_palindrom(word):
    for symbol in word :
        if not symbol.isalpha():
            return False

    for i in range(len(word) // + 1):
        if word[i] != word[-i-1]:
            return False
    return True
print(is_palindrom(input('Введите слово>>> ')))
