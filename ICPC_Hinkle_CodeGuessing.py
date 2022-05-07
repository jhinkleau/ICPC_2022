#Code Guessing Solution ICPC 2022
a_cards = [int(num) for num in input().split(" ")]
order = input()
if order == "AABB":
    if 10 - a_cards[1] > 3:
        print(-1)
    else:
        print(a_cards[1]+1, a_cards[1]+2)
if order == "ABAB":
    if a_cards[1] - a_cards[0] > 2:
        print(-1)
    elif 10 - a_cards[1] > 2:
        print(-1)
    else:
        print(a_cards[0]+1 ,  a_cards[1] + 1)
if order == ("ABBA"):
    if a_cards[1] - a_cards[0] > 3:
        print(-1)
    else:
        print((a_cards[0]+1) ,  (a_cards[0]+2))
if order == ("BBAA"):
    if a_cards[0] - 0 > 3:
        print(-1)
    else:
        print(a_cards[0]-2 ,  a_cards[0]-1)
if order == ("BABA"):
    if a_cards[0] - 0 > 2:
        print(-1)
    elif a_cards[1] - a_cards[0] > 2:
        print(-1)
    else:
        print(a_cards[0]-1 ,  a_cards[0]+1)
if order == ("BAAB"):
    if a_cards[0]  - 0 > 2:
        print(-1)
    elif 10 - a_cards[1] > 2:
        print(-1)
    else:
        print(a_cards[0]-1 ,  a_cards[1]+1)