def palindrome_check(word):
    if word == word[::-1]:
        return True, print("Słowo jest palindromem")
    else:
        return False, print("Słowo NIE jest palindromem")
        
palindrome_check("jd")
    

