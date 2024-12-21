### Check if String is a Palindrome or Not ###


def palindrome():
    f = str[: :-1]
    if f==str:
        print ("It is a palindrome")
    else:
        print ("It is not a palindrome")

str = input ("Enter a string: ")
palindrome()
