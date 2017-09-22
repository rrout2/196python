daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 
              'friday', 'saturday', 'sunday']

def day_of_the_week(day, n):
    newDay = n + daysOfWeek.index(day)
    while newDay > len(daysOfWeek) - 1:
        newDay %= 7
    return daysOfWeek[newDay]

again = 'y'
while again[0] == 'y' or again[0] == 'Y':
    d = input("What day? (enter as lowercase) : ")
    while d not in daysOfWeek:
        d = input("Please enter a lowercase day : ")

    x = True
    while x:
        try:
            num = int(input("How many days later? "))
            x = False
        except:
            pass

    print('In ', num, ' days, it will be ', day_of_the_week(d, num), '.', sep = '')
    again = input("Would you like to try again? ")
