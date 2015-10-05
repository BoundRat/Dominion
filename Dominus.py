__author__ = 'bommaritoe16'
import curses
import Deck
import Score
import Field
import Card
import os
import sys

os.system("mode con: cols=100 lines =25")
class Con():

    scores = []
    field = []
    thand = []
    win = []
    deckd = []
    screen = []
    start = 0
    def __init__(self):
        #init screen and window
        self.screen = curses.initscr()
        self.win = curses.newwin(0,0,0,0)
        curses.noecho()
        curses.curs_set(0)
        #color
        curses.start_color()
        curses.use_default_colors()
        #init hand
        self.thand = self.win.subwin(15,50,0,0)
        self.scores = self.win.subwin(15,20,0,49)
        self.fieldsc = self.win.subwin(0,0,14,0)
        #init deck
        self.deckd = Deck.Deck()
        self.deckd.rano_shit()
        self.f = Field.Field()

    def draw_hand(self,c,deckd):
        #redraw hand
        c.thand.clear()
        for i in range(len(c.deckd.hand)-c.start):
            #truncates hand
            if i >= 5:
                c.thand.addstr(11,1,"Press s to see rest of hand.")
                break
            stur = str(i+1) + ". " + str(c.deckd.hand[i+c.start].name)
            stur2 = str(c.deckd.hand[i+c.start].text)
            c.thand.addstr(1+i*2,1,stur)
            c.thand.addstr(1+i*2+1,10,stur2)

    def draw_field(self,c,deckd):
        #variable for "start of hand"
        #reset field, so you redraw 'dat shit
        c.fieldsc.clear()
        #prints field
        for i in range(len(c.f.field)):
            #ref for buy
            ref = i+1
            if i == 9: ref = 'a'
            elif i == 10: ref = 'b'
            elif i == 11: ref = 'c'
            elif i == 12: ref = 'd'
            elif i == 13: ref = 'e'
            stur = str(ref) + ". " + str(c.f.field[i][0]) + ":$" + str(c.f.field[i][2]) + "#" + str(c.f.field[i][3])
            stur2 = str(c.f.field[i][1])
            if(i < 4):
                c.fieldsc.addstr(1+i*2,1,stur)
                c.fieldsc.addstr(2+i*2,3,stur2)
            elif (i >= 4 and i < 8):
                c.fieldsc.addstr(1+(i-4)*2,20,stur)
                c.fieldsc.addstr(2+(i-4)*2,22,stur2)
            elif(i >= 8 and i < 12):
                c.fieldsc.addstr(1+(i-8)*2,38,stur)
                c.fieldsc.addstr(2+(i-8)*2,40,stur2)
            elif(i >= 12):
                c.fieldsc.addstr(1+(i-12)*2,56,stur)
                c.fieldsc.addstr(2+(i-12)*2,58,stur2)





c = Con()
s = Score.Score()
while 1:
    c.draw_field(c,c.deckd)

    #redraw hand
    c.draw_hand(c,c.deckd)

    #shows "score" window
    c.scores.addstr(1,1,"Gold: " + str(s.gold))
    c.scores.addstr(3,1,"Actions: " + str(s.actions))
    c.scores.addstr(5,1,"Deck: " + str(len(c.deckd.card_list)))
    c.scores.addstr(7,1,"Used: " + str(len(c.deckd.used_pile)))
    c.scores.addstr(9,1,"Buys: " + str(s.buys))

    #draws boxes
    c.win.border(0)
    c.fieldsc.border(0)
    c.thand.border(0)
    c.scores.border(0)
    c.screen.refresh()
    c.win.refresh()

    #catches user input
    d = c.screen.getch()

    #using cards in hand
    if d == ord('1'):
        #makes sure the card *exists*
        if(len(c.deckd.hand)>=1):
            c.deckd.use(0+c.start,s)
    elif d == ord('2'):
        if(len(c.deckd.hand)>=2):
            c.deckd.use(1+c.start,s)
    elif d == ord('3'):
        if(len(c.deckd.hand)>=3):
            c.deckd.use(2+c.start,s)
    elif d == ord('4'):
        if(len(c.deckd.hand)>=4):
            c.deckd.use(3+c.start,s)
    elif d == ord('5'):
        if(len(c.deckd.hand)>=5):
            c.deckd.use(4+c.start,s)

    #check note

    #Chapel
    if(c.deckd.note == "Chapel"):
        i = 0
        while i < 4:
            c.draw_hand(c,c.deckd)
            c.thand.border(0)
            c.win.border(0)
            c.thand.refresh()
            quitscr.clear()
            quitscr.border(0)
            quitscr.addstr(1,1,"Trash up to 4, e to end.")
            quitscr.refresh()
            q = c.screen.getch()
            if len(c.deckd.hand) == 0: break
            elif q == ord('e'):quitscr.clear();break
            elif q == ord('s'):
                if len(c.deckd.hand) > c.start+5:
                    c.start +=5
                else: c.start = 0
            elif q == ord('1'): del c.deckd.hand[0+c.start];quitscr.clear();i+=1
            elif q == ord('2'): del c.deckd.hand[1+c.start];quitscr.clear();i+=1
            elif q == ord('3'): del c.deckd.hand[2+c.start];quitscr.clear();i+=1
            elif q == ord('4'): del c.deckd.hand[3+c.start];quitscr.clear();i+=1
            elif q == ord('5'): del c.deckd.hand[4+c.start];quitscr.clear();i+=1
        quitscr.clear()
        c.deckd.note = ""

    #Moneylender
    if c.deckd.note == "Moneylender":
        copyes = False
        for i in range(len(c.deckd.hand)):
            if c.deckd.hand[i].name == "Copper":
                copyes = True
        if not copyes:c.deckd.note="";break
        c.draw_hand(c,c.deckd)
        c.thand.border(0)
        c.win.border(0)
        c.thand.refresh()
        quitscr.clear()
        quitscr.border(0)
        quitscr.addstr(1,1,"Discard a Copper for 3$, e to quit")
        quitscr.refresh()
        q = c.screen.getch()
        if q == ord('e'):quitscr.clear();c.deckd.note=""
        elif q == ord('s'):
            if len(c.deckd.hand) > c.start+5: c.start +=5
            else: c.start = 0
        elif q == ord('1'):
            if len(c.deckd.hand) >= 1:
                if c.deckd.hand[0].name == "Copper":
                    del c.deckd.hand[0]
                    s.gold +=3
        elif q == ord('2'):
            if len(c.deckd.hand) >= 2:
                if c.deckd.hand[1].name == "Copper":
                    del c.deckd.hand[1]
                    s.gold +=3
        elif q == ord('3'):
            if len(c.deckd.hand) >= 3:
                if c.deckd.hand[2].name == "Copper":
                    del c.deckd.hand[2]
                    s.gold +=3
        elif q == ord('4'):
            if len(c.deckd.hand) >= 4:
                if c.deckd.hand[3].name == "Copper":
                    del c.deckd.hand[3]
                    s.gold +=3
        elif q == ord('5'):
            if len(c.deckd.hand) >= 5:
                if c.deckd.hand[4].name == "Copper":
                    del c.deckd.hand[4]
                    s.gold +=3

        quitscr.clear()
        c.deckd.note = ""

    #Workshop
    if c.deckd.note == "Workshop":
        c.draw_hand(c,c.deckd)
        c.thand.border(0)
        c.win.border(0)
        c.thand.refresh()
        quitscr.clear()
        quitscr.border(0)
        quitscr.addstr(1,1,"Take a card up to $4, hit q to end.")
        quitscr.refresh()
        q = c.screen.getch()
        while True:
            if q == ord('q'):quitscr.clear();break
            elif q == ord('1'): c.f.buy_special(0,c.deckd,4);break
            elif q == ord('2'): c.f.buy_special(1,c.deckd,4);break
            elif q == ord('3'): c.f.buy_special(2,c.deckd,4);break
            elif q == ord('4'): c.f.buy_special(3,c.deckd,4);break
            elif q == ord('5'): c.f.buy_special(4,c.deckd,4);break
            elif q == ord('6'): c.f.buy_special(5,c.deckd,4);break
            elif q == ord('7'): c.f.buy_special(6,c.deckd,4);break
            elif q == ord('8'): c.f.buy_special(7,c.deckd,4);break
            elif q == ord('9'): c.f.buy_special(8,c.deckd,4);break
            elif q == ord('a'): c.f.buy_special(9,c.deckd,4);break
            elif q == ord('b'): c.f.buy_special(10,c.deckd,4);break
            elif q == ord('c'): c.f.buy_special(11,c.deckd,4);break
            elif q == ord('d'): c.f.buy_special(12,c.deckd,4);break
            elif q == ord('e'): c.f.buy_special(13,c.deckd,4);break
            else: quitscr.clear(); quitscr.border(0); quitscr.addstr(1,1,"Wut.");quitscr.refresh()

        quitscr.clear()
        c.deckd.note = ""



    #Libary
    if(c.deckd.note == "Library"):
        dr = 7 - len(c.deckd.hand)
        while dr > 0:
            if len(c.deckd.card_list) <= 0: c.deckd.reset_deck();c.win.refresh()
            elif not(c.deckd.card_list[0].name == "Copper" or c.deckd.card_list[0].name == "Silver" or c.deckd.card_list[0].name == "Gold"
                     or c.deckd.card_list[0].name == "Estate" or c.deckd.card_list[0].name == "Province" or c.deckd.card_list[0].name == "Duchy"):
                c.draw_hand(c,c.deckd)
                c.thand.border(0)
                c.win.border(0)
                c.thand.refresh()
                quitscr.clear()
                quitscr.border(0)
                quitscr.addstr(1,1," Discard " + str(c.deckd.card_list[0].name)+  "? Y/N")
                quitscr.refresh()
                q = c.screen.getch()
                if q == ord('Y'):
                    c.deckd.used_pile.append(c.deckd.card_list[0])
                    del c.deckd.card_list[0]
                    quitscr.clear()
                elif q == ord('N'):
                    c.deckd.hand.append(c.deckd.card_list[0])
                    del c.deckd.card_list[0]
                    dr += -1
                    quitscr.clear()
            else:
                c.deckd.hand.append(c.deckd.card_list[0])
                del c.deckd.card_list[0]
                dr += -1
                c.draw_hand(c,c.deckd)
                c.thand.border(0)
                c.win.border(0)
                c.thand.refresh()
        c.win.refresh()
        quitscr.clear()
        c.deckd.note = ""



    #Cellar
    if(c.deckd.note == "Cellar"):
        cards = 0
        while True:
            c.draw_hand(c,c.deckd)
            c.thand.border(0)
            c.win.border(0)
            c.thand.refresh()
            quitscr.clear()
            quitscr.border(0)
            quitscr.addstr(1,1,"Cycle a card(s), hit e to end.")
            quitscr.refresh()
            q = c.screen.getch()
            if len(c.deckd.hand) == 0:break
            elif q == ord('e'):quitscr.clear();break
            elif q == ord('s'):
                if len(c.deckd.hand) > c.start+5: c.start +=5
                else: c.start = 0
            elif q == ord('1'):
                if(len(c.deckd.hand) >=1):
                    cards +=1
                    del c.deckd.hand[0+c.start]
            elif q == ord('2'):
                if(len(c.deckd.hand) >=2):
                    cards +=1
                    del c.deckd.hand[1+c.start]
            elif q == ord('3'):
                if(len(c.deckd.hand) >=3):
                    cards +=1
                    del c.deckd.hand[2+c.start]
            elif q == ord('4'):
                if(len(c.deckd.hand) >=4):
                    cards +=1
                    del c.deckd.hand[3+c.start]
            elif q == ord('5'):
                if(len(c.deckd.hand) >=5):
                    cards +=1
                    del c.deckd.hand[4+c.start]
        c.deckd.draw(cards)
        quitscr.clear()
        c.deckd.note = ""



    #remodel
    if(c.deckd.note == "Remodel"):
        c.draw_hand(c,c.deckd)
        c.thand.border(0)
        c.thand.refresh()
        quitscr.clear()
        quitscr.border(0)
        quitscr.addstr(1,1,"Trash a card and upgrade up to 2 Cost?")
        quitscr.refresh()
        q = c.screen.getch()
        app_card = Card.Card()
        #lets you move through hand
        if q == ord('s'):
            if len(c.deckd.hand) > c.start+5:
                c.start +=5
            else: c.start = 0
        elif q == ord('1'):
            if(len(c.deckd.hand)>=1):
                #notes cost of card
                value = c.deckd.hand[0+c.start].cost +2
                del c.deckd.hand[0+c.start]
                c.fieldsc.border(0)
                c.draw_hand(c,c.deckd)
                c.thand.border()
                c.thand.refresh()
                quitscr.clear()
                quitscr.addstr(1,1,"You may take a card up to " + str(value) + " in cost.")
                quitscr.border(0)
                quitscr.refresh()

                while True:
                    q = c.screen.getch()
                    if q == ord('1'): c.f.buy_special(0,c.deckd,value);quitscr.clear();break
                    elif q == ord('2'): c.f.buy_special(1,c.deckd,value);quitscr.clear();break
                    elif q == ord('3'): c.f.buy_special(2,c.deckd,value);quitscr.clear();break
                    elif q == ord('4'): c.f.buy_special(3,c.deckd,value);quitscr.clear();break
                    elif q == ord('5'): c.f.buy_special(4,c.deckd,value);quitscr.clear();break
                    elif q == ord('6'): c.f.buy_special(5,c.deckd,value);quitscr.clear();break
                    elif q == ord('7'): c.f.buy_special(6,c.deckd,value);quitscr.clear();break
                    elif q == ord('8'): c.f.buy_special(7,c.deckd,value);quitscr.clear();break
                    elif q == ord('9'): c.f.buy_special(8,c.deckd,value);quitscr.clear();break
                    elif q == ord('a'): c.f.buy_special(9,c.deckd,value);quitscr.clear();break
                    elif q == ord('b'): c.f.buy_special(10,c.deckd,value);quitscr.clear();break
                    elif q == ord('c'): c.f.buy_special(11,c.deckd,value);quitscr.clear();break
                    elif q == ord('d'): c.f.buy_special(12,c.deckd,value);quitscr.clear();break
                    elif q == ord('e'): c.f.buy_special(13,c.deckd,value);quitscr.clear();break
                    else: quitscr.addstr(1,1,"Too expensive");quitscr.clear()
        elif q == ord('2'):
            if(len(c.deckd.hand)>=2):
                #notes cost of card
                value = c.deckd.hand[1+c.start].cost +2
                del c.deckd.hand[1+c.start]
                quitscr.clear()
                quitscr.addstr(1,1,"You may take a card up to " + str(value) + " in cost.")
                quitscr.border(0)
                quitscr.refresh()
                q = c.screen.getch()
                if q == ord('1'): c.f.buy_special(0,c.deckd,value);quitscr.clear()
                elif q == ord('2'): c.f.buy_special(1,c.deckd,value);quitscr.clear()
                elif q == ord('3'): c.f.buy_special(2,c.deckd,value);quitscr.clear()
                elif q == ord('4'): c.f.buy_special(3,c.deckd,value);quitscr.clear()
                elif q == ord('5'): c.f.buy_special(4,c.deckd,value);quitscr.clear()
                elif q == ord('6'): c.f.buy_special(5,c.deckd,value);quitscr.clear()
                elif q == ord('7'): c.f.buy_special(6,c.deckd,value);quitscr.clear()
                elif q == ord('8'): c.f.buy_special(7,c.deckd,value);quitscr.clear()
                elif q == ord('9'): c.f.buy_special(8,c.deckd,value);quitscr.clear()
                elif q == ord('a'): c.f.buy_special(9,c.deckd,value);quitscr.clear()
                elif q == ord('b'): c.f.buy_special(10,c.deckd,value);quitscr.clear()
                elif q == ord('c'): c.f.buy_special(11,c.deckd,value);quitscr.clear()
                elif q == ord('d'): c.f.buy_special(12,c.deckd,value);quitscr.clear()
                elif q == ord('e'): c.f.buy_special(13,c.deckd,value);quitscr.clear()
                else: quitscr.clear()
        elif q == ord('3'):
            if(len(c.deckd.hand)>=3):
                #notes cost of card
                value = c.deckd.hand[2+c.start].cost +2
                del c.deckd.hand[2+c.start]
                quitscr.clear()
                quitscr.addstr(1,1,"You may take a card up to " + str(value) + " in cost.")
                quitscr.border(0)
                quitscr.refresh()
                q = c.screen.getch()
                if q == ord('1'): c.f.buy_special(0,c.deckd,value);quitscr.clear()
                elif q == ord('2'): c.f.buy_special(1,c.deckd,value);quitscr.clear()
                elif q == ord('3'): c.f.buy_special(2,c.deckd,value);quitscr.clear()
                elif q == ord('4'): c.f.buy_special(3,c.deckd,value);quitscr.clear()
                elif q == ord('5'): c.f.buy_special(4,c.deckd,value);quitscr.clear()
                elif q == ord('6'): c.f.buy_special(5,c.deckd,value);quitscr.clear()
                elif q == ord('7'): c.f.buy_special(6,c.deckd,value);quitscr.clear()
                elif q == ord('8'): c.f.buy_special(7,c.deckd,value);quitscr.clear()
                elif q == ord('9'): c.f.buy_special(8,c.deckd,value);quitscr.clear()
                elif q == ord('a'): c.f.buy_special(9,c.deckd,value);quitscr.clear()
                elif q == ord('b'): c.f.buy_special(10,c.deckd,value);quitscr.clear()
                elif q == ord('c'): c.f.buy_special(11,c.deckd,value);quitscr.clear()
                elif q == ord('d'): c.f.buy_special(12,c.deckd,value);quitscr.clear()
                elif q == ord('e'): c.f.buy_special(13,c.deckd,value);quitscr.clear()
                else: quitscr.clear()
        elif q == ord('4'):
            if(len(c.deckd.hand)>=3):
                #notes cost of card
                value = c.deckd.hand[3+c.start].cost +2
                del c.deckd.hand[3+c.start]
                quitscr.clear()
                quitscr.addstr(1,1,"You may take a card up to " + str(value) + " in cost.")
                quitscr.border(0)
                quitscr.refresh()
                q = c.screen.getch()
                if q == ord('1'): c.f.buy_special(0,c.deckd,value);quitscr.clear()
                elif q == ord('2'): c.f.buy_special(1,c.deckd,value);quitscr.clear()
                elif q == ord('3'): c.f.buy_special(2,c.deckd,value);quitscr.clear()
                elif q == ord('4'): c.f.buy_special(3,c.deckd,value);quitscr.clear()
                elif q == ord('5'): c.f.buy_special(4,c.deckd,value);quitscr.clear()
                elif q == ord('6'): c.f.buy_special(5,c.deckd,value);quitscr.clear()
                elif q == ord('7'): c.f.buy_special(6,c.deckd,value);quitscr.clear()
                elif q == ord('8'): c.f.buy_special(7,c.deckd,value);quitscr.clear()
                elif q == ord('9'): c.f.buy_special(8,c.deckd,value);quitscr.clear()
                elif q == ord('a'): c.f.buy_special(9,c.deckd,value);quitscr.clear()
                elif q == ord('b'): c.f.buy_special(10,c.deckd,value);quitscr.clear()
                elif q == ord('c'): c.f.buy_special(11,c.deckd,value);quitscr.clear()
                elif q == ord('d'): c.f.buy_special(12,c.deckd,value);quitscr.clear()
                elif q == ord('e'): c.f.buy_special(13,c.deckd,value);quitscr.clear()
                else: quitscr.clear()
        elif q == ord('5'):
            if(len(c.deckd.hand)>=4):
                #notes cost of card
                value = c.deckd.hand[4+c.start].cost +2
                del c.deckd.hand[4+c.start]
                quitscr.clear()
                quitscr.addstr(1,1,"You may take a card up to " + str(value) + " in cost.")
                quitscr.border(0)
                quitscr.refresh()
                q = c.screen.getch()
                if q == ord('1'): c.f.buy_special(0,c.deckd,value);quitscr.clear()
                elif q == ord('2'): c.f.buy_special(1,c.deckd,value);quitscr.clear()
                elif q == ord('3'): c.f.buy_special(2,c.deckd,value);quitscr.clear()
                elif q == ord('4'): c.f.buy_special(3,c.deckd,value);quitscr.clear()
                elif q == ord('5'): c.f.buy_special(4,c.deckd,value);quitscr.clear()
                elif q == ord('6'): c.f.buy_special(5,c.deckd,value);quitscr.clear()
                elif q == ord('7'): c.f.buy_special(6,c.deckd,value);quitscr.clear()
                elif q == ord('8'): c.f.buy_special(7,c.deckd,value);quitscr.clear()
                elif q == ord('9'): c.f.buy_special(8,c.deckd,value);quitscr.clear()
                elif q == ord('a'): c.f.buy_special(9,c.deckd,value);quitscr.clear()
                elif q == ord('b'): c.f.buy_special(10,c.deckd,value);quitscr.clear()
                elif q == ord('c'): c.f.buy_special(11,c.deckd,value);quitscr.clear()
                elif q == ord('d'): c.f.buy_special(12,c.deckd,value);quitscr.clear()
                elif q == ord('e'): c.f.buy_special(13,c.deckd,value);quitscr.clear()
                else: quitscr.clear()
        c.deckd.note = ""

    #mine
    if(c.deckd.note == "Mine"):

        c.draw_hand(c,c.deckd)
        c.thand.border(0)
        c.thand.refresh()
        quitscr.clear()
        quitscr.addstr(1,1,"Trash which Treasure to Upgrade?")
        quitscr.border(0)
        quitscr.refresh()
        n = c.screen.getch()
        app_card = Card.Card()
        #lets you move through hand
        if n == ord('s'):
            if len(c.deckd.hand) > c.start+5:
                c.start +=5
            else: c.start = 0
        elif n == ord('1'):
            if(len(c.deckd.hand)>=1):
                #checks if copper or gold then upgrades
                if(c.deckd.hand[0+c.start].name == "Copper"):
                    app_card.set("Silver","+2 Gold",3)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[0+c.start]
                if(c.deckd.hand[0+c.start].name == "Silver"):
                    app_card.set("Gold","+3 Gold",6)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[0+c.start]
                quitscr.clear()
        elif n == ord('2'):
            if(len(c.deckd.hand)>=2):
                if(c.deckd.hand[1+c.start].name == "Copper"):
                    app_card.set("Silver","+2 Gold",3)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[1+c.start]
                elif(c.deckd.hand[1+c.start].name == "Silver"):
                    app_card.set("Gold","+3 Gold",6)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[1+c.start]
                quitscr.clear()
        elif n == ord('3'):
            if(len(c.deckd.hand)>=3):
                if(c.deckd.hand[2+c.start].name == "Copper"):
                    app_card.set("Silver","+2 Gold",3)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[2+c.start]
                elif(c.deckd.hand[2+c.start].name == "Silver"):
                    app_card.set("Gold","+3 Gold",6)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[2+c.start]
                quitscr.clear()
        elif n == ord('4'):
            if(len(c.deckd.hand)>=4):
                if(c.deckd.hand[3+c.start].name == "Copper"):
                    app_card.set("Silver","+2 Gold",3)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[3+c.start]
                elif(c.deckd.hand[3+c.start].name == "Silver"):
                    app_card.set("Gold","+3 Gold",6)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[3+c.start]
                quitscr.clear()
        elif n == ord('5'):
            if(len(c.deckd.hand)>=5):
                if(c.deckd.hand[4+c.start].name == "Copper"):
                    app_card.set("Silver","+2 Gold",3)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[4+c.start]
                elif(c.deckd.hand[4+c.start].name == "Silver"):
                    app_card.set("Gold","+3 Gold",6)
                    c.deckd.hand.append(app_card)
                    del c.deckd.hand[4+c.start]
                quitscr.clear()
        quitscr.clear()
        c.deckd.note = ""


    #buys cards
    elif d == ord('b'):
        quitscr = c.win.subwin(5,40,10,20)
        quitscr.clear()
        quitscr.addstr(1,1,"Which card do you want to buy?")
        quitscr.border(0)
        quitscr.refresh()
        q = c.screen.getch()
        if q == ord('1'): c.f.buy(0,c.deckd,s);quitscr.clear()
        elif q == ord('2'): c.f.buy(1,c.deckd,s);quitscr.clear()
        elif q == ord('3'): c.f.buy(2,c.deckd,s);quitscr.clear()
        elif q == ord('4'): c.f.buy(3,c.deckd,s);quitscr.clear()
        elif q == ord('5'): c.f.buy(4,c.deckd,s);quitscr.clear()
        elif q == ord('6'): c.f.buy(5,c.deckd,s);quitscr.clear()
        elif q == ord('7'): c.f.buy(6,c.deckd,s);quitscr.clear()
        elif q == ord('8'): c.f.buy(7,c.deckd,s);quitscr.clear()
        elif q == ord('9'): c.f.buy(8,c.deckd,s);quitscr.clear()
        elif q == ord('a'): c.f.buy(9,c.deckd,s);quitscr.clear()
        elif q == ord('b'): c.f.buy(10,c.deckd,s);quitscr.clear()
        elif q == ord('c'): c.f.buy(11,c.deckd,s);quitscr.clear()
        elif q == ord('d'): c.f.buy(12,c.deckd,s);quitscr.clear()
        elif q == ord('e'): c.f.buy(13,c.deckd,s);quitscr.clear()
        else: quitscr.clear()

    #quit game
    elif d == ord('q'):
        quitscr = c.win.subwin(5,40,10,20)
        quitscr.clear()
        quitscr.addstr(1,1,"Are you sure you want to quit Y/n?")
        quitscr.border(0)
        quitscr.refresh()
        c.screen.refresh()
        q = c.screen.getch()
        if q == ord('Y'):sys.exit();break
        else: quitscr.clear()


    #end turn
    elif d == ord('e'):
        quitscr = c.win.subwin(5,40,10,20)
        quitscr.clear()
        quitscr.addstr(1,1,"Are you sure you want to end your turn? Y/n")
        quitscr.border(0)
        quitscr.refresh()
        c.screen.refresh()
        q = c.screen.getch()
        if q == ord('Y'): c.start = 0;s.endturn();c.deckd.end();quitscr.clear();c.scores.clear()
        else: c.scores.clear();quitscr.clear()

    elif d == ord('s'):
        if len(c.deckd.hand) > c.start+5:
            c.start +=5
        else: c.start =0

    if(c.f.check_end()):
        quitscr = c.win.subwin(5,40,10,20)
        quitscr.addstr(1,1, "The game is over!")
        quitscr.addstr(3,1, "You got " + str(c.deckd.check_point(s)) + " points!")
