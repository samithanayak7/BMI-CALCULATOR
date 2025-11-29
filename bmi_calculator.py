name=input("Enter your name: ")
gender=input("Enter your gender: ")
height=int(input("Enter your height in cms: "))
weight=int(input("enter your weight in kgs: "))
bmi=((weight*10000)/(height)**2)
print(f"BMI: {bmi:.1f}")
if bmi>0:
    if (bmi<18.5):
        print(f"{name}, you are underweight!")
    elif (bmi<=24.9):
        print(f"{name}, you are normal weight!")
    elif (bmi<=29.9):
        print(f"{name}, you are overweight!")
    elif (bmi<=34.9):
        print(f"{name}, you are obese!")
    elif (bmi<=39.9):
        print(f"{name}, you are severely obese!")
    elif (bmi>=40):
        print(f"{name}, you are morbidly obese!")
else:
    print("Please enter valid inputs")