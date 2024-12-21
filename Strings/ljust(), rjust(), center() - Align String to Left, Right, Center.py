### ljust, rjust, center - Align string to left, right, center ###


## ljust - aligns string to left
str = "Awesome"
# ljust (width, fillchar)
str.ljust(12, "#")
print (str.ljust(12, "#"))
# Output: Awesome#####


## rjust - aligns string to right
str2 = "Awesome"
# rjust (width, fillchar)
str2.rjust(22," ")
print(str2.rjust(22, " "))
# Output:        Awesome        


## center - aligns string in center
str3 = "Python"
# center (width, fillchar)
str3.center(15, "-")
print(str3.center(15, "-"))
# Output: -----Python----
