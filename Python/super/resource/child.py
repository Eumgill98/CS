from parent import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.handicraft = 0

    def manufacture(self):
        print("제조에 성공했습니다.")
        self.handicraft += 10

class Orc(Player):
    def __init__(self, name):
        super().__init__(name)
        self.power = 0

    def greet(self): #오버 라이딩
        print("!@!$@!%!%!@%!@%!@^")

    def bust_up(self):
        print("부수기에 성공했습니다.")
        self.power += 10

class Elf(Player):
    def __init__(self, name):
        #super.__init__(name) #Super를 사용하지 않고 상속을 받았을 경우
        self.mana = 0

    def magic(self):
        print("마법에 성공했습니다")
        self.mana += 10

