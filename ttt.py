#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:47:25 2020

@author: liwenhuang
tic tac toe game raw
"""
from random import choice
from time import sleep 

class TTT():
    def __init__(self):
        self.board = [[0, 0, 0], 
                      [0, 0, 0], 
                      [0, 0, 0]]
    
    def print_board(self):
        print("-----------")
        for row in self.board:
            for position in row:
                if position:
                    print(position,  end = " | ")
                else:
                    print(" ",  end = " | ")
                   
            print("")
            print("-----------")
            
    
    def is_full(self):
        for row in self.board:
            for position in row:
                if not position:
                    return False
        print("Board is Full!")
        return True
    
    def play(self):
        print("Time to make a move!")
        while True:
            try:
                i = int(input("Put in a row number:"))
            except ValueError:
                print("Only put in number!")
                i = int(input("Put in a row number:"))
            if i < 0 or i > 2:
                print("Row number can only be a number from 0 to 2! Try again!")
                i = int(input("Put in a row number:"))
            try: 
                j = int(input("Put in a Column number:"))
            except ValueError:
                print("Only put in number!")
                j = int(input("Put in a Column number:"))
            if j < 0 or j > 2:
                print("Column number can only be a number from 0 to 2! Try again!")
                j = int(input("Put in a row number:"))
                
            if not self.board[i][j]:
                self.board[i][j] = "x"
                break
            else:
                print("Only make a move if the cell is empty")
                
    #sort out a couple of winning and losing scenarios
    def row_over(self):
        for row in self.board:
            if row == ["o"]*3 :
                print("Game Over!")
                return True
            if row == ["x"]*3:
                print("You Won!")
                return True
            
    def col_over(self):
        for j in range(3):
            col = []
            for i in range(3):
                col.append(self.board[i][j])
            if col == ["o"]*3:
                print("Game Over!")
                return True
            if col == ["x"]*3:
                print("You Won!")
                return True
            
    def diag_over(self):
        right_diag = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if right_diag == ["o"]*3 :
            print("Game Over!")
            return True
        if right_diag == ["x"]*3:
            print("You Won!")
            return True
        left_diag = [self.board[2][0], self.board[1][1], self.board[0][2]]
        if left_diag == ["o"]*3:
            print("Game Over!")
            return True
        if left_diag == ["x"]*3:
            print("You Won!")
            return True
    
    def is_over(self): # determind if one of the player has won or the board is full
       if self.row_over() or self.col_over() or self.diag_over():
        return True
       if self.is_full():
           return True
       return False
    
    def dumb_ai(self):
        avaible_move = []
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]:
                    avaible_move.append([i,j])
        if avaible_move:
            move = choice(avaible_move)
            i, j = move[0], move[1]
            self.board[i][j] ="o"
    
    def play_again(self): # if true, continue the game
        print("Do you want to play again? Y/N")
        return input().lower().startswith('y')
    
    
        
if __name__ == "__main__":
    while True:
        game = TTT()
        print("Welcome to tic-tac-toe!")
        while game.is_over() == False:
            game.play()
            game.print_board()
            sleep(2)
            print("Your opponent just made a move!")
            game.dumb_ai()
            game.print_board()
        if not game.play_again():
            break
        
#        while not game.game_over():
#            game.play()
#            game.print_board()
#            sleep(2)
#            print("Your opponent just made a move!")
#            game.dumb_ai()
#            game.print_board()
#        if game.game_over() or game.is_full():
#            if not game.play_again():
#                break
    
        
        
       
                
            
                