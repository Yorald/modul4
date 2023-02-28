def palindrome_check(word):
    word_backwards = []
    for i in word[::-1]:
        word_backwards.append(i)
    print(word_backwards)
    word_backwards_string = "".join(word_backwards)
    print(word_backwards_string)
    if word_backwards_string == word:
        print("To słowo jest palindromem!")
    else:
        print("To słowo NIE jest palindromem!")    

palindrome_check("kajak")
    

