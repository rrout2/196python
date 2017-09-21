standardLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def cleanStr(st):
    length = len(st)
    spot = length - 1;
    while spot >= 0:
        if st[spot] not in standardLetters:
            st = st.replace(st[spot], "")
            length -= 1
        spot -= 1
    return st


def is_anagram(s1, s2):
    st2 = cleanStr(s2)
    st1 = cleanStr(s1)
    for spot in range(len(st1)):
        if not (st1[spot].lower() in st2.lower()):
            return False
        else:
            st2 = st2.replace(s1[spot], "")
        if len(st2) > 0:
            return False
    return True


out = is_anagram("listen", "silent")
print(out)
