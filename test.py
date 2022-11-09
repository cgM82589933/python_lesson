# get user name and print out `Hello, {name}!`

name_input = input("What is your name? ")
name_input_ver = input("Verify name... ")


#statement_1 = "Hello, " + name_input + "!"
#statement_2 = f"Hello, {name_input}!"

#print(statement_1)
#print(statement_2)
#print(statement_1 == statement_2)

def case_1_function(name):
   print(f"You are you successfully logged in, {name}")

def case_2_function():
   print("Failed to login")

# compare two name and the verification
# if they match, run case_1_function
# if they don't, run case_2_function
if name_input == name_input_ver:
   case_1_function(name_input)

else:
   case_2_function()

