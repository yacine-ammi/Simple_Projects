# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:25:44 2020

@author: Yacino
"""


                      # Checking the validity of a cridit card
#try these numbers :
# 3, 7, 1, 4, 4, 9, 6, 3, 5, 3, 9, 8, 4, 3, 1
# 79927398713

                         #Luhn's Algorithm

# Demanding the number of the credit card and adding evry num to a list called mlist
number = input("Enter number ==>  ")
mlist = []
if number.isdigit():
    
    
    for char in number :
        number1 = int(char)
        mlist.append(number1)
    print(mlist)


    i = -2
    slist = []
    for num in range(int(len(mlist)/2)):
        slist.append(mlist[i]*2)
        i=i-2
    print(slist)
    
    
    glist = []
    card = 0
    for num in range(len(slist)):
        if slist[num]>9:
            card = card + ((slist[num]-10)+1)
        else:
            card = card + slist[num]
            
            
    j = -1
    for num in range((len(mlist)//2)+(len(mlist)%2)):
        card = card + mlist[j]
        j=j-2
    
    
    if (card % 10)==0:
        print(f"The card number you've entered is VALID")
    else:
        print(f"The card number you've entered is INVALID")
else:
    print(number, "Must contain only DIGIT numbers")
#_____________________________________________________________________________________