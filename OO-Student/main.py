from Student import Student

michael = Student( "Michael", "Miller", 22 )

michael.printInfo();
print( "Graduation title:", Student.graduationTitle )
num = michael.addOneYear();
#num += 5
#print(f"Num: {num}\nAge: {michael.age}")
michael.addSomeYears( 5 )
michael.printInfo()

#julie.age = 20
#print( michael.firstName, michael.lastName, michael.age )
#Student.graduationTitle = "Software Developer"
#print( michael.graduationTitle )
#print( julie.firstName, julie.lastName, julie.age )
#print( julie.graduationTitle )