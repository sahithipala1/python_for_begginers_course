# if_else basics

temperature = 35

if temperature > 40:
    print("temperature is hot today")
elif temperature > 25:
    print("temperature is cold today")

# weight

weight = int(input(" Please enter your weight:"))
unit = input(" is it in (k)kg or (l)lbs: ")

if unit.upper == "k":
    converted = weight / 0.45
    print("Weight in lbs is:" + str(converted))
else:
    converted = weight * 0.45
    print(" weight in kilo is:" + str(converted))
