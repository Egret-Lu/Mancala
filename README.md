


## Contents

- [Backgroud](#Background)
- [Install](#install)
- [Usage](#usage)
- [Badge](#badge)
- [Example Readmes](#example)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)

## Background

This project is designed for simulating mancala game. In the directory we used two kind of algorithmns minimax and ab minimax.  Both of them are basic methods of problem solving and this project apply them to mancala game to see in what level each of them are effective.

## Install

To use the method in this project you need to import the module in the directory

```python
from board import *
```

## Usage

Here I write a play.py script to run the mancala game. The program can be invoke by entering two methods as player. For example "**python play.py minimax random**" invoke a program with minimax as player 1 and random as player 2. For choice, all methods I provided includes:

- random: From all avaliable pit, randomly choose one
- human: Select a pit which is choosed by human player
- greedy: Select a  best pit which owns maximum in heuristic function
- minimax: Choose with minimax method
- ab_minimax: Choose with minmax add ab pruning method

You can also use evaluation.py to compare the performence of two methods.

```python
$python play.py minimax random
minimax vs random
player 1 move pit 3
1 ~ |    5||    5||    5||    0||    4||    4|

------------------------------------------------------
    |    4||    4||    4||    4||    4||    4| ~ 0
player 1 move pit 1
1 ~ |    5||    6||    6||    1||    5||    0|

------------------------------------------------------
    |    4||    4||    4||    4||    4||    4| ~ 0
player 2 move pit 1
1 ~ |    5||    6||    6||    1||    5||    0|

------------------------------------------------------
    |    0||    5||    5||    5||    5||    4| ~ 0
  ....
  player 2 move pit 5
7 ~ |    8||    10||    11||    0||    0||    0|

------------------------------------------------------
    |    0||    0||    0||    0||    0||    0| ~ 9
Player 1 wins!
minimax vs random game complete in 1.254120111465454 seconds
```

```python
$ python3 evaluation.py minimax ab_minimax
minimax vs ab_minimax current result:
[5, 0, 0]
Switch!
minimax vs ab_minimax current result:
[5, 5, 0]
minimax vs ab_minimax game complete with 5:5
--------------------
for minimax:
win rate:0.5
loss rate:0.5
draw rate:0.0
--------------------
for ab_minimax:
win rate:0.5
loss rate:0.5
draw rate:0.0
```

## Maintainers

Xinxuan Lu (Lucinda)

ID: 31870054

