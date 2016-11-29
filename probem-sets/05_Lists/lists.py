import math

def sum(list_):
    total = 0
    for item in list_:
        total += item
    return total

def product(list_):
    result = 1
    for item in list_:
        result *= item
    return result

def maximum(list_):
    if len(list_) == 0:
        return None
    else:
        max_ = list_[0]
        for item in list_:
            max_ = item if item > max_ else max_
        return max_

def nestedSum(superList):
    total = 0
    for list_ in superList:
        for item in list_:
            total += item
    return total

def getRow(rowIndex, table):
    return table[rowIndex - 1]

def getColumn(columnIndex, table):
    return [table[0][columnIndex - 1], table[1][columnIndex - 1]]

def implode(list_):
    magnitude = 10 ** (len(list_) - 1)
    num = 0
    for item in list_:
        num += int(item * magnitude)
        magnitude /= 10
    return num

def explode(num):
    result = []
    while num > 10:
        result += [num % 10]
        num //= 10
    result += [num % 10]
    result.reverse()
    return result

def delimit(items):
    length = len(items)
    if length == 1:
        return items[0]
    elif length == 2:
        return items[0] + ' and ' + items[1]
    elif length > 2:
        string = ''
        index = 0
        while index < length - 1:
            string += items[index] + ', '
            index += 1
        string += 'and ' + items[index]
        return string

def formatPolynomial(list_):
    polynomial = ''
    terms = ['x^3 ', 'x^2 ', 'x ']
    
    if list_[0] == -1:
        polynomial += '-' + terms[0]
    elif list_[0] == 0:
        pass
    elif list_[0] == 1:
        polynomial += terms[0]
    else:
        polynomial += str(list_[0]) + terms[0]
    print('Polynomial with first term:')
    print(polynomial)
    
    index = 1
    while index <= 2:
        if list_[index] == -1:
            polynomial += '- ' + terms[index]
        elif list_[index] == 0:
            pass
        elif list_[index] == 1:
            polynomial += '+ ' + terms[index]
        elif list_[index] > 1:
            polynomial += '+ ' + str(list_[index]) + terms[index]
        elif list_[index] < -1:
            polynomial += '- ' + str(list_[index]) + terms[index]
        index += 1
    
    if list_[3] < 0:
        polynomial += '- ' + str(list_[3])
    elif list_[3] == 0:
        polynomial = polynomial[:-1] # remove the space
    elif list_[3] > 0:
        polynomial += '+ ' + str(list_[3])
    
    return polynomial

def evalPolynomial(list_, x):
    terms = [x**3, x**2, x, 1]
    total = 0
    index = 0
    while index < len(list_):
        total += list_[index] * terms[index]
        index += 1
    return total

def isPrime(num):
    for x in range(2, math.floor(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def allPrimes(count):
    index = 1
    primes = []
    number = 2
    while index <= count:
        if isPrime(number):
            primes.append(number)
            index += 1
        number += 1
    return primes

def findPrimeGap(gap):
    index = 4
    one = 2
    two = 3
    while two - one < gap:
        if isPrime(index):
            one = two
            two = index
            print(one, two)
        index += 1
    return one, two

def onesHelper(num):
    return (
        ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine'][num])

def tensHelper(num):
    if num < 10:
        return onesHelper(num)
    elif num >= 10 and num < 20:
        return ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen'][num - 10]
    elif num >= 20:
        result = ['twenty', 'thirty', 'forty', 'fifty',
                'sixty', 'seventy', 'eighty', 'ninety'][(num // 10) - 2] # -2 because index 0 starts the list with 'twenty'
        if num % 10 > 0:
            result = result + '-' + onesHelper(num % 10)
        return result

def hundredsHelper(num):
    result = ''
    if num >= 100:
        result += onesHelper(num // 100) + ' hundred'
    if num % 100 != 0:
        if num >= 100:
            result += ' ' + tensHelper(num % 100)
        else:
            result += tensHelper(num % 100)
    return result

def articulate(num): # range: 1 to (10 ** 23)
    result = ''
    if num == 0:
        return 'zero'
    names = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion',
     'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion',
     'tredecillion', 'quattuordecillion', 'quindecillion', 'sexdecillion',
     'septecillion', 'octodecillion', 'novemdecillion', 'vigintillion',
     'unvigintillion', 'duovigintillion', 'tresvigintillion', 'quattorvigintillion',
     'quinquavigintillion', 'sesvigintillion', 'septemvigintillion', 'octovigintillion',
     'novemvigintillion', 'trigintillion', 'untrigintillion', 'duotrigintillion',
     'trestrigintillion', 'quattortrigintillion', 'quinquatrigintillion', 'sestrigintillion',
     'septentrigintillion', 'octotrigintillion', 'noventrigintillion', 'quadragintillion']
    namesIndex = 0
    result += hundredsHelper(num % 1000)
    num //= 1000
    while num > 0:
        if num % 1000 != 0:
            result = hundredsHelper(num % 1000) + ' ' + names[namesIndex] + ' ' + result
        num //= 1000
        namesIndex += 1
    return result

def sort(list_):
    for i in range(1, len(list_)):
        j = i-1 
        item = list_[i]
        while (list_[j] > item) and (j >= 0):
           list_[j+1] = list_[j]
           j -= 1
        list_[j+1] = item
    return list_

def formatTable(table):
    result = ''
    for row in table:
        result += '| '
        for item in row:
            result += str(item)
            result += ' '
        result += '|\n'
    return result

def find2D(table, element):
    rowIndex = 0
    for row in table:
        if row.count(element) != 0:
            column = row.index(element)
            return rowIndex, column
        rowIndex += 1
    return -1

def isSquare(table):
    height = len(table)
    width = 0
    for row in table:
        if len(row) == height:
            pass
        else:
            return False
    return True

def flipList(list_):
    newList = []
    index = len(list_) - 1
    while index >= 0:
        newList.append(list_[index])
        index -= 1
    return newList

def flip(table):
    newTable = []
    rowIndex = len(table) - 1
    while rowIndex >= 0:
        newTable.append(flipList(table[rowIndex]))
        rowIndex -= 1
    return newTable

def diagonal(table):
    index = 0
    points = []
    for row in table:
        try:
            points.append(row[index])
            index += 1
        except:
            return points
    return points

def derivative(list_):
    index1 = 0
    index2 = 1
    differences = []
    while index2 < len(list_):
        differences.append(list_[index2] - list_[index1])
        index1 += 1
        index2 += 1
    return differences

def scale(list_, scalar):
    newList = []
    for item in list_:
        newList.append(item * scalar)
    return newList

def magnitude(list_):
    sum_ = 0
    for item in list_:
        sum_ += item ** 2
    return math.sqrt(sum_)

def addVectors(list1, list2):
    index = 0
    newList = []
    while index < len(list1):
        newList.append(list1[index] + list2[index])
        index += 1
    return newList

def dotProduct(list1, list2):
    index = 0
    products = []
    while index < len(list1):
        products.append(list1[index] * list2[index])
        index += 1
    return sum(products)

def stdDev(list_):
    mean = sum(list_) / len(list_)
    stdList = [(item - mean) ** 2 for item in list_]
    return math.sqrt(sum(stdList) / len(stdList))

def firstInterval(list_):
    stdDevValue = stdDev(list_)
    mean = sum(list_)/len(list_)
    returnList = []
    for item in list_:
        if mean-stdDevValue <= item <= mean+stdDevValue:
            returnList.append(item)
    return returnList

def frequencies(dna):
    index = 0
    frequenciesList = []
    while index < len(dna):
        frequenciesList.append(
            {'T': 0.36,
             'A': 0.18,
             'C': 0.36,
             'G': 0.09}[dna[index]])
        index += 1
    return frequenciesList
