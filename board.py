import random as rm
def initial_game(M=6,B=4):
    list=[0,0];
    for i in range(M):
        list.insert(1,4)
    for i in range(M):
        list.append(4)
    return list
class Board():
    def __init__(self,board=initial_game(),last_step=None,player=1,last_move=None,again=0):
        #board shows in list begin from mancola of player2 and end in the last pit of player2
        #initial one shows like:[0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
        self.__board=board
        self.__M=int((len(board)-2)/2)
        self.__B=sum(board)/(self.__M*2)
        self.__size=len(board)
        self.__m1=board[self.__M+1]
        self.__m2=board[0]
        self.__m=[self.__m1,self.__m2]
        self.__b1=board[1:self.__M+1]
        self.__b2=board[self.__M+2:2*self.__M+2]
        self.__b=[self.__b1,self.__b2]
        self.__last_step=last_step
        self.last_move=last_move
        self.player=player #1,2, player who will go next
        self.again=again
        if not any(self.__b1) or not any(self.__b2):
            self.__terminal=1
        else:
            self.__terminal=0
    def move(self,pit):
        #pit from 1 to M
        board=list(self.__board)
        again=0
        if self.player==1:
            s_num=self.__b1[pit-1]
            begin=pit
            i=1
            board[begin]=0
            while i<=s_num:
                if (begin+i)%self.__size==0:
                #jump mancala of player 2
                    pass
                if i==s_num:
                    if (begin+i)%self.__size==self.__M+1:#last in own mancala
                        board[(begin+i)%self.__size]+=1
                        next_player=1
                        again=1
                        #next_Board=Board(board,self,1)
                    elif board[(begin+i)%self.__size]==0 and (begin+i)%self.__size>=1 and (begin+i)%self.__size<=self.__M:
                        this=(begin+i)%self.__size; # location my side
                        that=2*self.__M+2-this #location of opposite side
                        board[self.__M+1]=board[self.__M+1]+board[this]+board[that]+1 # get all stone and put in my own mancala
                        board[this]=0
                        board[that]=0
                        next_player=2
                        #next_Board=Board(board,self,2)
                    else:
                        board[(begin+i)%self.__size]+=1
                        next_player=2
                        #next_Board=Board(board,self,2)
                    i+=1         
                else:
                    board[(begin+i)%self.__size]+=1
                    i+=1
        #for player 2    
        elif self.player==2:
            s_num=self.__b2[pit-1]
            begin=self.__M+2+pit-1
            i=1
            board[begin]=0
            while i<=s_num:
                if (begin+i)%self.__size==(self.__M+1):
                #jump mancala of player 2
                    pass
                if i==s_num:
                    if (begin+i)%self.__size==0:#last in own mancala
                        board[(begin+i)%self.__size]+=1
                        next_player=2
                        again=1
                        #next_Board=Board(board,self,2)
                    elif board[(begin+i)%self.__size]==0 and (begin+i)%self.__size>=self.__M+2 and (begin+i)%self.__size<=2*self.__M+1:
                        this=(begin+i)%self.__size; # location my side
                        that=2*self.__M+2-this #location of opposite side
                        board[0]=board[self.__M+1]+board[this]+board[that]+1 # get all stone and put in my own mancala
                        board[this]=0
                        board[that]=0
                        next_player=1
                        #next_Board=Board(board,self,1)
                    else:
                        board[(begin+i)%self.__size]+=1
                        next_player=1
                        #next_Board=Board(board,self,1)
                    i+=1          
                else:    
                    board[(begin+i)%self.__size]+=1
                    i+=1
        next_Board=Board(board,self,next_player,None,again)
        last_move='player '+str(self.player)+' move pit '+str(pit)
        next_Board.last_move=last_move
        return next_Board,again

    def show_board(self):
        print(str(self.__m1)+' ~ ',end='')
        for i in range(len(self.__b1)):
            j=self.__b1[len(self.__b1)-1-i]
            print('|    '+str(j),end='|')
        print('\n')
        print('------------------------------------------------------')
        print('    ',end='')
        for i in range(len(self.__b2)):
            j=self.__b2[i]
            print('|    '+str(j),end='|')
        print(' ~ '+str(self.__m2))

    def heuristic(self,player):
        a=1
        b=0.7
        if player==2:#if next is player 1 then show score of board for player 2            
            if self.__terminal==1:
                h=self.__m2+sum(self.__b2)-(self.__m1+sum(self.__b1))
            else:
                h=self.__m2*a+sum(self.__b2)*b-(self.__m1*a+sum(self.__b1)*b)
        elif player==1:           
            if self.__terminal==1:
                h=self.__m1+sum(self.__b1)-(self.__m2+sum(self.__b2))
            else:
                h=self.__m1*a+sum(self.__b1)*b-(self.__m2*a+sum(self.__b2)*b)
        return h
    
    def avaliable_pit(self):
        board_self=self.__b[self.player-1]
        av_pits=[]
        for i in range(len(board_self)):
            if board_self[i]!=0:
                av_pits.append(i+1)
        return av_pits

    def end_game(self,out=0):
        if out==0:
            if self.__terminal==1:
                if(self.__m1+sum(self.__b1))>(self.__m2+sum(self.__b2)):
                    print('Player 1 wins!')
                elif (self.__m1+sum(self.__b1))<(self.__m2+sum(self.__b2)):
                    print('Player 2 wins!')
                elif (self.__m1+sum(self.__b1))==(self.__m2+sum(self.__b2)):
                    print('Draw')
            else:
                print('Game Continuing')
        else:
            print('Player '+str(out)+' out!')
            print('Player '+str((out+1)%2)+' wins!')

    def game_result(self,out=0):
        if out==0:
            if self.__terminal==1:
                if(self.__m1+sum(self.__b1))>(self.__m2+sum(self.__b2)):
                    return 1
                elif (self.__m1+sum(self.__b1))<(self.__m2+sum(self.__b2)):
                    return 2
                elif (self.__m1+sum(self.__b1))==(self.__m2+sum(self.__b2)):
                    return 0
            else:
                print('Game Continuing')
        else:
            return int((out+1)%2)


            
        
        
    
    def get_board(self):
        return self.__board
    def get_M(self):
        return self.__M
    def get_B(self):
        return self.__B
    def get_lastb(self):
        return self.__last_step
#     def get_m1(self):
#         return self.__m1
#     def get_m2(self):
#         return self.__m2
#     def get_b1(self):
#         return self.__b1
#     def get_b2(self):
#         return self.__b2
#     def get_next_step(self):
#         return self.__next_step
    def get_player(self):
        return self.player
    def get_terminal(self):
        return self.__terminal

def random(board):
    #randomly choose 
    is_end=0
    if board.get_terminal():
        is_end=1
        #board.end_game()
        return board,is_end
    av_pits=board.avaliable_pit()
    pit=rm.choice(av_pits)
    next_board,again=board.move(pit)
    # print(next_board.last_move)
    # next_board.show_board()
    return next_board,is_end


def greedy(board):
    #use greedy methods
    is_end=0
    if board.get_terminal():
        is_end=1
        #board.end_game()
        return board,is_end
    av_pits=board.avaliable_pit()
    next_candidate=[]
    for pit in av_pits:
        next_board,again=board.move(pit)
        next_candidate.append(next_board)
    next_candidate.sort(key=lambda x:x.heuristic(x.get_lastb().player),reverse=True)
    next_board=next_candidate[0]
    # print(next_board.last_move)
    # next_board.show_board()
    return next_board,is_end

def human(board):
    is_end=0
    if board.get_terminal():
        is_end=1
        #board.end_game()
        return board,is_end
    pit=-1
    av_pits=board.avaliable_pit()
    n=0
    while pit not in av_pits:
        if n==0:
            pit=int(input('player'+str(board.player)+' input your next pit you want to move (in 1 - '+ str(board.get_M())+'):'))
        else:
            if n>5:
                print('try too many times, you lose')
                board.end_game(board.player)
                is_end=1
                return board,is_end
            else:
                print('You can not move this pit, try another.')
                pit=int(input('player'+str(board.player)+'input your next pit you want to move (in 1 - '+ str(board.get_M())+'):'))
        n=n+1    
    next_board,again=board.move(pit)
    # print(next_board.last_move)
    # next_board.show_board()
    return next_board,is_end

#minimax
def minimax(board,maxdepth=4):
    is_end=0
    if board.get_terminal():
        is_end=1
        #board.end_game()
        return board,is_end
    next_board,next_score=maxmize(board,maxdepth,0,board.player)
    # print(next_board.last_move)
    # next_board.show_board()
    return next_board,is_end

def maxmize(board,maxdepth,depth,player):
    bestboard=board
    bestscore=-100000
    #initial best choice
    if board.again==1:
        next_depth=depth
    else:
        next_depth=depth+1
    if (depth>=maxdepth and board.again==0) or (board.get_terminal()==1):
        return board,board.heuristic(player)
    av_pits=board.avaliable_pit()

    for pit in av_pits:
        next_board,next_again=board.move(pit)
        if next_again:
            c_board,c_score=maxmize(next_board,maxdepth,next_depth,player)
        else:
            c_board,c_score=minmize(next_board,maxdepth,next_depth,player)
        if c_score>bestscore:
            bestboard=next_board
            bestscore=c_score
    return bestboard,bestscore

def minmize(board,maxdepth,depth,player):
    bestboard=board
    bestscore=100000
    #initial best choice
    if board.again==1:
        next_depth=depth
    else:
        next_depth=depth+1
    if (depth>=maxdepth and board.again==0) or (board.get_terminal()==1):
        return board,board.heuristic(player)
    av_pits=board.avaliable_pit()
    for pit in av_pits:
        next_board,next_again=board.move(pit)
        if next_again:
            c_board,c_score=minmize(next_board,maxdepth,next_depth,player)   
        else:
            c_board,c_score=maxmize(next_board,maxdepth,next_depth,player) 
        if c_score<bestscore:
            bestboard=next_board
            bestscore=c_score
    return bestboard,bestscore

#alphabeta
def ab_minimax(board,maxdepth=4,a=-5,b=5):
    is_end=0
    if board.get_terminal():
        is_end=1
        #board.end_game()
        return board,is_end
    next_board,next_score=abmaxmize(board,maxdepth,0,a,b,board.player)
    # print(next_board.last_move)
    # next_board.show_board()
    return next_board,is_end

def abmaxmize(board,maxdepth,depth,a,b,player):
    bestboard=board
    bestscore=-100000
    #initial best choice
    if board.again==1:
        next_depth=depth
    else:
        next_depth=depth+1
    if (depth>=maxdepth and board.again==0) or (board.get_terminal()==1):
        return board,board.heuristic(player)
    av_pits=board.avaliable_pit()
    for pit in av_pits:
        next_board,next_again=board.move(pit)
        if next_again:
            c_board,c_score=abmaxmize(next_board,maxdepth,next_depth,a,b,player)
        else:
            c_board,c_score=abminmize(next_board,maxdepth,next_depth,a,b,player)
        if c_score>bestscore:
            bestboard=next_board
            bestscore=c_score
        if c_score>=b:
            return bestboard,bestscore
    return bestboard,bestscore

def abminmize(board,maxdepth,depth,a,b,player):
    bestboard=board
    bestscore=100000
    #initial best choice
    if board.again==1:
        next_depth=depth
    else:
        next_depth=depth+1
    if (depth>=maxdepth and board.again==0) or (board.get_terminal()==1):
        return board,board.heuristic(player)
    av_pits=board.avaliable_pit()
    for pit in av_pits:
        next_board,next_again=board.move(pit)
        if next_again:
            c_board,c_score=abminmize(next_board,maxdepth,next_depth,a,b,player)   
        else:
            c_board,c_score=abmaxmize(next_board,maxdepth,next_depth,a,b,player) 
        if c_score<bestscore:
            bestboard=next_board
            bestscore=c_score
        if c_score<=a:
            return bestboard,bestscore
    return bestboard,bestscore




