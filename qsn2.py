# create Empty dog dictionary
dog={
}

# Add name, Color, legs,breed,age to dog dictionary
dog["name"]="Brownie"
dog["color"]="Peach"
dog["legs"]=4
dog["breed"]="Pitbull"
dog["age"]=8


#Create Student dictionary firstname, lastname,Gender,Age,Maritalstatus,Skills,Country,City,Address
student={
    "first_name":"Sheshwanth",
    "last_name":"Gundeti",
    "gender":"Male",
    "age":24,
    "marital_status":"Single",
    "skills":["Python","C Programing","Testing"],
    "country":"India",
    "city":"Nizamabad",
    "address":"Subhash Colony"
}


#Get the length of the student dictionary

length=len(student)
print("The length of student dictionary is : \n{}".format(length))

#Get the value of the skills and check the data type ,it should be list
x=[]
x=student["skills"]
print("The skills are : {} \n".format(x))
print("Type of skills is : {} \n ".format(type(x)))


#Modify the skills by adding one or two skills

student["skills"].append("R Language")
print("The updated skills :{} \n".format(student["skills"]))

#get the dictionary keys as a list

Student_keys=list(student.keys())
Dog_keys=list(dog.keys())

print("The keys are of student dictionary are : {} \n".format(Student_keys))
print("The keys are of dog dictionary are : {} \n".format(Dog_keys))


#get the dictionary values a list

student_values=list(student.values())
dog_values=list(dog.values())

print("The values of student dictionary are : {} \n".format(student_values))
print("The values of dog dictionary are : {} \n".format(dog_values))