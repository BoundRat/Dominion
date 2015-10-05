__author__ = 'bommaritoe16'
import random
import Card
import Score
import Deck

class Field():
    field = []
    total_cards = []

    def __init__(self):
        self.total_cards = [["Copper","+1 Gold",0,45],["Silver","+2 Gold",3,40],["Gold","+3 Gold",6,30],["Estate", "1 Point",2,8],["Duchy","2 Points",5,8],["Province","3 Points",8,8],
                            ["Village","Cycle +Action",3,10],["Spy","Spy, Cycle",4,10],["Smithy","Draw 3",4,10],["Market","Everything 1",5,10],["Mine","Upgrade Treasure",5,10],
                            ["Remodel","Trash Card +2",4,10],["Chapel","Trash 4",2,10],["Cellar","Cycle Hand",2,10],["Bueraucrat","Fateseal",4,10],["Moat","Draw 2, Block",2,10],
                            ["Library","Draw til 7",5,10],["Moneylender","3$ for Copper",4,10],["Laboratory","Cycle +Card",5,10],["Woodcutter","+Buy +2$",3,10],["Workshop","4$ Card",3,10],
                            ]
        temp = self.total_cards
        for i in range(6):
            self.field.append(temp[i])
        for i in range(8):
            r = random.randint(7,len(temp))-1
            self.field.append(temp[r])
            del temp[r]


    def buy(self,n,d,s):
        buy_card = Card.Card()
        buy_card.set(self.field[n][0],self.field[n][1],self.field[n][2])
        if s.gold >= self.field[n][2]:
            if s.buys > 0:
                s.gold += -self.field[n][2]
                d.used_pile.append(buy_card)
                s.buys += -1
                self.field[n][3] += -1

    def buy_special(self,n,d,value):
        buy_card = Card.Card()
        buy_card.set(self.field[n][0],self.field[n][1],self.field[n][2])
        if value >= self.field[n][2]:
            d.used_pile.append(buy_card)
            self.field[n][3] += -1

    def check_end(self):
        empty = 0
        for i in range(len(self.field)):
            if self.field[i][3] == 0:
                empty +=1
        if empty ==3 : return True
