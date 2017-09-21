standardLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def cleanStr(st):
    length = len(st)
    spot = 0
    result = ''
    while spot < length:
        if st[spot] in standardLetters:
            result += st[spot]
        spot += 1
    return result
again = 'y'
while again[0] == 'y' or again[0] == 'Y':
    inp = input("What string would you like cleaned? ")
    print("You typed", inp)
    print("Your cleaned string is ", cleanStr(inp), ".", sep="")
    again = input("Would you like to try again? ")
