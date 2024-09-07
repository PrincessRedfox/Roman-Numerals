# program: ROMAN NUMERALS.py
# author: Sarina Saiyed
# email: 2338323@students.carmel.ac.uk
# student number: 2338323
#
# A manufacturing company wishes to make a new calculator that allows
# the user to input two numbers in Arabic decimal form (each input
# number must not exceed 2499) and displays the numbers in Roman numeral
# form.  The calculator then allows a user to add or subtract the two
# numbers, displaying the result in both Arabic decimal and Roman
# numeral form.

 
########################################################################
# Design

# Assign a variable for one of the input Arabic decimal number from the user
# Assign another variable for the other  Arabic decimal number from the user
# Set a stored variable of both the roman numeral values (M, D, C, L, X, V, I)
#   and the Arabic decimal values (1000, 500, 100, 50, 10, 5, 1)
# Take the first assigned variable and go down the index of the stored
#   variable of the Arabic decimal values and divide each value until the
#   results are more than zero
# When the result is more than zero, it will show how many of that roman
#   value will be needed
#       e.g … 49 // 50 => 0, 49 // 10 => 4 
# Therefore, will need to represent 10 + 10 + 10 + 10 => XXXX 
# To check if there are more character that need to be converted, take
#   the first assigned variable and take the modulus operation of it
#   with the index of the stored variable of the Arabic decimal values
#       e.g 49 % 10 => 9
# If the given number is not in the the stored variable of the roman
#   numeral values, repeat the process of splitting the unit values
#   of the modulus results
#       … 9 // 10 => 0, 9 // 5 => 1
# Roman value: XXXXV
# 9 % 1 => 1
# Roman value: XXXXVI
# After repeating until the entire value is converted to additive roman
#   numeral, repeat the steps again for the second input value
# Output the converted input values for the user
# Give the user the option to add or subtract the two numbers
# If the user chooses to add both numbers,
# Add the Arabic decimal form of there two input numbers and than convert
#   to roman numeral 
# If the user chooses to subtract from the two numbers, 
# Subtract the Arabic decimal form of the two input numbers
# If the result if less than or equal to zero
# Tell the user this is result is not possible 
# Set the user back to where they can choose to either add or subtract
#   their two numbers
# If the result is more than zero, covert the result into roman numerals
# Finally, display to the user the result in both Arabic decimal and
#   Roman numeral form.


########################################################################
# Pseudocode

# DEF RomanConverter1(DecimalInt1, ArabicDecimal, RomanNumerals)
#       IF DecimalInt1 > 2499:
#               PRINT("Your input numbers are too big")
#               RETURN
#
#       Roman1 = ""
#       i = 0
#       WHILE DecimalInt1  > 0:
#               Divide1 = DecimalInt1 // ArabicDecimal[i]
#               DecimalInt1 = DecimalInt1 % ArabicDecimal[i]
#               WHILE Divide1:
#                       Roman1 = Roman1 + RomanNumerals[i]
#                       Divide1 -=1
#               END WHILE
#               i +=1
#       END WHILE
#       RETURN Roman1
#       END IF

#
# DEF RomanConverter2(DecimalInt2,ArabicDecimal, RomanNumerals)
#       IF DecimalInt2 > 2499:
#               PRINT("Your second input numbers are too big")
#               RETURN]

#       Roman2 = ""
#       i = 0
#       WHILE DecimalInt2  > 0:
#               Divide2 = DecimalInt2 // ArabicDecimal[i]
#               DecimalInt2 = DecimalInt2 % ArabicDecimal[i]
#               WHILE Divide2:
#                       Roman2 = Roman2 + RomanNumerals[i]
#                       Divide2 -=1
#               END WHILE
#               i +=1
#       END WHILE
#       RETURN Roman2
#       END IF
#
# DEF calculator(DecimalInt1,DecimalInt2,ArabicDecimal,RomanNumerals):
#       option = INPUT("Would you like to Add or Subtract your numbers? \n")
#       IF option == "Add":
#               RomanResultA = ""
#               i = 0
#               resultA = DecimalInt1 + DecimalInt2
#               divideA = resultA // ArabicDecimal[i]
#               resultA = resultA % ArabicDecimal[i]
#               WHILE divideA:
#                       RomanResultA = RomanResultA + RomanNumerals[i]
#                       divideA -=1
#               END WHILE
#               i += 1
#               PRINT(resultA, RomanResultA)
#       ELIF option == "Subtract":
#               RomanResultS = ""
#               i = 0
#               resultS = DecimalInt1 + DecimalInt2
#               IF results <= 0:
#                       PRINT("Answer cannot be less than or equal to zero, choose addtion")
#                       RETURN
#               divideS = resultS // ArabicDecimal[i]
#               resultS = resultS % ArabicDecimal[i]
#               WHILE divideS:
#                       RomanResultS = RomanResultS + RomanNumerals[i]
#                       divideS -=1
#               END WHILE
#               i += 1
#       PRINT(resultS, RomanResultS)
#       END IF
#
#
# ArabicDecimal = [1000, 500, 100, 50, 10, 5, 1]
# RomanNumerals = ["M", "D", "C", "L", "X", "V", "I"]
# 
# PRINT("The numbers you are about to enter cannot exceed 2499.")
# DecimalInt1 = INT(INPUT("Enter your first number: "))
# DecimalInt2 = INT(INPUT("Enter your second number: "))
#


########################################################################
# Variables

# INT DecimalInt1
# INT DecimalInt2
# INT ArabicDecimal
# STR RomanNumerals
# STR Roman1
# STR Roman2
# INT Divide1
# INT Divide2
# STR option
# STR RomanResultA
# STR RomanResultS
# INT resultA
# INT resultS
# INT divideA
# INT divideS


########################################################################
# Functions

# RomanConverter1
# RomanConverter2
# addcalculator
# subcalculator

########################################################################
# Main


def RomanConverter1(DecimalInt1):
    if DecimalInt1 > 2499: # if statement that ends the funtion 
        print("Your first input number is too big:")# if the first value is greater than 2499
        return
    Roman1 = "" #empty string variable, store final result
    i = 0 # index is set to zero
    while DecimalInt1 > 0: #while loop that continues when the variable 'Decimal1' is more than 0
        Divide1 = DecimalInt1 // ArabicDecimal[i] # the variable is divided with the value of each index in the stored variable
        DecimalInt1 = DecimalInt1 % ArabicDecimal[i]# the answer from before is used to find the modulus using the same stored variable
                                                    # This will continue untill the variable is 0
        while Divide1: # while the variable is not zero, will execute body untill Divide1 = 0
            Roman1 = Roman1 + RomanNumerals[i] # the empty string is added onto using the index of the roman stored variable 
            Divide1 -= 1 # takes the value away from 1; so when variable = 0 the body will end
        i += 1 # increments the index of the stored variables to indicate that the largest value as been checked and will be going to the next largest value untill the end
    return Roman1 # ends the program and allows to return the final converted input

def RomanConverter2(DecimalInt2): # same code as the first function
    if DecimalInt2 > 2499:
        print("Your second input number is too big: ")
        return
    Roman2 = ""
    i = 0
    while DecimalInt2 > 0:
        Divide2 = DecimalInt2 // ArabicDecimal[i]
        DecimalInt2 = DecimalInt2 % ArabicDecimal[i]
        while Divide2:
            Roman2 = Roman2 + RomanNumerals[i]
            Divide2 -= 1
        i += 1
    return Roman2


def addcalculator(DecimalInt1,DecimalInt2):
    RomanResultA = ""
    i = 0
    resultA = DecimalInt1 + DecimalInt2 # gives the Arabic decimal addtion value
    while resultA > 0: # converts the results into roman numerals like in the convertion functions
        divideA = resultA // ArabicDecimal[i]
        resultA = resultA % ArabicDecimal[i]
        while divideA:
            RomanResultA = RomanResultA + RomanNumerals[i]
            divideA -=1
        i += 1
    resultA = DecimalInt1 + DecimalInt2 #repeating this line of code to be able to output both values
    return RomanResultA, resultA # returns both the arabic decimal and roman numeral form
        
        
def subcalculator(DecimalInt1,DecimalInt2):
    RomanResult = ""
    i = 0
    resultS = DecimalInt1 - DecimalInt2 # gives the subtraction
    if resultS <= 0: # ends the function if the result is zero or negative
        print("Answer cannot be less than or equal to zero")
    return
    while resultS > 0: # converts answer to roman numeral
        divideS = resultS // ArabicDecimal[i]
        resultS = resultS % ArabicDecimal[i]
        while divideS:
            RomanResult = RomanResult + RomanNumerals[i]
            divideS -=1
        i += 1
    resultS = DecimalInt1 - DecimalInt2
    return RomanResult, resultS
        
        
        
#Varibles are below the functions so that they are able to be passed through the parameters or used as arguments

ArabicDecimal = [1000, 500, 100, 50, 10, 5, 1] #stored Arabic decimal variable
RomanNumerals = ["M", "D", "C", "L", "X", "V", "I"] #stored Roman numeral variable


print("The numbers you are about to enter cannot exceed 2499.") # tells user the input limit

DecimalInt1 = int(input("Enter your first number: ")) #input variable
DecimalInt2 = int(input("Enter your second number: ")) #input variable

print("Input one:",RomanConverter1(DecimalInt1)) # prints out the roman convertion of first input
print("Input two:",RomanConverter2(DecimalInt2)) # prints out the roman convertion of second input



if DecimalInt1 <= 2499 and DecimalInt2 <= 2499: # if statement to allow user access to addtion and subtraction if both inputs are less than 2499
    option = input("Would you like to add or subtract? \n")
    if option == "add":
        addcalculator(DecimalInt1 ,DecimalInt2) #send the user to the addcalculator funtion
        print(addcalculator(DecimalInt1 ,DecimalInt2)) # prints out the return values after the variables have fully passed the function
    elif option == "subtract":
        subcalculator(DecimalInt1,DecimalInt2)
        print(subcalculator(DecimalInt1,DecimalInt2))
    else:
        print("Please enter either 'add' or 'subtract'")
        quit #end the program


    

