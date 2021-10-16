# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:19:58 2020

@author: Yacine
"""
import matplotlib.pyplot as plt

text = input("""write your text 
here ==> """)
count_letter = {}
for letter in text:
    if letter.isalpha():
        count_letter[letter.lower()] = count_letter.get(letter, 0)+1
        
print(count_letter)

x,y = zip(*count_letter.items())
print(x, end=" ")
print(y, end=" ")
plt.bar(x,y)
plt.show()
 
