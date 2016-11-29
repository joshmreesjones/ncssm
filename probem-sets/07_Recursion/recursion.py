def printNest ( nest ) :
 asStr = str(nest)
 width = len(asStr)
 charmap = [' ' * width]
 def write ( s , r , c , charmap) :
  while len(charmap) <= r :
    charmap += [' ' * width]
  row = charmap[r]
  charmap[r] = row[:c] + s + row[c+len(s):]
 depth = -1
 i = 0
 while i < width :
  ch = asStr[i]
  if ch == '[' :
   depth += 1
  write ( ch , depth , i , charmap )
  if ch == ']' :
   depth -= 1
  i += 1
 print (charmap[0])
 for row in charmap[1:] :
   print ('\n'+row)

def isList ( exp ) :
  return type(exp) == type([])

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def pascal(row, column):
    if column == 1:
        return 1
    elif column == row:
        return 1
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)

def euclidGCD(num1, num2):
    if num2 == 0:
        return num1
    else:
        return euclidGCD(num2, num1 % num2)

def quickExpt(base, exp):
    if exp == 1:
        return base
    else:
        return base * quickExpt(base, exp - 1)

def log(base, num):
    if num / base < 1:
        return 0
    else:
        return 1 + log(base, num / base)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def digitalRoot(num):
    if num < 10:
        return num
    else:
        return digitalRoot(digitalRoot(num // 10) + num % 10)

def primeFactorization(num):
    factor = None
    if num == 1:
        return []
    for test in range(2, int((num ** 0.5)) + 1):
        if num % test == 0:
            factor = test
            break
    if factor == None:
        return [num]
    else:
        return [factor] + primeFactorization(num // factor)

def onePath(matrix, row, column):
    if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]):
        return None
    elif row == 0 and column == len(matrix[0]) - 1:
        return []
    elif matrix[row][column] == 0:
        return None
    else:
        if onePath(matrix, row - 1, column) != None:
            return ['up'] + onePath(matrix, row - 1, column)
        elif onePath(matrix, row, column + 1) != None:
            return ['rt'] + onePath(matrix, row, column + 1)

def isFlat(list_):
    if len(list_) == 0:
        return True
    else:
        return isFlat(list_[1:]) and not isinstance(list_[0], list)

def nestSum(item):
    if isinstance(item, list):
        total = 0
        for x in item:
            if not isinstance(x, list):
                total += x
            else:
                total += nestSum(x)
        return total
    else:
        return item

def countAtoms(item):
    if isinstance(item, list):
        total = 0
        for x in item:
            if not isinstance(x, list):
                total += 1
            else:
                total += countAtoms(x)
        return total
    else:
        return 1

def nestMax(item):
    compare = []
    if not isinstance(item, list):
        return item
    else:
        for x in item:
            if not isinstance(x, list):
                compare.append(x)
            else:
                compare.append(nestMax(x))
    return max(compare)

def flatten(item):
    flattened = []
    if not isinstance(item, list):
        return item
    else:
        for x in item:
            if not isinstance(x, list):
                flattened.append(x)
            else:
                flattened += flatten(x)
    return flattened

def clearPath(obstacle, matrix, targetx, targety):
    return clearPathH(0, 0, obstacle, matrix, targetx, targety)

def clearPathH(x,y,obstacle, matrix, targetx, targety):
    print(x, y)
    if x < 0 or x > len(matrix) or y < 0 or y > len(matrix[0]):
        return None
    elif targetx == 0 and targety == 0:
        return None
    elif matrix[targetx][targety] == obstacle:
        return None
    elif (x, y) == (targetx, targety):
        return []
    else:
        if clearPathH(x + 1, y, obstacle, matrix, targetx, targety) != None:
            return [matrix[x][y]] + clearPathH(x + 1, y, obstacle, matrix, targetx, targety)
        elif clearPathH(x, y + 1, obstacle, matrix, targetx, targety) != None:
            return [matrix[x][y]] + clearPathH(x, y + 1, obstacle, matrix, targetx, targety)

def findSum(num, values):
    index = 0
    if num == 0:
        return []
    elif len(values) == 0:
        return None
    elif num < 0:
        return None
    while index < len(values):
        t = findSum(num - values[index], values[:index] + values[index + 1:])
        if t != None: return [values[index]] + t
        index += 1

#def findAllSums(num, values):
    # um, no idea

def merge(list1, list2):
    merged = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            merged.append(list1[0])
            del list1[0]
        elif list2[0] < list1[0]:
            merged.append(list2[0])
            del list2[0]
        elif list1[0] == list2[0]:
            merged.append(list1[0])
            del list1[0]
            merged.append(list2[0])
            del list2[0]
    merged = merged + list1 + list2
    return merged

def sort(list_):
    if list_ == []:
        return []
    else:
        minLocation = list_.index(min(list_))
        return [min(list_)] + sort(list_[:minLocation] + list_[minLocation + 1:])

def mergeSort(list_):
    divide = len(list_) // 2
    list1 = list_[:divide]
    list2 = list_[divide:]
    return merge(sort(list1), sort(list2))

def nestIn(item, nest):
    if item == nest:
        return True
    elif isinstance(nest, list):
        for x in nest:
            if nestIn(item, x):
                return True
        return False
    else:
        return False

def listReverse(list_):
    if len(list_) == 1:
        return list_
    else:
        return [list_[-1]] + listReverse(list_[:-1])

def nestReverse(nest):
    nest = listReverse(nest)
    index = 0
    while index < len(nest):
        if isinstance(nest[index], list):
            nest[index] = nestReverse(nest[index])
        index += 1
    return nest

def nestFind(item, nest):
    if item == nest:
        return []
    elif isinstance(nest, list):
        index = 0
        while index < len(nest):
            if nestIn(item, nest[index]):
                return [index] + nestFind(item, nest[index])
            index += 1
        return -1
    else:
        return -1

def isomorphic(list1, list2):
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if type(list1[index]) != type(list2[index]):
            return False
        if isinstance(list1[index], list):
            if isomorphic(list1[index], list2[index]) == False:
                return False
        index += 1
    return True

nest1 = [[4],[[3,6],[],7],8]
nest2 = [[[3]] , 7 , [[5 , [9 , 2] , [[[[[4]] , 2]]]]]]
nest3 = [[5],[[3,9],[],7],2]

def pillage(nest):
    result = []
    index = 0
    while index < len(nest):
        if isinstance(nest[index], list):
            result.append(pillage(nest[index]))
        index += 1
    return result

def combinations(string, length):
    if length == 0:
        return ['']
    else:
        result = []
        i = 0
        while i < len(string):
            for char in combinations(string[i+1:], length-1):
                result.append(string[i] + char)
            i += 1
        return result

#print(combinations ( 'unicorN' , 8 ))
#print(combinations ( 'unicorN' , 0 ))
#print(combinations ( 'unicorN' , 1 ))
print(combinations ( 'unicorN' , 2 ))
print('\n\n')
print(combinations ( 'unicorN' , 3 ))
#print(combinations ( 'unicorN' , 6 ))
#print(combinations ( 'unicorN' , 7 ))

def depth(nest):
    index = 1
    for x in nest:
        if isinstance(x, list):
            index += depth(x)
    return index

def nestMap(function, nest): #function thinks I only give it one argument...
    result = []
    for x in nest:
        if isinstance(x, list):
            result.append(function(nestMap(x)))
        else:
            result.append(function(x))
    return result

def align(function, nest1, nest2):
    index = 0
    result = []
    while index < len(nest1):
        if isinstance(nest1[index], list):
            result.append(align(function, nest1[index], nest2[index]))
        else:
            result.append(function(nest1[index], nest2[index]))
        index += 1
    return result

#def allnTupleSums(num, values):
    #no idea...

#def diagonalInsert(char, list_):
    #Hmm...

def addSingleton(char, list_):
    return [char] + list_

def partitions(string, items):
    # I don't have a clue! Is this bad?
