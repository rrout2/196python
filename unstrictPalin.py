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
