def exponent (x):
	n = 1
	mone = 1.0
	mahane = 1
	a = 1
	while n <= 150:
		mone = mone * x
		mahane = mahane * n
		a = a + (mone/mahane)
		n = n + 1
	return a

def Ln (x):
	if (x <= 0.0):
		return 0.0
	yi = x - 1.0
	while True:
		yi_1 = yi + 2 * ((x - exponent(yi)) / (x + exponent(yi)))
		if (yi - yi_1 >= 0):
			if (yi - yi_1 < 0.000001):
				break
		else:
			if (yi - yi_1 > -0.000001):
				break
		yi = yi_1
	return yi

def XtimesY (x , y):
	if (x < 0.0):
		return 0.0
	return exponent(y * Ln(x))


def sqrt (x , y):
	try:
		return XtimesY (y , (1/x))
	except:
		return 0.0

def calculate (x):
	print (exponent (x) * XtimesY (7.0 , x) * XtimesY (x , -1) * sqrt (x , x))


x = float(input("give x "))

calculate (x)










#if (x < 0.0):
#		if (y - int(y) != 0.0):
#			print (y)
#			print (int(y))
#			print (y - int (y))
#			if (((y * 10)/2) - int (((y * 10)/2)) != 0.0):
#				print ("the answer is complex number")
#				return 0.0
#			else:
#				return pow
#		elif ((y/2) - int(y/2) != 0.0):
#			return -1 * pow
#		else:
#			return pow
#	else:
#		return pow


#y = float(input("give y "))
#pow = sqrt (x , y)
#pow = XtimesY(x , y)
#print (pow)