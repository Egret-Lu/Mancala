def initial_game(M=6,B=4):
    list=[0,0];
    for i in range(M):
        list.insert(1,4)
    for i in range(M):
        list.append(4)
    return list