class Hero:
    def __init__(self, userID='', name='', HP=10, STR = 1, DEX = 1, SPD = 1, MPE = 1, HIT = 5):
        #User's Discord ID
        self.userID = userID
        #Discord#0000 set
        self.name = name
        #Player's Total Flat Hitpoints
        self.HP = HP
        #Player's Total Flat Strength Stat
        self.STR = STR
        #Player's Total Flat Dexterity Stat
        self.DEX = DEX
        #Player's Total Flat Speed Stat
        self.SPD = SPD
        #Player's Total Flat 'Magic Power Effectiveness'
        self.MPE = MPE
        #Player's Hit Percentage
        self.HIT = HIT