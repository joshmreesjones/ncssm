"""
    Here, I have condensed the problem set to one line
    per function (including primeFactorization). It's
    not pretty, but it's awesome.
"""
def rangeProduct(x,y): return x if x == y else (x * rangeProduct(x + 1, y))
def digitalRoot(num): return num if num < 10 else (digitalRoot(digitalRoot(num // 10) + num % 10))
def primeFactorization(num): return [] if num == 1 else ([num] if len([(test if num % test == 0 else None) for test in range(2, int((num ** 0.5) + 1))]) == 0 else [[(test if num % test == 0 else None) for test in range(2, int((num ** 0.5) + 1))][0]] + primeFactorization(num // [(test if num % test == 0 else None) for test in range(2, int((num ** 0.5) + 1))][0]))
def format(num): return str(num) if num < 1000 else (format(num // 1000) + ',' + str(num % 1000))
def count(char, string): return 0 if string == '' else ((1 if char == string[0] else 0) + count(char, string[1:]))
def isSubset(subset, string): return True if subset == '' else ((subset[0] in string) and (isSubset(subset[1:], string)))
def implode(list_): return 0 if list_ == [] else (10 * implode(list_[:-1]) + list_[-1])
def sort(list_): return [] if list_ == [] else ([min(list_)] + sort(list_[:list_.index(min(list_))] + list_[list_.index(min(list_)) + 1:]))

"""
    Here's the readable version!
"""

def rangeProduct(x, y):
    if x == y:
        return x
    else:
        return x * rangeProduct(x + 1, y)

def digitalRoot(num):
    if num < 10:
        return num
    else:
        return digitalRoot(digitalRoot(num // 10) + num % 10)

def primeFactorization(num):
    factor = None
    if num == 1: # 1 is a special case
        return []
    for test in range(2, int((num ** 0.5)) + 1):
        if num % test == 0:
            factor = test
            break
    if factor == None:
        return [num]
    else:
        return [factor] + primeFactorization(num // factor)            

def format(num): # format is a keyword! We just lost its functionality. :(
    if num < 1000:
        return str(num)
    else:
        return format(num // 1000) + ',' + str(num % 1000)

def count(char, string):
    if string == '':
        return 0
    else:
        return (1 if char == string[0] else 0) + count(char, string[1:])

def isSubset(subset, string):
    if subset == '':
        return True
    else:
        return (subset[0] in string) and (isSubset(subset[1:], string))

def implode(list_):
    if list_ == []:
        return 0
    else:
        return 10 * implode(list_[:-1]) + list_[-1]

def sort(list_):
    if list_ == []:
        return []
    else:
        minLocation = list_.index(min(list_))
        return [min(list_)] + sort(list_[:minLocation] + list_[minLocation + 1:])