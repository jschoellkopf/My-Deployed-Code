players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

class Player:
    
    team = []
    
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]
        Player.team.append(self.name)
    
    @classmethod
    def get_team(cls, team_list):
        for i in range(len(team_list)):
            Player(team_list[i])
        return Player.team

player_kevin = Player(players[0])
player_jason = Player(players[1])
player_kyrie = Player(players[2])

print(player_kevin.position)
print(player_jason.age)
print(player_kyrie.team)

new_team = []
for i in range(len(players)):
    new_player = Player(players[i]) # how do i make an evolving player variable name player1 - 6
    
    new_team.append(new_player)

print(new_team)
print(Player.get_team(players))