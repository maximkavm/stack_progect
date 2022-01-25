from collections import deque

if __name__ == '__main__':
    player1 = deque()
    player2 = deque()

    pl1 = input().split()
    pl2 = input().split()

    for i in range(len(pl1)):
        player1.append(int(pl1[i]))
    for i in range(len(pl2)):
        player2.append(int(pl2[i]))

    count = 0
    while count < 10 ** 6 and len(player1) > 0 and len(player2) > 0:
        count += 1
        card_pl1 = player1.popleft()
        card_pl2 = player2.popleft()

        if card_pl1 == 0 and card_pl2 == 9:
            player1.append(card_pl1)
            player1.append(card_pl2)
            continue

        if card_pl1 == 9 and card_pl2 == 0:
            player2.append(card_pl1)
            player2.append(card_pl2)
            continue

        if card_pl1 > card_pl2:
            player1.append(card_pl1)
            player1.append(card_pl2)
        else:
            player2.append(card_pl1)
            player2.append(card_pl2)

if count > 10 ** 6:
    print('botva')
else:
    if len(player1) == 0:
        print('second', count)
    else:
        print('first', count)
