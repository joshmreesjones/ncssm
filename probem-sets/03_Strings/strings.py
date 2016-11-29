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
    if ':' in time:
        hourtime = int(time[0:time.find(':')])
        minutestring = time[time.find(':') + 1:time.find(' ')]
        AMPM = time[time.find(' ') + 1:]
    else:
        return "Could not parse time."
    
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

# def elevationANgle3G(a, b):
#
#
#
#
#

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

def bostonize(phrase):
    return phrase.replace('r', 'a')

def isSuffix(string1, string2):
    return string1 == string2[-len(string1):]

def isPrefix(string1, string2):
    return string1 == string2[:len(string1)]

def isDufix(string1, string2):
    return isPrefix(string1, string2) and isSuffix(string1, string2)

def insertBefore(letter, string, index):
    return string[:string.find(index)] + letter + string[string.find(index):]

def dropCharAt(index, string):
    return string[:index] + string[index + 1:]

def drop(letter, string):
    return string.replace(letter, '')

def pigLatin(string):
    return string[1:] + string[0] + 'ay'

def eCoR1(string):
    return string[:string.find('GAATTC') + 1], string[string.find('GAATTC') + 1:]

def antisense(string):
    return string.replace('T', 'a').replace('A', 't').replace('C', 'g').replace('G', 'c').replace('t', 'T').replace('a', 'A').replace('c', 'C').replace('g', 'G')

def toSciNo(num): # other name used for testing - easier to type toSciNo
    e = 0
    while not (1 <= num < 10):
        if 0 < num < 1:
            num *= 10
            e -= 1
        elif num == 0:
            break
        elif num >= 10:
            num /= 10
            e += 1
    print(str(num) + 'e' + str(e))

toScientificNotation = toSciNo # assign toSciNo function to long version

def toFloat(string):
    if ' ' in string:
        number = int(string[:string.find(' ')])
        numerator = int(string[string.find(' ') + 1:string.find('/')])
        denominator = int(string[string.find('/') + 1:])
        return number + (numerator / denominator)
    elif not ' ' in string:
        if '/' in string:
            numerator = int(string[:string.find('/')])
            denominator = int(string[string.find('/') + 1:])
            return numerator / denominator
        elif not '/' in string:
            return int(string)

#def formatDate(date):
    #

def formatSSN(num):
    SSN = str(num)
    if len(SSN) == 9:
        return '#' + SSN[0:3] + '-' + SSN[3:5] + '-' + SSN[5:9]
    else:
        return 'Invalid social security number'
