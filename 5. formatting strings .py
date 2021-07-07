# Assigning two variables to strings
person="Iron Man"
day="day!!!"
# Using 'Format'(f) to say "Iron Man saved the day!!!" by calling variables inside the string
print(f"{person} saved the {day}")
# Using 'format'(.format()) to say "Iron Man saved the day!!!" by calling variables from the list made by .format() inside the string
print("{0} saved the {1}".format(person,day))

