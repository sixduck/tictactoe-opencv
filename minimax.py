# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:15:22 2021

@author: luc
"""

import random
def isMovesLeft(board) :
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == '-') :
                return True
    return False



def evaluate(b) :
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):       
            if (b[row][0] == "X"):
                return 10
            elif (b[row][0] == "O") :
                return -10

    for col in range(3) :
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == "X"):
                return 10
            elif (b[0][col] == "O"):
                return -10
 
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
        if (b[0][0] == "X") :
            return 10
        elif (b[0][0] == "O") :
            return -10
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == "X") :
            return 10
        elif (b[0][2] == "O") :
            return -10

    return 0


def minimax(board, depth,alpha,beta, isMax) :
    score = evaluate(board)
    if (score == 10) :
        return score
    if (score == -10) :
        return score
    if (isMovesLeft(board) == False) :
        return 0
    
    if (isMax) :    
        best = -1000
        for i in range(3) :        
            for j in range(3) :
                if (board[i][j]=='-') :
                    board[i][j] = "X"
                    score = minimax(board,depth + 1,alpha,beta,False)
                    board[i][j] = '-'
                    best = max(score,best)
                    alpha = max(alpha,score)
                    if alpha >= beta:
                        break
        return best
    else :
        best = 1000
        for i in range(3) :        
            for j in range(3) :
                if (board[i][j] == '-') :
                    board[i][j] = "O"
                    score = minimax(board, depth + 1,alpha,beta,True)
                    board[i][j] = '-'
                    best = min(score,best)
                    beta = min(beta,score)
                    if alpha >= beta:
                        break
        return best
    
    
def findBestMove(board) :
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(3) :    
        for j in range(3) :
            if (board[i][j] == '-') :
                board[i][j] = "X"
                moveVal = minimax(board, 0,-100,100, False)
                board[i][j] = '-'
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove

def go_first(board):
    first = random.randint(1,2)
    if first == 1:
        move = input('Moi ban di truoc, nhap hang: ')
        move1 = input('nhap o: ')
        board[int(move)][int(move1)] = "O"
        first = 2
        return first, board
    else:
        board[1][1] = 'X'
        first = 1
        return first, board

def switch(player):
    if player == 1:
        player = 2
        return player
    if player == 2:
        player = 1
        return player
    

def isGameEnd(board):
    score = evaluate(board)
    tie = isMovesLeft(board)
    if score == 10 or score == -10 or tie is not True:
        return True
# board = [["-","-","-"],
#           ["-","-","-"],
#           ["-","-","-"]]
# score = isGameEnd(board)
# print(score)
# bestMove = findBestMove(board)
# print("ROW:", bestMove[0], " COL:", bestMove[1])
# print(go_first())
# nextPlayer, gamestate = go_first(board)
# print(nextPlayer)
# print(gamestate)