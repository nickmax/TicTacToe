#!/usr/bin/python3

import os
import colored
import termcolor
from os import *
from termcolor import *
from colored import bg,fg,attr

#Colours
#2
red = fg("red")
green = fg("green")
blue = fg("blue")
reset = attr("reset")
yellow = fg("yellow")
link = "https://github.com/nickmax/TicTacToe.git"
def Licenses():
    print("Copyright 2020 N.MATHENGE "+ red+"https://www.instagram.com/_math.enge_/ "+ reset +yellow +">> INSTAGRAM"+reset )

    print("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:")

    print("The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.")

    print("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")



cells = []
movelist = ["A","B","C","D","E","F","G","H","I","a","b","c","d","e","f","g","h","i"]
movelistsmall = ["a","b","c","d","e","f","g","h","i"]



x_moved = []
o_moved = []
cells2 = list("_________")

cells = []
movedlist = []

count_x = 0
count_o = 0
x_wins = False
o_wins = False


fail = "Please try again!"
fail1 = "Already Occupied by 'X'"
fail2 = "Already Occupied by 'O'"
fail3 = "No such location!"
header = "TICTACTOE"
rules = "Input 3 in a row or a column and if they match.You win "
rules2 = "HAVE FUN!"
xmovesent = "Its 'X' turn! \nPlease input the location!"
omovesent = "Its 'O' turn! \nPlease input the location!"
startgamestr = "To play press Enter \nTo read the rules enter -R"



def xmove():
    #Xmove
    print(xmovesent)
    while True:
        xmove = input()
        if xmove not in movelist:
            print(fail3)
        elif xmove in x_moved:
            print(fail1)
        elif xmove in o_moved:
            print(fail2)
        else:
            cells.append("X")
            x_moved.append(xmove)
            try:
                v = movelist.index(xmove)
                cells2[v]=("X")
            except:
                y = movelistsmall.index(xmove)
                cells2[y] = ("X")
            break
        
        
def omove():
    #Omove
    print(omovesent)
    while True:
        omove = input()
        if omove not in movelist:
            print(fail3)
            print(fail)
        elif omove in x_moved:
            print(fail1)
        elif omove in o_moved:
            print(fail2)
        else:
            cells.append("O")
            o_moved.append(omove)
            try:
                v = movelist.index(omove)
                cells2[v]=("O")
            except:
                y = movelistsmall.index(omove)
                cells2[y] = ("O")
            break
                
        
        
def xmove2():
    print(xmovesent)
    while True:
        xmove2 = input()
        if xmove2 not in movelist:
            print(fail3)
        elif xmove2 in x_moved:
            print(fail1)
        elif xmove2 in o_moved:
            print(fail2)
        else:
            cells.append("X")
            x_moved.append(xmove2)
            try:
                v = movelist.index(xmove2)
                cells2[v]=("X")
            except:
                y = movelistsmall.index(xmove2)
                cells2[y] = ("X")
            break
           
        
def omove2():
    print(omovesent)
    while True:
        omove2 = input()
        if omove2 not in movelist:
            print(fail3)
        elif omove2 in x_moved:
            print(fail1)
        elif omove2 in o_moved:
            print(fail2)
        else:
            cells.append("O")
            o_moved.append(omove2)
            try:
                v = movelist.index(omove2)
                cells2[v]=("O")
            except:
                y = movelistsmall.index(omove2)
                cells2[y] = ("O")
            break
       
def xmove3():
    print(xmovesent)
    while True:
        xmove3 = input()
        if xmove3 not in movelist:
            print(fail3)
        elif xmove3 in x_moved:
            print(fail1)
        elif xmove3 in o_moved:
            print(fail2)
        else:
            cells.append("X")
            x_moved.append(xmove3)
            try:
                v = movelist.index(xmove3)
                cells2[v]=("X")
            except:
                y = movelistsmall.index(xmove3)
                cells2[y] = ("X")
            break
        

def omove3():
    print(omovesent)
    while True:
        omove3 = input()
        if omove3 not in movelist:
            print(fail3)
        elif omove3 in x_moved:
            print(fail1)
        elif omove3 in o_moved:
            print(fail2)
        else:
            cells.append("O")
            o_moved.append(omove3)
            try:
                v = movelist.index(omove3)
                cells2[v]=("O")
            except:
                y = movelistsmall.index(omove3)
                cells2[y] = ("O")
            break

def xmove4():
    print(xmovesent)
    while True:
        xmove4 = input()
        if xmove4 not in movelist:
            print(fail3)
        elif xmove4 in x_moved:
            print(fail1)
        elif xmove4 in o_moved:
            print(fail2)
        else:
            cells.append("X")
            x_moved.append(xmove4)
            try:
                v = movelist.index(xmove4)
                cells2[v]=("X")
            except:
                y = movelistsmall.index(xmove4)
                cells2[y] = ("X")
            break

def omove4():
    print(omovesent)
    while True:
        omove4 = input()
        if omove4 not in movelist:
            print(fail3)
        elif omove4 in x_moved:
            print(fail1)
        elif omove4 in o_moved:
            print(fail2)
        else:
            cells.append("O")
            o_moved.append(omove4)
            try:
                v = movelist.index(omove4)
                cells2[v]=("O")
            except:
                y = movelistsmall.index(omove4)
                cells2[y] = ("O")
            break
            
def xmove5():
    print(xmovesent)
    while True:
        xmove5 = input()
        if xmove5 not in movelist:
            print(fail3)
        elif xmove5 in x_moved:
            print(fail1)
        elif xmove5 in o_moved:
            print(fail2)
        else:
            cells.append("X")
            x_moved.append(xmove5)
            try:
                v = movelist.index(xmove5)
                cells2[v]=("X")
            except:
                y = movelistsmall.index(xmove5)
                cells2[y] = ("X")
            break

    
def boardstate():
    try:
        print(red +"---------" + ((" ")*15)+"---------"+reset)
        print(green +"| " + cells2[0] + " " + cells2[1] + " " + cells2[2] + " |" + ((" ")*15) +"| " + movelist[0] + " " + movelist[1] + " " + movelist[2] + " |"+reset)
        print(blue +"| " + cells2[3] + " " + cells2[4] + " " + cells2[5] + " |" + ((" ")*15) +"| " + movelist[3] + " " + movelist[4] + " " + movelist[5] + " |"+reset)
        print(green +"| " + cells2[6] + " " + cells2[7] + " " + cells2[8] + " |" + ((" ")*15) +"| " + movelist[6] + " " + movelist[7] + " " + movelist[8] + " |"+reset)
        print(red +"---------" + ((" ")*15)+"---------"+reset)
    except:
        missing = 9 - len(cells)
        for x in range(missing):
            cells2.append("_")
            print(missing)
            print("---------")
            print("| " + cells2[0] + " " + cells2[1] + " " + cells2[2] + " |")
            print("| " + cells2[3] + " " + cells2[4] + " " + cells2[5] + " |")
            print("| " + cells2[6] + " " + cells2[7] + " " + cells2[8] + " |")
            print("---------")
def checkresult():
    zerox = 0
    zeroy = 0
    if (cells2[0] == cells2[1] == cells2[2] == 'X' or
    cells2[3] == cells2[4] == cells2[5] == 'X' or
    cells2[6] == cells2[7] == cells2[8] == 'X' or
    cells2[0] == cells2[3] == cells2[6] == 'X' or
    cells2[1] == cells2[4] == cells2[7] == 'X' or
    cells2[2] == cells2[5] == cells2[8] == 'X' or
    cells2[0] == cells2[4] == cells2[8] == 'X' or
    cells2[2] == cells2[4] == cells2[6] == 'X'):
        zerox = 1

    if (cells2[0] == cells2[1] == cells2[2] == 'O' or
    cells2[3] == cells2[4] == cells2[5] == 'O' or
    cells2[6] == cells2[7] == cells2[8] == 'O' or
    cells2[0] == cells2[3] == cells2[6] == 'O' or
    cells2[1] == cells2[4] == cells2[7] == 'O' or
    cells2[2] == cells2[5] == cells2[8] == 'O' or
    cells2[0] == cells2[4] == cells2[8] == 'O' or
    cells2[2] == cells2[4] == cells2[6] == 'O'):
        zeroy = 2
    if (abs(len(x_moved) - len(o_moved)) > 1 or
    zeroy == 2 and zerox ==1):
        cprint('\nImpossible', 'red', attrs=['blink'])
        askagain()
    elif zerox ==1:
        cprint('\nX wins ', 'green', attrs=['blink'])
        askagain()
    elif zeroy == 2:
        cprint('\nO wins', 'magenta', attrs=['blink'])
        askagain()
    elif len(x_moved) + len(o_moved) == 9:
        cprint('\nDraw', 'blue', attrs=['blink'])
        quit()
        askagain()
    elif "_" in cells2:
         cprint('\nGame not finished', 'cyan' , attrs=['blink'])
         
         
    
            

def boardfinal():
    print("---------")
    print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
    print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
    print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
    print("---------")
    
def example():
    print(red+" _____ _     _____         _____"+reset)          
    print(red+"|_   _(_) __|_   _|_ _  __|_   _|__   ___ "+reset) 
    print(green+"  | | | |/ __|| |/ _` |/ __|| |/ _ \ / _ \ "+reset) 
    print(green+"  | | | | (__ | | (_| | (__ | | (_) |  __/ "+reset) 
    print(blue+"  |_| |_|\___||_|\__,_|\___||_|\___/ \___| "+reset) 
    print()
    print(red+"---------"+reset)
    print(green +"| " + movelist[0] + " " + movelist[1] + " " + movelist[2] + " |"+reset)
    print(blue+"| " + movelist[3] + " " + movelist[4] + " " + movelist[5] + " |"+reset)
    print(green+"| " + movelist[6] + " " + movelist[7] + " " + movelist[8] + " |"+reset)
    print(red+"---------"+reset)

def clear():
    os.system("clear")
    
    

        

    
def game():
    example()
    #first move
    xmove()
    boardstate()
    clear()
    boardstate()
    checkresult()
    
    #second move
    omove()
    boardstate()
    clear()
    boardstate()
    checkresult()
    
    #third move
   
    xmove2()
    boardstate()
    clear()
    boardstate()
    checkresult()
    

    #fourth move
    omove2()
    boardstate()
    clear()
    boardstate()
    checkresult()
    

    #fifth move
    xmove3()
    boardstate()
    clear()
    boardstate()
    checkresult()
    

    #sixth move
    omove3()
    boardstate()
    clear()
    boardstate()
    checkresult()
    

    #seventh move
    xmove4()
    boardstate()
    clear()
    boardstate()
    checkresult()
    #eighth move
    omove4()
    boardstate()
    clear()
    boardstate()
    checkresult()
    #last move
    xmove5()
    boardfinal()
    checkresult()
    
    
def askagain():
    print("Would you  like to play another Round?"+blue+reset)
    cprint("'Yes' or '-y' to continue ", 'green' , attrs=['blink'])
    cprint("'No' or 'quit' to exit", 'red' , attrs=['blink'])
    print(green+"'L' or '-l' for Licenses and Credits")
    print(blue + "Please " + reset + yellow +"STAR "+ reset + blue + "this on Github"+reset+link)
    rematch = input(">>")
    if rematch in ["Yes","yes","-y","yaaah","-Y","y"]:
        clear()
        game()
    elif rematch in ["no","naah","-n","-q","quit","Quit","n"]:
        clear()
        quit()
    elif rematch in ["-l","L"]:
        Licenses()
        askagain()
    else:
        print("Unknown Command")
        quit()
game()
askagain()
    
    

        
        


 

        
    















        
    
    

