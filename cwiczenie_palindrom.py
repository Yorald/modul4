def palindrome_check(word):
    if word == word[::-1]:
        True, print("Słowo jest palindromem")
    else:
        False, print("Słowo NIE jest palindromem")
        
palindrome_check("kajak")
    

