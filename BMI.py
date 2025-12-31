height=int(input("Enter your Height in cm"))
weight=int(input("Enter your Weight in kg"))
bmi=weight/(height/100)**2
print(bmi)
if(bmi<=18.4):
    print("You are underweight")
elif(bmi<=24.9):
    print("You are healthy")
elif(bmi<=29.9):
    print("You are overweight")
elif(bmi<=34.9):
    print("You are severely overweight")
else:
    print("Your obiese")