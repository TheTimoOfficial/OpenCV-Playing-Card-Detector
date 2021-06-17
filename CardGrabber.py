import CardViewer

#Liste aller Karten mit Zähler
cardindex = {
    "SpadesAce": 0,
    "SpadesTwo": 0,
    "SpadesThree": 0,
    "SpadesFour": 0,
    "SpadesFive": 0,
    "SpadesSix": 0,
    "SpadesSeven": 0,
    "SpadesEight": 0,
    "SpadesNine": 0,
    "SpadesTen": 0,
    "SpadesJack": 0,
    "SpadesQueen": 0,
    "SpadesKing": 0,

    "ClubsAce": 0,
    "ClubsTwo": 0,
    "ClubsThree": 0,
    "ClubsFour": 0,
    "ClubsFive": 0,
    "ClubsSix": 0,
    "ClubsSeven": 0,
    "ClubsEight": 0,
    "ClubsNine": 0,
    "ClubsTen": 0,
    "ClubsJack": 0,
    "ClubsQueen": 0,
    "ClubsKing": 0,

    "DiamondsAce": 0,
    "DiamondsTwo": 0,
    "DiamondsThree": 0,
    "DiamondsFour": 0,
    "DiamondsFive": 0,
    "DiamondsSix": 0,
    "DiamondsSeven": 0,
    "DiamondsEight": 0,
    "DiamondsNine": 0,
    "DiamondsTen": 0,
    "DiamondsJack": 0,
    "DiamondsQueen": 0,
    "DiamondsKing": 0,

    "HeartsAce": 0,
    "HeartsTwo": 0,
    "HeartsThree": 0,
    "HeartsFour": 0,
    "HeartsFive": 0,
    "HeartsSix": 0,
    "HeartsSeven": 0,
    "HeartsEight": 0,
    "HeartsNine": 0,
    "HeartsTen": 0,
    "HeartsJack": 0,
    "HeartsQueen": 0,
    "HeartsKing": 0, }
#Liste der erkannten Karten
cardlist = []                                      


def getCard(Card, count):

    #Variablen für eine Karte
    cardnum = Card.best_rank_match      #Kartenwert
    cardcol = Card.best_suit_match      #Kartenfarbe
   

    #IF-Abfrage die Unerkannte Karten Filtert
    if cardnum != 'Unknown' and cardcol != 'Unknown':

        cardsum = cardcol + cardnum                     #Kartenname gesamt
        cardindex[cardsum] = cardindex[cardsum] + 1
        validateCard(cardsum, count)

    else:
        pass
        
def validateCard(Card, count):
    
    if count >= 25 and cardindex[Card] >= 20:

        if Card == 'HeartsAce':
            cardlist.clear()
            CardViewer.purgecards()


        if Card not in cardlist and Card != 'HeartsAce':
            cardlist.append(Card)
            print(cardlist)
            CardViewer.drawcard(Card)
            cardindex.fromkeys(cardindex, 0)
        else:
            pass

    elif count >= 25 and cardindex[Card] < 20:
        
        cardindex.fromkeys(cardindex, 0)

    else:
        pass 
