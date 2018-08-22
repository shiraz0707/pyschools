'''
#Compute the area and perimeter of a circle with radius = 3
pi = 3.14
area =
perimeter =
'''

def findArea(radius):
	area_of_circle = pi * radius**2
	return area_of_circle 

def findPerimiter(radius):
	perimeter_of_circle = 2 * pi * radius
	return perimeter_of_circle

radius = 3
pi = 3.14

print findArea(radius)
print findPerimiter(radius)

