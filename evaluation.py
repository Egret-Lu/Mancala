from board import *
import sys
import time

#minimax vs random
players=sys.argv
player1=players[1]
player2=players[2]
result=[0,0,0]
for i in range(5):
	board=Board()
	is_end=board.get_terminal()
	while is_end==0:
	    if board.get_player()==1:
	        board,is_end=eval(player1)(board)
	    if board.get_player()==2:
	        board,is_end=eval(player2)(board)
	if board.game_result()==1:
		result[0]+=1   
	if board.game_result()==2:
		result[1]+=1  
	if board.game_result()==0:
		result[2]+=1 
print(player1+' vs '+player2+' current result:')
print(result)
print('Switch!')
for i in range(5):
	board=Board()
	is_end=board.get_terminal()	
	while is_end==0:
	    if board.get_player()==1:
	        board,is_end=eval(player2)(board)
	    if board.get_player()==2:
	        board,is_end=eval(player1)(board)
	
	if board.game_result()==2:
		result[0]+=1   
	if board.game_result()==1:
		result[1]+=1  
	if board.game_result()==0:
		result[2]+=1 
print(player1+' vs '+player2+' current result:')
print(result)
print(player1+' vs '+player2+' game complete with '+str(result[0])+':'+str(result[1]))
print('--------------------')
print('for '+player1+':')
print('win rate:'+str(result[0]/sum(result)))
print('loss rate:'+str(result[1]/sum(result)))
print('draw rate:'+str(result[2]/sum(result)))
print('--------------------')
print('for '+player2+':')
print('win rate:'+str(result[1]/sum(result)))
print('loss rate:'+str(result[0]/sum(result)))
print('draw rate:'+str(result[2]/sum(result)))

