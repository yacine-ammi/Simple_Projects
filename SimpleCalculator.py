# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 01:58:02 2019

@author: Yacine Ammi
"""
operations = ["+", "-", "*", "/"]
while True:
    print("User Manuel : ")
    print("Enter '+' to add two numbers")
    print("Enter '-' to substract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter any other character to end the program")
    if True:
        break
while True:
    uinput=input("Which operation do you want prcess Sir/Miss : ")
    if uinput not in operations :
        break

    
    elif uinput == "+":
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = num1 + num2
        print("The answer is " + str(result) )
    
    elif uinput == "-":
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = num1 - num2
        print("The answer is " + str(result) )
    
    elif uinput == "*":
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = num1 * num2
        print("The answer is " + str(result) )
    
    elif uinput == "/":
        try:
            num1 = float(input("Enter a number : "))
            num2 = float(input("Enter another number : "))
            result = num1 / num2
            print("The answer is " + str(result) )
        except ZeroDivisionError :
            print(" Error : You cant divide by zero \n please do it again ")
            continue
    
    else :
        print("\n Error : This option doesn't exist \n")
        print("Please read carefully the User Manuel \n")
        
        
    
        
    
    
