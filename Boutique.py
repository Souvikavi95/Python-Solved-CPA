class Boutique:
    def __init__(self, id, name, type, rating, points):
        self.boutiqueId = id
        self.boutiqueName = name
        self.boutiqueType = type
        self.boutiqueRating = rating
        self.points = points


class OnlineBoutique:
    def __init__(self, b_dict):
        self.boutiqueDict = b_dict  # b_dict is a dictionary

    def getBoutique(self, low_l, up_l, ex_p, t):
        c_list = []
        for a, b in self.boutiqueDict.items():
            if a.lower() == t.lower():
                for c in b:
                    if low_l <= c.boutiqueRating <= up_l:
                        c.points += ex_p
                        c_list.append(c)
        c_sorted = sorted(c_list, key=lambda x: x.boutiqueRating, reverse=True)
        if len(c_sorted) == 0:
            return None
        else:
            return c_sorted


if __name__ == "__main__":
    nob = int(input())
    bt_dict = {}
    for bt in range(nob):
        temp_list = []
        b_id = int(input())
        b_name = input()
        b_type = input()
        b_rate = float(input())
        b_points = int(input())
        b_obj = Boutique(b_id, b_name, b_type, b_rate, b_points)
        if b_type in bt_dict.keys():
            bt_dict[b_type].append(b_obj)
        else:
            bt_dict[b_type] = [b_obj]
    lr = float(input())
    ur = float(input())
    pt = int(input())
    ct = input()
    online_b = OnlineBoutique(bt_dict)
    res = online_b.getBoutique(lr, ur, pt, ct)
    if res is None:
        print("No boutique found")
    else:
        for li in res:
            print(f"{li.boutiqueId} {li.boutiqueName} {li.points}")
