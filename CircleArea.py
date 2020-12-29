'''
Write a Python program which accepts the radius of a circle from the user and compute the area.
r = 1.1
Area = 3.8013271108436504
'''
import math

'''
Declare function that calculates a circle's area given the radius
'''
# Declare function header
def area_of_circle(r):
    # calculate area
    ans = math.pi*r**2
    
    # return area
    return ans

# Display instruction to user
print ('this program calculates the area of a circle')
# Get radius from user
radius = input('radius:')
radius = float(radius)
# call function to calculate area
area = area_of_circle(radius)
# display area
print('the area of the circle is ',round(area, 2) )