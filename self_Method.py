# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
#마린 1
#마린 2
#탱크 등의 유닛 생성

#레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wrait1 = Unit("레이스",80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wrait1.name, wrait1.damage))

#마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wrait2 = Unit("빼앗은 레이스", 80, 5)
wrait2.clocking = True

if wrait2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wrait2.name))

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}".format(self.name, location, self.damege))

    def damage(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))

        self.hp =- damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
