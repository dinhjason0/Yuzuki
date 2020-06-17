class Item(object):
    def __init__(self, name='', dmgtype='', dmgrange=[1,5], abilitya='', abilityb='', gear_pos=[0,0,0,0,0,0,0,0,0,0]):
        #Item name
        self.name = name
        #dmgtype
        self.dmgtype = dmgtype
        #dmgrange
        self.dmgrange = dmgrange
        #ability A
        self.abilitya = abilitya
        #ability B
        self.abilityb = abilityb
        #gear_pos
        self.gear_pos = gear_pos