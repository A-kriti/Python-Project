# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:01:19 2020

@author: akrit
"""

import random
print("Hello friend ,nice to see you here!")
print("So are you ready to play this mind reading game with me? ","\n","Press 'y'or 'Y' if you are interested otherwise if you say 'no' you lost a great chance!")

Yes_No=input()
if Yes_No=='Y' or Yes_No=='y' :
    print("Let's start the game! ")
    print("type 'Y' for yes")
    c1=input()
    if c1!='Y'and c1!='y':
        print("You left the game :( Have nice day dear! ")
    else: 
        print("Step 1___________________________________________________________")
        print("\n")
        print("Take any number between 1 to 1000 in your mind")
        print("If u had done this then press 'Y' or 'y'")
        c2=input()
        if c2!='Y' and c2!='y':
            print("You left the game :( Have nice day dear!")
        else:
            print("Step 2___________________________________________________________")
            print("\n")
            print("I know that you are very good in Calculations , so let's check it")
            print("\n")
            
            print("All the following calculations you had to do in your mind")
            print("\n")
            #Alexa is my best and and she'll yours also
            print("Step 3___________________________________________________________")
            print("\n")
            print("Assume 'Alita' is your friend")
            print("Now take the same number you assumed intially from 'Alita' and sum up all the values you have")
            print("\n")
            
            print("If u had done this then press 'Y' or 'y'")
            
            c3=input()
            
            if c3!='Y'and c3!='y':
                print("You left the game :( Have nice day dear! ")
            else:
                print("Step 4___________________________________________________________")
                print("\n")
                My_value=int(random.randint(1,1000))
                print("\n")
                print("Take '{0}' by my side".format(My_value))
                print("\n")
                print("If u had done this then press 'Y' or 'y'")
            
                c4=input()
            
                if c4!='Y'and c4!='y':
                    print("You left the game :( Have nice day dear! ")
                else:
                    print("Step 5___________________________________________________________")
                    print("\n")
                    print("Add all the values you have")
                    print("\n")
                    print("If u had done this then press 'Y' or 'y'")
            
                    c5=input()
            
                    if c5!='Y'and c5!='y':
                        print("You left the game :( Have nice day dear! ")
                    else:
                        print("Step 6___________________________________________________________")
                        print("\n")
                        print("Divide the total sum by '2'")
                        print("\n")
                        print("If u had done this then press 'Y' or 'y'")
            
                        c6=input()
            
                        if c6!='Y'and c6!='y':
                            print("You left the game :( Have nice day dear! ")
                        else:
                            print("Step 7___________________________________________________________")
                            print("\n")
                            c6=input()
            
                            if c6!='Y'and c6!='y':
                                print("You left the game :( Have nice day dear! ")
                            else:
                                print("Return back same number that you had taken from 'Alexa' to her" )
                                print("\n")
                                print("FINAL ANSWER__________________________________________________________")
                                print("\n")
                                print("I am not a magician but i now that how much money you have right now!")
                                print("\n")
                                print("Do you want to know the ans??","/n","Say 'yes' or 'no'")
                                print("\n")
                                Yes_No1=input()
                                if Yes_No1=='Y' or Yes_No=='y' :
                                    print("Now you are left with this number: ",My_value/2)
                                    print("\n")
                                    print("Well played!")
                                else:
                                    print("Thanks for playing!")
else:
    print("Have a Nice Day")
print("Thanks for playing!")