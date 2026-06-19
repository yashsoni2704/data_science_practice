class Player:
    player_count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Player.player_count +=1
t1 = Player("Yash",20)
t2 = Player("Yash2",21)
print(Player.player_count)