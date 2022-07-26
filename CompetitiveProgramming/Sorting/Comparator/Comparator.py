#https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

#https://medium.com/voice-of-code/sorting-comparator-21d98c192bbb

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score        
    def __repr__(self):
        return {'name':self.name,'score':self.score}
        
    def comparator(a, b):
        if a.score>b.score:
            return -1
        if a.score<b.score:
            return 1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)