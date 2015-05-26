#Use Conditionals and Operators learned last class
#Write a program that allows the user to input their subjects
#Then ask for their grade in each subject
#Calculate the GPA based on these values (You may to research how GPA is calculated)

subj1=raw_input("Enter your subject")
subj2=raw_input("Enter your subject?")
subj3=raw_input("Enter your subject?")
subj4=raw_input("Enter your subject?")

math = raw_input("What is your grade in math?")
english= raw_input("What is your grade in english?")
physics=raw_input("What is your grade in physics?")
computer=raw_input("What is your grade in computer?")


if math =='A':
    math=4.00
elif math =='A':
    math=4.00
elif math=='B':
    math=3.00
elif math=='A':
    math=4.00

if english =='A':
    english=4.00
elif english =='A':
    english=4.00
elif english=='B':
    english=3.00
elif english=='A':
    english=4.00
    
if physics =='A':
    physics=4.00
elif physics =='A':
    physics=4.00
elif physics=='B':
    physics=3.00
elif physics=='A':
    physics=4.00

if computer =='A':
    computer=4.00
elif computer =='A':
    computer=4.00
elif computer=='B':
    computer=3.00
elif computer=='A':
    computer=4.00

print math
print english
print physics
print computer 
    
GPA=raw_input("What is your GPA?")
#4.0+4.0+3.0+4.0/4
