__author__ = 'bommaritoe16'
import Card
import random
import Score
#A!L4n58UrY student wifi
class Deck():
    card_list = []
    used_pile = []
    hand = []
    note = []

    def __init__(self):
        self.card_list = [Card.Card() for i in range(10)]

    def rano_shit(self):
        for i in range(10):
            if(i < 7): self.card_list[i].set("Copper","+1 Coin",0)
            if(i>= 7): self.card_list[i].set("Estate","1 Point",2)
        self.shuffle()
        self.draw(5)

    def shuffle(self):
        if len(self.card_list) == 0:
            self.reset_deck()
        old_list = self.card_list
        new_list = []
        for i in range(len(old_list)):
            r = random.randint(0,len(old_list)-1)
            new_list.append(old_list[r])
            del old_list[r]
            self.card_list = new_list

    def reset_deck(self):
        self.card_list = self.used_pile
        self.used_pile = []
        self.shuffle

    def use(self,x,s):
        if self.hand[x].name == "Copper":
            s.gold +=1
            self.used_pile.append(self.hand[x])
            del self.hand[x]
        elif self.hand[x].name == "Silver":
            s.gold += 2
            self.used_pile.append((self.hand[x]))
            del self.hand[x]
        elif self.hand[x].name == "Gold":
            s.gold += 3
            self.used_pile.append((self.hand[x]))
            del self.hand[x]
        elif s.actions > 0:
            s.actions += -1
            if self.hand[x].name == "Village":
                s.actions +=2
                self.draw(1)
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Smithy":
                self.draw(3)
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Market":
                s.gold += 1
                s.buys +=1
                s.actions +=1
                self.draw(1)
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Mine":
                self.note = "Mine"
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Moat":
                self.draw(2)
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Bueraucrat":
                self.note = "Bueraucrat"
                card = Card.Card()
                card.set("Silver","+2 Gold",3)
                self.card_list.insert(0,card)
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Remodel":
                self.note = "Remodel"
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Spy":
                self.note = "Spy"
                self.used_pile.append((self.hand[x]))
                s.actions +=1
                del self.hand[x]
            elif self.hand[x].name == "Cellar":
                s.actions +=1
                self.used_pile.append((self.hand[x]))
                self.note = "Cellar"
                del self.hand[x]
            elif self.hand[x].name == "Library":
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
                self.note = "Library"
            elif self.hand[x].name == "Chapel":
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
                self.note = "Chapel"
            elif self.hand[x].name == "Moneylender":
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
                self.note = "Moneylender"
            elif self.hand[x].name == "Laboratory":
                self.draw(2)
                s.actions+=1
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Woodcutter":
                s.buys +=1
                s.gold += 2
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
            elif self.hand[x].name == "Workshop":
                self.used_pile.append((self.hand[x]))
                del self.hand[x]
                self.note = "Workshop"

            else: s.actions+=1

    def draw(self,n):
        for i in range(n):
            if(len(self.card_list)==0): self.reset_deck();self.shuffle()
            c = self.card_list[0]
            self.hand.append(c)
            del self.card_list[0]

    def end(self):
        for i in range(len(self.hand)):
            self.used_pile.append(self.hand[0])
            del self.hand[0]
        self.draw(5)

    def check_point(self,s):
        self.card_list.append(self.hand)
        self.card_list.append(self.used_pile)
        for i in range(len(self.card_list)):
            if(self.card_list[i].name == "Estate"):
                s.score +=1
            elif(self.card_list[i].name == "Duchy"):
                s.score +=2
            elif(self.card_list[i].name == "Province"):
                s.score +=3
            elif(self.card_list[i].name == "Garden"):
                s.score += int(len(self.card_list)/10)