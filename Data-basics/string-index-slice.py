my_sentence = "The world is round"

#1st index
print(my_sentence[0])

print("----------------")

#last index
print(my_sentence[-1])

print("----------------")

#Slice - Grabbing a subsection
#Syntax: [start:stop:step]
#step decides how many jumps to make

print(my_sentence[4:9])

print("----------------")

print(len(my_sentence))

print("----------------")

print(my_sentence[::]) #Console entire sentence from start to end

print("----------------")

print(my_sentence[::2]) #Console from start to end but in jumps of 2 step sizes

my_alphabet = "abcdeffghijklmnopqrstuvwxyz"

print("----------------")

print(my_alphabet[::2])

print("----------------")

print(my_alphabet[::3])

print("----------------")

print(my_alphabet[1:10:3])

print("----------------")

print(my_alphabet[::-1]) #Easy way to reverse a string

print("----------------")

print(my_sentence[::-1])