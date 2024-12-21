### Index() - Find First Occurrence of Character in String ###
# This includes the black spaces in the string

str = "Hello to the world"

str.index("the")

print (str.index("the"))
# Output: 9

print (str.index("to"))
# Output: 6

print (str.index("world"))
# Output: 1


# Element not present in string - error
print (str.index("as"))
# Output: ValueError: substring not found
