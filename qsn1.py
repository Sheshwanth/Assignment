age=[19,22,19,24,20,25,26,24,25,24]

#sort

age.sort()
print("The sorted age is: \n{} ".format(age))

#min & max using min and max functions

min=min(age)
max=max(age)
print("The minimum age is {} and maximum age is {} \n".format(min,max))


#Append min and max age to the list with method.
age.append(min)
age.append(max)
print("Age after appending the minimum and maximum age is :\n {}".format(age))


#median

count=len(age)
median=int(count/2)
print("Median is : {}".format(age[median]))

#Average

total=sum(age)
average=total/count
print("Average is : {}".format(average))

#Range

range=max-min
print("Range is : {}".format(range))