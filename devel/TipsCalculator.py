#Said Moussadeq
#Tip calculator
def badService(mealPrice, percentage):
   return mealPrice * .15 + mealPrice 

def goodService(mealPrice, percentage):
   return mealPrice * .18 + mealPrice

def excellentService(mealPrice, percentage):
   return mealPrice * .20 + mealPrice


print("How was your service?")
print("1.bad service")
print("2.good service")
print("3.excellent service")

choice = input("Enter choice(1/2/3):")

mealPrice = int(input("what is the total of your meal? "))
percentage = int(input("what percentage would you like to tip 15, 18 or 20: "))

if choice == '1':
   print("Sorry about your bad service. Your total will be", badService(mealPrice, percentage), "$")

elif choice == '2':
   print("We are happy to hear that you had a good service! Your total will be", goodService(mealPrice, percentage), "$")

elif choice == '3':
   print(" We are happy to hear that you had fantastic service! Your total will be", excellentService(mealPrice, percentage), "$")

else:
   print("Invalid input")
