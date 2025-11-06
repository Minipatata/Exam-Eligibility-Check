#Write a program to check whether the student can take an exam or not. 
# Students will be allowed only in two conditions: 
# If they have a medical cause (‘Y’ for yes and ‘N’ for no). 
# If yes, then they will be allowed. If No, then check attendance 
# If attendance is above 75, then allowed; otherwise, not allowed.

medical_cause=str(input("Do you have a medical cause Y | N"))
if medical_cause=="Y":
    print("Than you can take the exam")
else:
    print("No, you can not take the exam")
    attendance=int(input("Write your attendance level"))
    if attendance>75:
        print("Than you are allowed")
    else:
        print("You still can not do the exam")