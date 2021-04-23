class Blood:
    def __init__(self, b_grp, unit_hand):
        self.bloodGroup = b_grp
        self.unitInHand = unit_hand


class BloodBank:
    def __init__(self, bloodList):
        self.bloodList = bloodList

    def isBloodAvailable(self, blood_grp, unit_req):
        res = 0
        for packet in self.bloodList:
            if packet.bloodGroup.upper() == blood_grp.upper() and packet.unitInHand >= unit_req:
                res = 1
        if res == 1:
            return True
        else:
            return False

    def finMinBloodStock(self):
        unit_list = []
        res_list = []
        for blood in self.bloodList:
            unit_list.append(blood.unitInHand)
        min_stock = min(unit_list)
        for q in self.bloodList:
            if q.unitInHand == min_stock:
                res_list.append(q.bloodGroup)
        return res_list

if __name__ == "__main__":
    nob = int(input())
    b_l = []
    for r in range(nob):
        b_g = input()
        b_u = int(input())
        b_obj = Blood(b_g, b_u)
        b_l.append(b_obj)
    target_grp = input()
    target_unit = int(input())

    bank_obj = BloodBank(b_l)
    res1 = bank_obj.isBloodAvailable(target_grp, target_unit)
    res2 = bank_obj.finMinBloodStock()

    if (res1 == True):
        print("Blood Available")
    else:
        print("Blood not Available")
    for item in res2:
        print(item)
