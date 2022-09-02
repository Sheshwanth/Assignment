radius_of_circle=30

#area of a circle
area_of_circle=3.14*radius_of_circle**2
print("The area of circle 1 is {}".format(area_of_circle))

#circumference of a circle
circum_of_circle=2*3.14*radius_of_circle
print("The circumference of  circle 1 is {}".format(circum_of_circle))

#taking radius as user input and calculate the area
radius=float(input("Enter the radius "))
def area(radius):
    area_of_circle2=3.14*radius**2
    print("The area of circle 2 is {}".format(area_of_circle2))
area(radius)