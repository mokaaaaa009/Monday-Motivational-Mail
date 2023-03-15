#---------Exercise1---------------
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades={}
# for key in student_scores:
#   if student_scores[key]>90:
#     student_grades[key]="Outstanding"
#   elif student_scores[key]>=81 and student_scores[key]<=90:
#     student_grades[key]="Exceeds Expectations"
#   elif student_scores[key]>=71 and student_scores[key]<=80:
#     student_grades[key]="Acceptable"
#   else :
#     student_grades[key]="Fail"    

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# # 🚨 Don't change the code below 👇
# print(student_grades)
#------------Exercise 2 ------------------------
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(countr,visits,cities):
#     newInfo={"country":countr,"visits":visits,"cities":cities}
#     travel_log.append(newInfo)
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# for key in order:
#   for index in order[key]:
#      print(index)
# print(order["main"][2])


#HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program")
exit=1
biders={}
while(exit):
  
  name=input("What's your name?: ")
  bid =input("What's your bid?:$ ")
  biders[name]=bid
  print("Are there any other biders ? Type yes or no")
  exit=input()
  if exit == "no":
    exit=0
    max="0"
    name=""
  
for biderr in biders:
  if biders[biderr]>max:
    max = biders[biderr]
    name = biderr
print("The Winner is "+name+" with a bid of "+max)  
