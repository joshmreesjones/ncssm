#	AP Computer Science A (I)
#	Functions problem set
#	Josh Rees-Jones
#	ncssm.edu/~yeh/hw/Functions1.html

"""
Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 180 * (1000 - 2)
179640
>>> 43297 % 34
15
>>> .5 * 7842 * 2342
9182982.0
>>> from math import *
>>> (4/3) * pi * (1 ** 3)
4.1887902047863905
>>> a = 3
>>> b = -6
>>> c = -8
>>> radical = sqrt((b ** 2) - (4 * a * c))
>>> (-b + radical) / (2 * a)
2.914854215512676
>>> (-b - radical) / (2 * a)
-0.9148542155126762
>>> 
"""

from math import *



def nGonAngleSum(sides):
	sum = 180 * (sides - 2)
	return sum



def remainder(a, b):
	remainder = a % b
	return remainder



def triangleArea(base, height):
	area = .5 * base * height
	return area



def sphereVolume(radius):
	return 4/3 * pi * (radius ** 3  )



def radical(a, b, c):
	return sqrt(b**2 - 4 * a * c)



def quadraticEquation(a, b, c):
	solution1 = (-b + radical(a, b, c)) / (2 * a)
	solution2 = (-b - radical(a, b, c)) / (2 * a)
	return (solution1, solution2)



def triangleArea360(a, b, c):
	s = .5 * (a + b + c)
	area = sqrt(s * (s - a) * (s - b) * (s - c))
	return area



def magnitude(x, y):
	return sqrt(x ** 2 + y ** 2)



def mitosis(object):
	return (object, object)



# quadraticEquation already defined; quadratic assigned to the same function object as quadraticFunction
quadratic = quadraticEquation



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



def circumCenter(x1, y1, x2, y2, x3, y3):
	perpBisector1 = perpBisector(x1, y1, x2, y2)
	slope1, b1 = perpBisector1[0], perpBisector1[1]
	perpBisector2 = perpBisector(x2, y2, x3, y3)
	slope2, b2 = perpBisector2[0], perpBisector2[1]
	x = (b2 - b1) / (slope1 - slope2)
	y = slope1 * x + b1
	return (x, y)



def isDivisible(a, b):
	return False if a % b else True



def isEven(num):
	return False if num % 2 else True



def nand(bool1, bool2):
	return not (bool1 and bool2)



def onePair(a, b, c):
	# if a, b, and c are all equal, return false
	return False if (a == b) and (a == c) and (b == c) or (a != b) and (a != c) and (b != c) else True



def mantissa(num):
	return num - int(num)


def combine3Digits(a, b, c):
	return int(str(a) + str(b) + str(c))



def lastDigit(num):
	return int(str(num)[-1])



def numDigits(num):
	return int(log(num,10)) + 1



def leadingDigit(num):
	return int(str(num)[:1])



def minutesElapsed(h1, m1, h2, m2):
	minutes1 = h1 * 60 + m1
	minutes2 = h2 * 60 + m2
	return minutes2 - minutes1

def precision(num):
	return len(str(num).split(".")[1])

def unscaledValue(num):
	return int(int(num) * (10 ** precision(num)) + (num - int(num)) * (10 ** precision(num)))

def solveAngle(a, b, c):
	return acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

def solveTriangle(a, b, c):
	return solveAngle(b, c, a), solveAngle(c, a, b), solveAngle(a, b, c)

def intersect(slope1, b1, slope2, b2):
	x = (b2 - b1) / (slope1 - slope2)
	y = slope1 * x + b1
	return x, y

def interpolate(a, b, c):
	return (b - a) * c + a

def areIncreasing(a, b, c):
	return True if a < b and b < c else False

def exactlyTwoDigits(num):
	return True if sqrt(num ** 2) >= 10 and sqrt(num ** 2) < 100 else False

def nor(bool1, bool2):
	return not (bool1 or bool2)

def xor(bool1, bool2):
	return True if bool1 + bool2 == 1 else False

def validTriangle(side1, side2, side3):
	return True if (side3 < side1 + side2) and (side1 < side2 + side3) and (side2 < side3 + side1) else False
