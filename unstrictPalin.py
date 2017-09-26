standardLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def is_palindrome(s):
    front = 0
    back = len(s) - 1
    half = int(len(s)/2)
    while front < half:
        while s[front] not in standardLetters:
            front += 1
        while s[back] not in standardLetters:
            back -= 1
        if not(s[back].lower() == s[front].lower()):
            return False
        front += 1
        back -= 1

    return True
