class Player:
    player_count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.player_count+=1
p1 = Player("Yash",22)
p2 = Player("Rohit",24)
print(p1.player_count)