# Day 2 - 100 Days of Code by Angela Yu - Udemy
# This is Day 2 project on the course. A Tip Calculator.

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
#Getting the amount of the bill
bill = float(input("What was the total bill?\n"))

#Getting the amount of the tip 
tip = 1.0 + float(input("What percentage tip would you like to give? 10, 12 or 15?\n")) / 100

#Getting the amount of friends to divide
people = int(input("How many people to split the bill?\n"))

#Calculating the amount per person with tip
bill_splited = (bill * tip) / people

#Showing the result to user
print(f"Each person should pay: ${bill_splited:.2f}")
