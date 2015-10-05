__author__ = 'bommaritoe16'
import Score

class Card():
    text = ""
    name = ""
    cost = 0

    def __init__(self):
        self.text = "used"
        self.name = "used"

    def set(self,name,text,cost):
        self.text = text
        self.name = name
        self.cost = cost