# 1- write a program which takes 2 inputs from the user : weight(kg)
# and height(meter) and prints the BMI in the output.
weight = int(input("Enter your weight(kg) : "))
height = float(input("Enter your height(meter): "))
BMI = weight / (height*2)
print(f"BMI is : {round(BMI, 2)}")

# 2- write a program which takes the name of the user as input and replace all the occurence of character
# 'a' in the name to 'b' and print it.
user_name = input("Enter your name : ")
print(f"After replacing a with b: " + user_name.replace("a", "b"))

# 3- write a program which takes 2 inputs from user as principle amount (int) and
# rate of annual interest (float) and print the expected total amount  after  2 years.
princ_amt = int(input("Enter Principal amount : "))
rate_of_interest = float(input("Enter rate of interest : "))
print(f"Expected amount after 2 years : {round(princ_amt*rate_of_interest*1.1,2)}")

# 4- write a program which takes city name from user input. irrespective of in
# which case user enters the city name, print the city name in camel case meaning first letter should be capital
# and rest in small.
city_name = input("Enter city name: ")
print(city_name.title())

# 5- write a program which takes the name of the user as input and print the index of character 'a' in the string.
# if 'a' is not there then return -1.
user_name = input("Enter your name: ")
if 'a' in user_name:
    print(user_name.index('a'))
else:
    print("-1")

# 6-  Display the number of letters in the below string
my_word = "antidisestablishmentarianism"
print(len(my_word))

# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# Display : my name is Mohit Sharma and I am 32 years old.
# note that first letter of first name and last name both should be in capital letters and rest in small.
f_name = input("Enter first name : ")
l_name = input("Enter last name : ")
age = int(input("Enter age : "))
print(f"My name is {f_name.title()} {l_name.title()} and I am {age} years old.")


# 8-take 3 inputs from user : first name , last name and company name. create the email alias for
# the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# Display : morma@infosys.com
f_name = input("Enter first name : ")
l_name = input("Enter last name : ")
company_name = input("Enter company name : ")
email_add = f_name[0:2].lower() + l_name[-3:].lower() + "@" + company_name.lower() + ".com"
print(email_add)




