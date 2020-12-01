height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')

bmi = int(weight)/ float(height)**2
bmi_round = round(bmi, 1)

if bmi < 18.5:
    print(f'You have a BMI of {bmi_round}. You are underweight.')
elif bmi >= 18.5 and bmi < 25:
    print(f'You have a BMI of {bmi_round}. You are normal weight.')
elif bmi >= 25 and bmi < 30:
    print(f'You have a BMI of {bmi_round}. You are overweight.')
elif bmi >= 30 and bmi < 35:
    print(f'You have a BMI of {bmi_round}. You are obese.')
else:
    print(f'You have a BMI of {bmi_round}. You are clinically obese.')