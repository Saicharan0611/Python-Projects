# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)
random_choice = random.randint(0, num_items-1)
person_choosed = names[random_choice]
print(person_choosed + " is going to pay the meal today!")