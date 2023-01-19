total = input("Enter the bill total-> ")
percentage = input("Enter the Tip Percentage-> ")
people = input("Enter number of people-> ")
hundred = 100
total = float(total)
percentage = int(percentage)
people = int(people)

# print(total)
# print(percentage)
# print(people)
# print(hundred)

pay = (total * (percentage / hundred)) / people

print("Each person should pay ", float(pay)) 
# print(pay)