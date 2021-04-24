class Player:
    def __init__(self, p_name, p_ctry, p_age, ctry_frm):
        self.playerName = p_name
        self.playedCountry = p_ctry  # list of countries played for
        self.playerAge = p_age
        self.countryFrom = ctry_frm


def countPlayers(player_list, ctry_name):
    count = 0
    for player in player_list:
        if player.countryFrom.lower() == ctry_name.lower():
            count += 1
    return count


def getPlayerPlayedForMaxCountry(p_list):
    max_p = len(p_list[0].playedCountry)
    max_p_name = p_list[0].playerName
    for player in p_list:
        if len(player.playedCountry) > max_p:
            max_p = len(player.playedCountry)
            max_p_name = player.playerName
    return max_p_name


if __name__ == "__main__":
    nop = int(input())
    player_obj_list = []
    for q in range(nop):
        player_name = input()
        noc = int(input())
        c_list = []
        for r in range(noc):
            t = input()
            c_list.append(t)
        player_age = int(input())
        player_c = input()
        player_obj = Player(player_name, c_list, player_age, player_c)
        player_obj_list.append(player_obj)

    target_c = input()
    # END OF INPUT

    # PRINTING RESULTS
    res1 = countPlayers(player_obj_list, target_c)
    res2 = getPlayerPlayedForMaxCountry(player_obj_list)
    print(res1)
    print(res2)
