# Please run with Python 3.
# 
# Josh Rees-Jones
# Bradley King
# 
# Numerical Analysis final project

def rk4(function, x0, y0, h, steps):
	"""
	Generate a solution to the specified differential equation
	using the Runge-Kutta Order 4 method given an initial position,
	iteration width, and iteration count.
	
	Args:
		function: the differential equation to be approximated
		x0: the initial x position
		y0: the initial y position
		h: the step width
		steps: the number of iterations to run RK4
	Returns:
		the final y value
	Raises:
		ValueError: if h <= 0 or steps < 0
	"""
	
	if h <= 0:
		raise ValueError("h cannot be positive")
	
	if steps < 0:
		raise ValueError("steps must be at least 0")

	print("--== RK4 ==--")

	x, y = x0, y0
	
	for i in range(steps):
		part1 = "{0:02}".format(i)
		part2 = "{:10.4f}".format(x)
		part3 = "{:10.12f}".format(y)

		print(part1 + "\t" + part2 + "\t" + part3)

		k1 = function(x, y)
		k2 = function(x + (h/2), y + (h/2) * k1)
		k3 = function(x + (h/2), y + (h/2) * k2)
		k4 = function(x + h, y + k3 * h)
		
		y += h * (k1/6 + k2/3 + k3/3 + k4/6)
		x += h
	
	return y

def linearEuler(function, x0, y0, h, steps):
	"""
	Generate a solution to the specified differential equation
	using linear Euler's method given an initial position, iteration
	width, and iteration count.
	
	Args:
		function: the differential equation to be approximated
		x0: the initial x position
		y0: the initial y position
		h: the step width
		steps: the number of iterations to run linearEuler
	Returns:
		the final y value
	Raises:
		ValueError: if h <= 0 or steps < 0
	"""

	if h <= 0:
		raise ValueError("h cannot be positive")
	
	if steps < 0:
		raise ValueError("steps must be at least 0")
	
	print("--== Linear Euler's ==--")
	
	x, y = x0, y0

	for i in range(steps):
		part1 = "{0:02}".format(i)
		part2 = "{:10.4f}".format(x)
		part3 = "{:10.12f}".format(y)

		print(part1 + "\t" + part2 + "\t" + part3)

		y += h * function(x, y)
		x += h
		
	return y
	
def quadraticEuler(function, derFunction, x0, y0, h, steps):
	"""
	Generate a solution to the specified differential equation
	using quadratic Euler's method given an initial position, iteration
	width, iteration count, and the derivate of the specified
	differential equation.
	
	Args:
		function: the differential equation to be approximated
		derFunction: the derivative with respect to x of the specified
			differential equation
		x0: the initial x position
		y0: the initial y position
		h: the step width
		steps: the number of iterations to run RK4
	Returns:
		the final y value
	Raises:
		ValueError: if h <= 0 or steps < 0
	"""
	
	if h <= 0:
		raise ValueError("h cannot be positive")
	
	if steps < 0:
		raise ValueError("steps must be at least 0")
	
	x, y = x0, y0

	print("--== Quadratic Euler's ==--")
	
	for i in range(steps):
		part1 = "{0:02}".format(i)
		part2 = "{:10.4f}".format(x)
		part3 = "{:10.12f}".format(y)

		print(part1 + "\t" + part2 + "\t" + part3)

		y += h * function(x, y) + (h**2/2) * derFunction(x, y)
		x += h
		
	return y

# test code

def f1(x, y):
	return -x / y

def derf1(x, y):
	return (-1/y) - (x**2)



def f2(x, y):
	return x**2 + y

def derf2(x, y):
	return x**2 + 2*x + y



def f3(x, y):
	return 1

def derf3(x, y):
	return 0



def f4(x, y):
	return y

def derf4(x, y):
	return y

print("\n" * 5)

rk4(f1, 0, 3, .1, 10)
rk4(f2, 0, 3, .1, 10)
rk4(f3, 0, 3, .1, 10)
rk4(f4, 0, 3, .1, 10)

print("\n" * 5)

linearEuler(f1, 0, 3, .1, 10)
linearEuler(f2, 0, 3, .1, 10)
linearEuler(f3, 0, 3, .1, 10)
linearEuler(f4, 0, 3, .1, 10)

print("\n" * 5)

quadraticEuler(f1, derf1, 0, 3, .1, 10)
quadraticEuler(f2, derf2, 0, 3, .1, 10)
quadraticEuler(f3, derf3, 0, 3, .1, 10)
quadraticEuler(f4, derf4, 0, 3, .1, 10)

