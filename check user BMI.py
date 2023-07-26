#user input the his weight in kg  and height in cm
Weight= float(input("Enter your weight in Kg:"))

Height= float(input("Enter your height in cm:"))

#convert from cm to m
Height_m= Height/ 100
#input the BMI rule to get user BMI after inputing his weight and height and print it out 
BMI=(Weight/(Height_m)**2)
print(BMI)

#take the result of user BMI and compared with this coditions to know if under or over weight or normal or Obses 
if (BMI<18.5):
    print("Underweight")

elif (18.5<=BMI<25.0):
    print("Normal")

elif (25.0<=BMI<30.0):
    print("Overweight")

elif (BMI<=30.0):
    print("Obese")