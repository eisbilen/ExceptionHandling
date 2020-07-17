len("data") == 4
#len("data") = 4

for k in range(10):
    print(k)
#fr k in range(10):
#    print(k)

print (4 + 4)
#print ('4' + 4)


try:
    #code to monitor
    print (5/0)

    #this code will not be executed
    #as above line raises a ZeroDivisionError
    print ("this code will not be executed")

except ZeroDivisionError as e:
    #code to handle the exception when it occurs
    print(e)
    print("OPPS")

else:
    print("try block executed with no error")

finally:
    print("finally block is always executed")


try:
    #code to monitor
    print (5/0)

    #this code will not be executed
    #as above line raises a ZeroDivisionError
    print ("this code will not be executed")

except ZeroDivisionError as e:
    #code to handle the exception when it occurs
    print(e)
    print("OPPS")

student_age = 8

if student_age < 2:
    raise Exception("Sorry, student age cannot be lower than 2")


class InvalidStudentAgeException(Exception):
    """Exception for errors in the student age

     Attributes:
        student_age -- student_age that we monitor
        error_message -- explanation of the error
    """

    def __init__(self, student_age, error_message="Student age should be in 2-10 range"):
        self.student_age = student_age
        self.error_message = error_message
        super().__init__(self.error_message + ": " + str(student_age) + " is not a valid age")


student_age = int(input("Enter Student age: "))
if not 1 < student_age < 11:
    raise InvalidStudentAgeException(student_age)