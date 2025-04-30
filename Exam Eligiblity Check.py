medical_cause = input("Did you have a medical cause? Yes or No: ")
atten = int(input("Enter the attendance of the student: "))
if medical_cause == 'Yes':
    print("You are allowed.")
else:
    if atten >= 75 :
        print("allowed")
    else:
        print("Not allowed.")