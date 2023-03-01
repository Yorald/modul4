def palindrome_check(word):
    if word == word[::-1]:
        return True
    else:
        return False
        
palindrome_check("kajak")
    

