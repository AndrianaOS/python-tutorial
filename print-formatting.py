# .format() method
# string.format()
print("This is string {}".format("formatting"))

#Use indexing to place strings in specific positions
print("The {2} {1} {0}".format("fox", "brown", "quick"))


#Using keys to place strings in specific positions
print("The {c} {g} {d}".format(d="dog", c="cute", g="golden"))


#To create a precision width use {value:width.precisionf}
#Precision refers to the amount of decimal places you want
result = 100/777

print("The result is {r:1.3f}".format(r=result))

#f-string method
name = "Jennie"
age  = "25"
print(f"Hello, her name is {name.upper()}")
print(f"Hello, her name is {name} and she is {age} years old")