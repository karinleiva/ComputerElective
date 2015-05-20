name = raw_input("What is your name?")
age = input("How old are you?")

namebf = raw_input("What is your best friend's name?")
agebf = input("How old is your best friend?")

if age == agebf:
    print name, "and" , namebf , "are both" , age , "years old"
elif age > agebf:
        print name, "is older than" , namebf 
        print name, "is" , age, "and" , namebf , "is" , agebf
elif age < agebf:
    print name, "is younger than" , namebf 
    print name, "is" , age, "and" , namebf , "is" , agebf
