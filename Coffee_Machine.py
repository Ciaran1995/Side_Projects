#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:49:59 2021

@author: ciaranmcdonnell
"""

import numpy as np

class Coffee_Machine:
    """ Coffee machine class with pre-determined drinks and prices.
    """
    
    resources = {'Water': 300, 'Milk': 200, 'Coffee': 100}
    drinks = {'Espresso': 1.50, 'Latte': 2.0, 'Cappuccino': 2.50}
    recipes = {'Espresso': np.array([20,0,10]), 'Latte': np.array([20,30,5]), 'Cappuccino':np.array([20,30,10])}
    
   # def __init__(self):
        
        
    def print_resources(self):
        print('Water: '  + str(self.resources['Water']) + 'ml')
        print('Milk: '  + str(self.resources['Milk']) + 'ml')
        print('Coffee: '  + str(self.resources['Coffee']) + 'g')
            
    def print_drinks(self):
        for j in self.drinks:
            print(j + ': £' + str(self.drinks[j]))    
            
    def sell_drink(self):
        drink_choice = False
        while drink_choice == False: # Loop until drink choice is made.
            drink = input('What would you like? \nEspresso  \nLatte  \nCappuccino\n')
            if (self.resources['Water']-self.recipes[drink][0])>=0 and (self.resources['Milk']-self.recipes[drink][1])>=0 and (self.resources['Coffee']-self.recipes[drink][2])>=0:
                print("Nice choice!")
                drink_choice = True
            else:
                print("Cannot make your " + drink)
                if (self.resources['Water']-self.recipes[drink][0])<0:
                    print("Not enough water.")
                if (self.resources['Milk']-self.recipes[drink][1])<0:
                    print("Not enough milk.")
                if (self.resources['Coffee']-self.recipes[drink][2])<0:
                    print("Not enough coffee.")
            
                another = input("Would you like to choose another drink? y/n\n").lower()
                if another == 'n':
                    return
                
        
        sale = False
        while sale == False:
            print('Your ' + drink + ' costs: £' + str(self.drinks[drink]))
            quarters = input("Number of quarters you have: ")
            if 0.25*int(quarters)>= self.drinks[drink]:
                change = 0.25*int(quarters) - self.drinks[drink]
                print("Thank you for your purchase. Your change is £" + str(round(change,2)) + ". Enjoy!")
                self.resources['Water'] = self.resources['Water']-self.recipes[drink][0]
                self.resources['Milk'] = self.resources['Milk']-self.recipes[drink][1]
                self.resources['Coffee'] = self.resources['Coffee']-self.recipes[drink][2]
                
                sale = True
            else:
                dimes = input("Number of dimes you have: ")
                if 0.25*int(quarters) + 0.1*int(dimes) >= self.drinks[drink]:
                    change = 0.25*int(quarters) + 0.1*int(dimes) - self.drinks[drink]
                    print("Thank you for your purchase. Your change is £" + str(round(change,2)) + ". Enjoy!")
                    self.resources['Water'] = self.resources['Water']-self.recipes[drink][0]
                    self.resources['Milk'] = self.resources['Milk']-self.recipes[drink][1]
                    self.resources['Coffee'] = self.resources['Coffee']-self.recipes[drink][2]
                    
                    sale = True
                else:
                    nickels = input("Number of nickels you have: ")
                    if 0.25*int(quarters) + 0.1*int(dimes) + 0.05*int(nickels) >= self.drinks[drink]:
                        change = 0.25*int(quarters) + 0.1*int(dimes) + 0.05*int(nickels) - self.drinks[drink]
                        print("Thank you for your purchase. Your change is £" + str(round(change,2)) + ". Enjoy!")
                        self.resources['Water'] = self.resources['Water']-self.recipes[drink][0]
                        self.resources['Milk'] = self.resources['Milk']-self.recipes[drink][1]
                        self.resources['Coffee'] = self.resources['Coffee']-self.recipes[drink][2]
                    
                        sale = True 
                    else:
                        pennies = input("Number of pennies you have: ")
                        if 0.25*int(quarters) + 0.1*int(dimes) + 0.05*int(nickels) + 0.01*int(pennies) >= self.drinks[drink]:
                            change = 0.25*int(quarters) + 0.1*int(dimes) + 0.05*int(nickels) + 0.01*int(pennies) - self.drinks[drink]
                            print("Thank you for your purchase. Your change is £" + str(round(change,2)) + ". Enjoy!")
                            self.resources['Water'] = self.resources['Water']-self.recipes[drink][0]
                            self.resources['Milk'] = self.resources['Milk']-self.recipes[drink][1]
                            self.resources['Coffee'] = self.resources['Coffee']-self.recipes[drink][2]
                    
                            sale = True 
                        else:
                            print("Sorry that's not enough change! Please collect your money and start again.")
                            return
                    
        
        