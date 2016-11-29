import random
import math

def triangle(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

def sigma(num1, num2):
    total = 0
    while num1 <= num2:
        total += num1
        num1 += 1
    return total

def factorial(num):
    total = 1
    while num > 0:
        total *= num
        num -= 1
    return total

def pi(num1, num2):
    sum_ = 1
    while num1 <= num2:
        sum_ *= num1
        num1 += 1
    return sum_

def count(char, string):
    totalchars = 0
    index = 0
    while index < len(string):
        totalchars += 1 if string[index] == char else 0
        index += 1
    return totalchars

def replace(charBefore, charAfter, string):
    returnString = ''
    for char in string:
        returnString += charAfter if char == charBefore else char
    return returnString

def reverse(string):
    i = len(string) - 1
    returnString = ''
    while i >= 0:
        returnString += string[i]
        i -= 1
    return returnString

def segregate(string):
    vowelsList = 'aeiouAEIOUyY'
    consonants = vowels = ''
    for char in string:
        vowels += char if char in vowelsList else ''
        consonants += char if char not in vowelsList else ''
    return consonants, vowels

def abacab(string): # Let the inefficiency ensue
    a, b, c, d = 0, 1, 2, 3
    returnString = (
        string[a] + 
        string[b] + 
        string[a] + 
        string[c] + 
        string[a] + 
        string[b] + 
        string[a] + 
        string[d] + 
        string[a] + 
        string[b] + 
        string[a] + 
        string[c] + 
        string[a] + 
        string[b] + 
        string[a])
    return returnString

def dcdb(string):
    a, b, c, d = 0, 1, 2, 3
    returnString = (
        string[d] +
        string[c] +
        string[d] +
        string[b] +
        string[d] +
        string[c] +
        string[d] +
        string[a] +
        string[d] +
        string[c] +
        string[d] +
        string[b] +
        string[d] +
        string[c] +
        string[d])
    return returnString

def crossover(string1, string2, index):
    return string1[:index] + string2[index:], string2[:index] + string1[index:]

def merge(string1, string2):
    i = 0
    finalstring = ''
    while i < len(string1) and i < len(string2):
        finalstring += string1[i]
        finalstring += string2[i]
        i += 1
    if len(string1) > len(string2):
        return finalstring + string2[i:]
    elif len(string1) < len(string2):
        return finalstring + string1[i:]
    elif len(string1) == len(string2):
        return finalstring

def choose1337char(char): # This took a while
    if not char.isalpha() and char !=' ':
        print("The argument passed to choose1337char is not valid.")
        return
    leetA = ['4', '/-\\', '@', '^', '/\\', '//-\\\\', '/=\\']
    leetB = ['8', ']3', ']8', '|3', '|8', ']]3', '13']
    leetC = ['(', '{', '[[', '<']
    leetD = [')', '[}', '|)', '|}', '|>', '[>', ']]']
    leetE = ['3', 'ii']
    leetF = ['|=', '(=', ']]=', 'ph']
    leetG = ['6', '9', '(_>', '[[6', '&', '(_+']
    leetH = ['#', '|-|', '(-)', ')-(', '}{', '}-{', '{-}', '/-/', '\\-\\', '|~|',
                                                                 '[]-[]', ']]-[[']
    leetI = ['1', '!', '|', '][', '[]']
    leetJ = ['_|', 'u|', ';_[]', ';_[[']
    leetK = ['|<', '|{', '][<', ']]<', '[]<']
    leetL = ['|', '1', '|_', '[]_', '][_']
    leetM = ['/\\/\\', '|\\/|', '[\\/]', '(\\/)', '[]\\/[]', '\\\\\\', '(T)', '^^',
                                            '.\\\\', './/', '][\\\\//][', 'JVL']
    leetN = ['/\\/', '|\\|', '(\\)', '/|/', '[\\]', '{\\}', '][\\][', '[]\\[]', '~']
    leetO = ['0', '()', '[]', '<>', '*', '[[]]']
    leetP = ['|D', '|*', '|>', '[]D', '][D']
    leetQ = ['(,)', '0,', 'O,', 'O\\', '[]\\']
    leetR = ['|2', '|?', '|-', ']]2', '[]2', '][2']
    leetS = ['5', '$', 'z']
    leetT = ['7', '+', "']'", '7`', '~|~', '-|-', "']['", '"|"']
    leetU = ['(_)', '|_|', '\\_\\', '/_/', '\\_/', '[]_[]', ']_[']
    leetV = ['\\/', '\\\\//']
    leetW = ['\\/\\/', '|/\\|', '[/\\]', '(/\\)', 'VV', '///', '\\^/', '\\VV/',
                                                             '1/V', 'V1/', '1/1/']
    leetX = ['><', '}{', ')(', '}[']
    leetY = ["'/", '%', '`/', '\\j', '``//', 'j', '\\|/', '-/']
    leetZ = ['2', 'z', '7_', '`/_']
    leetSpace = ['  ']
    
    leetDict = {'a': leetA, 'b': leetB, 'c': leetC, 'd': leetD, # I made a script
                'e': leetE, 'f': leetF, 'g': leetG, 'h': leetH, # to generate this
                'i': leetI, 'j': leetJ, 'k': leetK, 'l': leetL, # dictionary!
                'm': leetM, 'n': leetN, 'o': leetO, 'p': leetP,
                'q': leetQ, 'r': leetR, 's': leetS, 't': leetT,
                'u': leetU, 'v': leetV, 'w': leetW, 'x': leetX,
                'y': leetY, 'z': leetZ, ' ': leetSpace}
    return leetDict[char.lower()][random.randint(0, len(leetDict[char.lower()]) - 1)]

def l337(string):
    leetString = ''
    for char in string:
        leetString += choose1337char(char)
    print("If you don't find this a suitable solution, just look at the code.")
    return leetString

def digitcount(digit, num):
    count = 0
    count += 1 if digit == num % 10 else 0
    while num >= 10:
        num //= 10
        count += 1 if digit == num % 10 else 0
    return count

def isSubset(subset, string):
    for char in subset:
        if string.find(char) == -1:
            return False
    return True

def isAbbrev(abbrev, string):
    for char in abbrev:
        if string.find(char) != -1:
            abbrev = abbrev[1:]
            string = string[string.find(char) + 1:]
        elif string.find(char) == -1:
            return False
    return True

def makeRectangle(height, width):
    rectString = ''
    tempWidth= width
    while height > 0:
        while tempWidth > 0:
            rectString += '*'
            tempWidth -= 1
        tempWidth = width
        rectString += '\n'
        height -= 1
    print(rectString)

def makePyramid(layers, element):
    pyramidString = ''
    counter = 1
    elementCounter = 1
    while counter != layers + 1:
        pyramidString += (
            (' ' * (layers - counter)) + 
            (element * elementCounter) + 
            '\n'
            )
        counter += 1
        elementCounter += 2

    return pyramidString

def isPrime(num):
    for x in range(2, math.floor(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def fibonacci(iteration):
    num1 = 0
    num2 = 1
    num2temp = 1
    while iteration > 0:
        num2temp = num2
        num2 = num1 + num2
        num1 = num2temp
        iteration -= 1
    return num1

def formatNumber(num):
    formattedString = ''
    insertIndex = -4
    while num != 0:
        print('num: ' + str(num))
        print('formattedString: ' + str(formattedString))
        print('\n')
        if num >= 1000:
            formattedString = ',' + str(num % 1000) + formattedString
        else:
            formattedString = str(num % 1000) + formattedString
        
        num //= 1000
    return formattedString

def digitalRoot(num):
    total = 0
    while True:
        total += num % 10
        num //= 10
        if num < 10:
            total += num % 10
            break
    if total >= 10:
        total = digitalRoot(total) # RECURSION! HOORAY!
    return total

def phoneNumber(string):
    newNumber = ''
    for char in string:
        if char.isalpha():
            newNumber += { #kind of like a switch in Java:
                           #http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
                    'a': '2',
                    'b': '2',
                    'c': '2',
                    'd': '3',
                    'e': '3',
                    'f': '3',
                    'g': '4',
                    'h': '4',
                    'i': '4',
                    'j': '5',
                    'k': '5',
                    'l': '5',
                    'm': '6',
                    'n': '6',
                    'o': '6',
                    'p': '7',
                    'q': '7',
                    'r': '7',
                    's': '7',
                    't': '8',
                    'u': '8',
                    'v': '8',
                    'w': '9',
                    'x': '9',
                    'y': '9',
                    'z': '9'
                }[char.lower()]
        else:
            newNumber += char
    return newNumber

def findDiagraph(string1, string2):
    index = 0
    while index < len(string1):
        if string2.find(string1[index:index+2]) == -1:
            index += 1
        else:
            return string1[index:index+2]
    return ''

def marry(string1, string2):
    diagraph = findDiagraph(string1, string2)
    if len(diagraph) == 2:
        marriedString = string1[:string1.find(diagraph)] + diagraph + string2[string2.find(diagraph) + 2:]
    elif len(diagraph) == 0:
        marriedString = string1 + string2
    return marriedString

def findFactors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors += [i]
    return factors

def isPerfect(num):
    factors = findFactors(num)
    total = 0
    for i in factors:
        total += i
    return True if total == num else False

# The next perfect number is 496!

def findPerfectNumbers():
    print('Do you want to begin finding perfect numbers?')
    result = input('[Y/N]: ')
    if result == 'N':
        return
    elif result == 'Y':
        count = 1
        while True: # This is very inefficient, but it's 3:10 AM so I am a little loopy
            if isPerfect(count): # right now and don't feel like finding a better way
                print(count)
                input('Press enter to find another.')
            count += 1

def isPalindrome(string):
    index = 0
    while index < len(string):
        if string[index] != string[::-1][index]:
            return False
        index += 1
    return True

def areAnagrams(string1, string2):
    if len(string1) != len(string2):
        return False
    for char in string1:
        if string2.find(char) == -1:
            return False
        index = string2.find(char)
        string1 = string1[1:]
        string2 = string2[:index] + string2[index + 1:]
        index += 1
    return True
