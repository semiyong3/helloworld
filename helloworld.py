class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{0} 유닛이 생성됐다".format(self.name))
        print("체력 {0}".format(self.hp))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
        .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 이다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됨".format(self.name))
        
        
marine1 = AttackUnit("마린", 40, 30)
marine1.damaged(25)
marine1.damaged(25)