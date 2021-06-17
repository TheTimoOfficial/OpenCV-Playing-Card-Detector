from collections import namedtuple
from collections import defaultdict
import re

#Globale Variablen
card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
rank_kurz = {"Ace": 'A', "Two": '2', "Three": '3', "Four": '4', "Five": '5', "Six": '6', "Seven": '7', "Eight": '8', "Nine": '9', "Ten": 'T', "Jack": 'J', "Queen": 'Q', "King": 'K'}
color_kurz = {"Hearts": 'H', "Spades": 'S', "Clubs": 'C', "Diamonds": 'D'}
hand_order = {10: 'Royal Flush', 9 : 'Straight Flush', 8 : 'Quads', 7 : 'Full House', 6 : 'Flush', 5 : 'Straight', 4 : 'Three of a Kind', 3 : 'Two Pair', 2 : 'Pair', 1 : 'High Card'}

#getAllCards bereitet die Karten, die vom CardViewer kommen, zur Analyse vor
def getAllCards(cardlist):
    shortcardlist = []
   
   #Diser Loop kürzt den Kartennahmen. Z.B. 'SpadesTwo' -> '2S' oder 'DiamondsKing' -> 'KD'
    for card in cardlist:

        splitcard = re.findall('[A-Z][^A-Z]*', card)

        color = splitcard[0][0]
        rank = rank_kurz[splitcard[1]]

        shortcard = rank + color
        shortcardlist.append(shortcard)

    #Variablen deklaration
    middleCards = shortcardlist[0:5]
    restCards  = shortcardlist[5:]
    playeramount = len(restCards) / 2
    cardsindex = 0
    playernumber = 1


    while playernumber <= playeramount:

        nextindex = cardsindex + 2
        playerCards = restCards[cardsindex:nextindex]
        hand = middleCards + playerCards

        result = check_hand(hand)
        print("Spieler", playernumber, ':', hand_order[result])
        playernumber = playernumber + 1
        cardsindex = cardsindex + 2



       
def check_hand(hand):
    
    if check_royal_flush(hand):
        return 10

    if check_straight_flush(hand):
        return 9

    if check_four_of_a_kind(hand):
        return 8

    if check_full_house(hand):
        return 7

    if check_flush(hand):
        return 6

    if check_straight(hand):
        return 5

    if check_three_of_a_kind(hand):
        return 4

    if check_two_pairs(hand):
        return 3

    if check_one_pairs(hand):
        return 2
    



def check_royal_flush(hand):
    return False




#Funktioniert
def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False




#Funktioniert
def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,1,4] or sorted(value_counts.values()) == [1,2,4] or sorted(value_counts.values()) == [3,4] :
        return True
    return False





#Funktioniert
def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,1,2,3] or sorted(value_counts.values()) == [2,2,3]:
        return True
    return False





#Funktioniert
def check_flush(hand):

    cardcolors = {
    'clubs' : 0,
    'diamonds' : 0,
    'spades' : 0,
    'hearts' : 0
    }
    

    for card in hand:

        if card.startswith('Clubs'):
            cardcolors['clubs'] = cardcolors['clubs'] + 1
        elif card.startswith('Diamonds'):
            cardcolors['diamonds'] = cardcolors['diamonds'] + 1
        elif card.startswith('Spades'):
            cardcolors['spades'] = cardcolors['spades'] + 1
        else:
            cardcolors['hearts'] = cardcolors['hearts'] + 1

    for x in cardcolors:
        if cardcolors[x] >= 5:
            return True
            break
        else:
            return False

    
    '''
    suits = [i[1] for i in hand]

    lengh = len(set(suits))

    if lengh ==3 or lengh == 2:
        return True
    else:
        return False
    '''





#Funktioniert
def check_straight(hand):
    count = 0
    handranks = []

    for card in hand:
        thisrank = card_order_dict[card[0]]
        handranks.append(thisrank)
    
    for rank in (14, *range(2, 15)):
        if rank in handranks:
            count += 1
            if count == 5:
                return True
                break
        else:
            count = 0

    


#Funktioniert?
def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False





#Funktioniert
def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,1,1,2,2] or sorted(value_counts.values())==[1,2,2,2]:
        return True
    else:
        return False





#Funktioniert
def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False















































































'''
def checkRoyalty(wholeCards):
    pass



#Check if the Hand is a Flush, if so, check if its a Straight or a Royal Flush
def checkFlush(hand):
    cardcolors = {
    'clubs' : 0,
    'diamonds' : 0,
    'spades' : 0,
    'hearts' : 0
    }
    

    for card in hand:

        if card.startswith('Clubs'):
            cardcolors['clubs'] = cardcolors['clubs'] + 1
        elif card.startswith('Diamonds'):
            cardcolors['diamonds'] = cardcolors['diamonds'] + 1
        elif card.startswith('Spades'):
            cardcolors['spades'] = cardcolors['spades'] + 1
        else:
            cardcolors['hearts'] = cardcolors['hearts'] + 1

    for x in cardcolors:
        if cardcolors[x] >= 5:
            isFlush = True
            isStraight = checkStraight(hand)
            break
        else:
            isFlush = False

    return isFlush, isStraight



def checkStraight(hand):
    cardranks = {
        'Ace' : 0,
        'Two' : 0,
        'Three': 0,
        'Four' : 0,
        'Five' : 0,
        'Six' : 0,
        'Seven' : 0,
        'Eight' : 0,
        'Nine' : 0,
        'Ten' : 0,
        'Jack' : 0,
        'Queen' : 0,
        'King' : 0
    }

    for card in hand:
        pass
        




def checkQuads(hand):
    pass



def checkThreeOfKind(hand):
    pass



def checkPair(hand):
    pass


#Die 2 Karten des Spielers nach der höchsten filtern
def checkHighCard(playerCard):
    pass 
'''