x = True
while x:
    try:
        enter = int(input("Please enter an integer value : "))
        x = False
    except:
        pass
while not(isinstance(enter, int)):
    enter = input("Please enter an integer value : ")
print('You entered', enter)