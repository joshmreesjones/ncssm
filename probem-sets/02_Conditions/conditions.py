from math import *

def larger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return None
    else:
        return None

def largest3(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c

def californicate(word):
    return word + 'a'

def snoopify(word):
    return word + 'izzle'

def firstChar(word):
    return word[0]

def lastChar(word):
    return word[-1]

def dropFirst(word):
    return word[1:]

def dropLast(word):
    return word[:-1]

def splitAt(word, index):
    return word[:index], word[index:]

def isPrefix(prefix, word):
    return True if prefix == word[:len(prefix)] else False

def insertAfter(new, word, letter):
    index = word.find(letter) + 1
    return word[:index] + new + word[index:]

def insertAt(new, word, index):
    return word[:index] + new + word[index:]

def sandwich(a, b):
    return a + b + a

def toRNA(string):
    return string.replace("T", "U")

def to12hr(time):
    hournum = int(time[0:2])
    minutenum = int(time[2:4])
    
    if not (0 <= hournum <= 24):
        return 'illegal time'
    elif not (0 <= minutenum < 60):
        return 'illegal time'
    
    if hournum == 0:
        hourtime = 12
    elif 1 <= hournum <= 12:
        hourtime = hournum
    elif 13 <= hournum <= 24:
        hourtime = hournum - 12
    
    minutetime = minutenum
    
    if 0 <= hournum <= 11 or hournum == 24:
        AMPM = 'AM'
    elif 12 <= hournum <= 23:
        AMPM = 'PM'

    hourstring = str(hourtime)
    
    if minutetime < 10:
        minutestring = '0' + str(minutetime)
    elif minutetime >= 10:
        minutestring = str(minutetime)
    
    return hourstring + ':' + minutestring + ' ' + AMPM

def to24hr(time):
    hourtime = int(time[0:time.find(':')])
    minutestring = time[time.find(':') + 1:time.find(' ')]
    AMPM = time[time.find(' ') + 1:]
    
    if (not (AMPM == 'AM')) and (not (AMPM == 'PM')):
        return 'illegal time - AMPM'
    elif not (1 <= hourtime <= 12):
        return 'illegal time - hourtime'
    elif not (0 <= int(minutestring) <= 59):
        return 'illegal time - minutestring'
    elif len(minutestring) != 2:
        return 'illegal time - minutestring'
    
    if AMPM == 'AM':
        if hourtime == 12:
            hourstring = '00'
        elif 1 <= hourtime <= 9:
            hourstring = '0' + str(hourtime)
        elif 10 <= hourtime <= 11:
            hourstring = str(hourtime)
    elif AMPM == 'PM':
        if hourtime == 12:
            hourstring = str(hourtime)
        elif 1 <= hourtime <= 9:
            hourstring = str(hourtime + 12)
        elif 10 <= hourtime <= 11:
            hourstring = str(hourtime + 12)

    return hourstring + minutestring

def xterm(coefficient):
    if coefficient == 0:
        return ""
    elif coefficient == 1:
        return "x"
    elif coefficient == -1:
        return "-x"
    else:
        return str(coefficient) + "x"

def yterm(b):
    if b < 0:
        return ' - ' + str(abs(b))
    elif b == 0:
        return ''
    elif b > 0:
        return ' + ' + str(b)

def formatLine(m, b):
    return 'y = ' + xterm(m) + yterm(b)

def elevationANgle3G(a, b):
    return 'I was told not to worry about this since I don\'t know the math behind it.'

def saffirSimpson(wind):
    if 30 <= wind < 50:
        return 'Tropical Depression'
    elif 50 <= wind < 80:
        return 'Tropical Storm'
    elif 80 <= wind < 100:
        return 'Category 1 Hurricane'
    elif 100 <= wind < 120:
        return 'Category 2 Hurricane'
    elif 120 <= wind < 150:
        return 'Category 3 Hurricane'
    elif 150 <= wind < 160:
        return 'Category 4 Hurricane'
    elif 160 <= wind:
        return 'Category 5 Hurricane'
    else:
        return 'Not very high winds...'

def sort3(a, b, c):
    if a < b < c:
        return a, b, c
    elif a < c < b:
        return a, c, b
    elif b < a < c:
        return b, a, c
    elif b < c < a:
        return b, c, a
    elif c < a < b:
        return c, a, b
    elif c < b < a:
        return c, b, a

def filterOdds(a, b):
    if a % 2 == 1:
        returnA = True
    else:
        returnA = False
    if b % 2 == 1:
        returnB = True
    else:
        returnB = False

    if returnA and (not returnB):
        return a
    if (not returnA) and returnB:
        return b
    if (not returnA) and (not returnB):
        return None
    if returnA and returnB:
        return a, b

def letterGrade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def plusMinus(grade):
    _range = grade % 10
    if 0 <= _range <= 3:
        return '-'
    if 3 < _range < 7:
        return ''
    if 7 <= _range < 10:
        return '+'

def completeGrade(grade):
    return letterGrade(grade) + plusMinus(grade)

def radical(a, b, c):
    return b**2 - 4 * a * c

def imaginary(a, b, c):
    part1 = str(-b)
    
    if radical(a, b, c) != -1:
        part2 = str(radical(a, b, c)) + 'i'
    elif radical(a, b, c) == -1:
        part2 = 'i'

    solution1 = part1 + ' + ' + part2
    solution2 = part1 + ' - ' + part2
    return solution1, solution2
#Having trouble with imaginaries and would rather work on building GUIs :)


def quadratic(a, b, c):
    if radical(a, b, c) >= 0:
        solution1 = str((-b + sqrt(radical(a, b, c))) / (2 * a))
        solution2 = str((-b - sqrt(radical(a, b, c))) / (2 * a))
    elif radical(a, b, c) < 0:
        solution1 = imaginary(a, b, c)[0]
        solution2 = imaginary(a, b, c)[1]

    if solution1 != solution2:
        return solution1, solution2
    elif solution1 == solution2:
        return solution1

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return (x, y)

def slope(x1, y1, x2, y2):
    slope = (y1 - y2) / (x1 - x2)
    return slope

def perpBisector(x1, y1, x2, y2):
    slope = -((x1 - x2) / (y1 - y2))
    midX, midY = midpoint(x1, y1, x2, y2)[0], midpoint(x1, y1, x2, y2)[1]
    b = -(slope*midX) + midY
    return (slope, b)

def bisector(x1, x2, y1, y2):
    slope = perpBisector(x1, y1, x2, y2)[0]
    b = perpBisector(x1, y1, x2, y2)[1]
    return formatLine(slope, b)

def leapYears(start, end):
    leap_years = 0
    for year in range(start, end):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1
    return leap_years
