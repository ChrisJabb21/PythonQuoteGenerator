'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Created on Sat Oct 20 16:00:16 2018
# @author: Chris Jabbour 

#This program is a random quote generator of select quotes from 
the Famous Lebanese-American writer poet Kahlil Gibran using 
the random python library and list structures.
'''
import random

#declaration of author and list items or quotes
Author = "Kahlil Gibran"
Quote1 = "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars."
Quote2 = "Work is love made visible."
Quote3 = "Beauty is not in the face; beauty is a light in the heart."
Quote4 = "Trust in dreams, for in them is hidden the gate to eternity."
    
#initialization and assignment of elements in Quotelist
QuoteList = [Quote1, Quote2, Quote3, Quote4]
    
def main():
    
    #print program name and description
    print ("\n #----Kahlil Gibran Random Quote Generator----#")
           
    print("\n This program is a random quote generator for the Famous Lebanese-American writer and poet Kahlil Gibran.")
    
    userchoice()

#fcn to ask if user wants to see another quote.
def userreply():
    
    user_input = input(f"Would you like to see another quote? y/n \n >> ")
    
    if user_input in ["y", "Y", "yes", "Yes"]:
        
        print("\n Quote:" ,random.choice(QuoteList))
        
        userreply()
        
    elif user_input in ["n", "N", "no", "No"]:
        
        print("\n Understood, have a nice day! \n")
    
    else:
        print("\n That is invalid input, please enter one of the following choices. \n")
        
        userchoice()
        
#fcn for user decision
def userchoice():
    #ask user for input
    user_input = input(f"Would you like to see a quote by {Author}? y/n \n >> ")

    #conditional statements to check for user inputs using list notation
    if user_input in ["y", "Y", "yes", "Yes"]:
        
        print("\n Quote:" ,random.choice(QuoteList))
        
        #function recall to ask if your wants to  
        userreply()

    elif user_input in ["n", "N", "no", "No"]:
        
        print("\n Understood, have a nice day! \n")
    
    else:
        print("\n That is invalid input, please enter one of the following choices. \n")
        
        userchoice()