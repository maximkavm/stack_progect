from collections import deque

if __name__ == '__main__':
    player1 = deque()
    player2 = deque()

    # player1 = [int,input().split()]
    # player2 = [int, input().split()]
    pl1 = [1, 3, 5, 7, 9]
    pl2 = [2, 4, 6, 8, 0]

    for i in range(len(pl1)):
        player1.append(pl1[i])
    for i in range(len(pl2)):
        player2.append(pl2[i])
    print(*player1)
    print(*player2)
    count = 0
    while count < 10 ** 6 and len(player1) > 0 and len(player2) > 0:
        count += 1
        card_pl1 = player1.popleft()
        card_pl2 = player2.popleft()
        if (card_pl1 != 0 and card_pl2 != 9) or (card_pl1 != 9 and card_pl2 != 0):
            if card_pl1 > card_pl2:
                player2.append(card_pl1)
                player2.append(card_pl2)
            else:
                player1.append(card_pl1)
                player1.append(card_pl2)
        else:
            if card_pl1 < card_pl2:
                player2.append(card_pl1)
                player2.append(card_pl2)
            else:
                player1.append(card_pl1)
                player1.append(card_pl2)



    print(*player1)
    print(*player2)
    print(count)

    if count > 10 ** 6:
        print('botva')
    else:
        if len(player1) == 0:
            print('second')
        else:
            print('first')
