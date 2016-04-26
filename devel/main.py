# Said Moussadeq
#Tip calculator
mealPrice = input("What is the total, rounded to the nearest dollar?\n")
service = input("How was your service good, bad or excellent?\n")
tip=0

mealPrice = int(mealPrice)

if service == "good":
    percentage = input("Great! Would you like to tip 20% or 22%?\n")
    if percentage == "20%" or "20":
        tip = mealPrice * .20
    elif percentage == "22%" or "22":
        tip = mealPrice * .22
    else:
        tip = "--- please enter 20% or 22% for good service tip"
elif service == "bad":
    percentage = input("Sorry about your bad service. Would you like to tip 15% or 18%?\n")
    if percentage == "15%" or "15":
        tip = mealPrice * .15
    elif percentage == "18%" or "18":
        tip = mealPrice * .18
    else:
        tip = "--- please enter 15% or 18% for bad service tip"
elif service == "excellent":
    percentage = input("Fantastic! Would you like to tip 25% or 30%?\n")
    if percentage == "25%" or "25":
        tip = mealPrice * .25
    elif percentage == "30%" or "30":
        tip = mealPrice * .30
    else:
        tip = "--- please enter 25% or 30% for excellent service tip"
else:
    tip = " --- please enter Good, Bad, or Excellent for level of service."

tip = str(tip)
print("\nTip your server $" + tip)
