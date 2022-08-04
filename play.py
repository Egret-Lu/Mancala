from board import *
import sys
import time

players=sys.argv
if len(sys.argv)==3:
	player1=players[1]
	player2=players[2]
	print(player1+' vs '+player2)
	start_time=time.time()
	board=Board()
	is_end=board.get_terminal()
	while is_end==0:
	    if board.get_player()==1:
	        board,is_end=eval(player1)(board)
	        if is_end==0:
	            print(board.last_move)
	            board.show_board()
	    if board.get_player()==2:
	        board,is_end=eval(player2)(board)
	        if is_end==0:
	            print(board.last_move)
	            board.show_board()
else:
	print('Wrong input!')
board.end_game()
end_time=time.time()
time_all=end_time-start_time
print(player1+' vs '+player2+' game complete in '+str(time_all)+' seconds')