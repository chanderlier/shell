#!/usr/bin/python3
from  abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        self._name = name
        self._hp   = hp

    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self,other):
        pass

class Ultraman(Fighter):
    __slots__ = ('_name','_hp','_mp')

    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp 

    def attack(self,other):
        other.hp -= randint(15,25)

    def huge_attack(self,other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp *3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10 ,15)
            return True
        else:
            return False
    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point
    def __str__(self):
        return '~~~%s Ultraman~~~\n' % self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)
    def __str__(self):
        return '~~~%s little monster~~~\n' % self._name + '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman,monsters):
    print(ultraman)
    for monster in monsters:
        print(monster,end= '')


def main():
    u = Ultraman('refrain',1000,200)
    m1 = Monster('longtaoA', 250)
    m2 = Monster('longtaoB', 550)
    m3 = Monster('longtaoC', 850)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('==========the %02d round =======' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1,10)
        if skill <= 6:
            print('%s use normal attack %s.' % (u.name, m.name))
            u.attack(m)
            print('%s magic power resume %d.' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s use magic attack.' % u.name)
            else:
                print('%s failed to use magic attack.' % u.name)
        else:
            if u.huge_attack(m):
                print('%s use ultra attack %s.' % (u.name, m.name))
            else:
                print('%s use normal  attack %s.' % (u.name, m.name))
                print('%s magic power resume  %s.' % (u.name, u.resume()))
        if m.alive > 0:
            print('%s attack back %s.' % (m.name, u.name))
        display_info(u, ms)
        fight_round += 1 
    print('\n========the battle end=======\n')
    if u.alive > 0:
        print('%s Ultraman win' % u.name)
    else:
        print('monster win')
if __name__ == '__main__':
    main()
        
 
