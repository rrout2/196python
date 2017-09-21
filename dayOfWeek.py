daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday',
              'friday', 'saturday', 'sunday']

def day_of_the_week(day, n):
    x = int(n)
    newDay = x + daysOfWeek.index(day)
    while newDay > len(daysOfWeek) - 1:
        newDay -= 7
    while newDay < 0:
        newDay += 7
    return daysOfWeek[newDay]

print (day_of_the_week('monday', 2.1))