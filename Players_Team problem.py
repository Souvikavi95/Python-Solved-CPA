class Player:
    def __init__(self, name, ctry, age, match, runs, wckts):
        self.playerName = name
        self.playerCountry = ctry
        self.playerAge = age
        self.noOfMatches = match
        self.noOfRuns = runs
        self.noOfWickets = wckts


class Team:
    def __init__(self, lp):
        self.listOfPlayers = lp

    def getMinRuns(self):
        min_run = self.listOfPlayers[0].noOfRuns
        min_p = self.listOfPlayers[0]
        for player in self.listOfPlayers:
            if player.noOfRuns < min_run:
                min_run = player.noOfRuns
                min_p = player
        return min_p

    def getMaxWickets(self):
        max_wckt = self.listOfPlayers[0].noOfWickets
        max_p = self.listOfPlayers[0]
        for p in self.listOfPlayers:
            if p.noOfWickets > max_wckt:
                max_wckt = p.noOfWickets
                max_p = p
        return max_p


if __name__ == "__main__":
    nop = int(input())
    player_list = []
    for i in range(nop):
        n = input()
        c = input()
        a = int(input())
        m = int(input())
        r = int(input())
        w = int(input())
        player_obj = Player(n, c, a, m, r, w)
        player_list.append(player_obj)

    team_obj = Team(player_list)
    res_min = team_obj.getMinRuns()
    res_max = team_obj.getMaxWickets()

    print(res_min.playerName)
    print(res_min.noOfRuns)
    print(res_min.playerCountry)
    print(res_max.playerName)
    print(res_max.noOfWickets)
    print(res_max.playerCountry)
