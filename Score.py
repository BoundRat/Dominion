__author__ = 'bommaritoe16'


class Score():
    gold = 0
    actions = 1
    buys = 1
    score = 0

    def __init__(self): pass

    def Goldsc(self):
        return self.gold

    def Actionsc(self):
        return self.actions

    def set(self,Gold,Actions):
        self.gold = Gold
        self.actions = Actions

    def endturn(self):
        self.gold = 0
        self.actions = 1
        self.buys = 1

