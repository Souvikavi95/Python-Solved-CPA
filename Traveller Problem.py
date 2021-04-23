class Traveler:
    def __init__(self, travelerName, traveledCountry, travelerAge, countryFrom):
        self.travelerName = travelerName
        self.traveledCountry = traveledCountry
        self.travelerAge = travelerAge
        self.countryFrom = countryFrom


class TravelAgency:
    def __init__(self, travelerList):
        self.travelerList = travelerList

    def countTravelersTraveledCountry(self, country):
        count = 0
        for t in self.travelerList:
            for c in t.traveledCountry:
                if c.lower() == country.lower():
                    count += 1
        return count

    def getTravelerTravelledMaxCountry(self):
        max_c = len(self.travelerList[0].traveledCountry)
        max_t = self.travelerList[0]
        for r in self.travelerList:
            if len(r.traveledCountry) > max_c:
                max_c = len(r.traveledCountry)
                max_t = r
        max_name = max_t.travelerName
        return max_name


if __name__ == "__main__":
    n1 = int(input())
    traveler_list = []
    for i in range(n1):
        name = input()
        n2 = int(input())
        c_list = []
        for j in range(n2):
            c_name = input()
            c_list.append(c_name)
        age = int(input())
        c_from = input()
        t_obj = Traveler(name,c_list,age,c_from)
        traveler_list.append(t_obj)
    cin = input()

    ta_obj = TravelAgency(traveler_list)
    res1 = ta_obj.countTravelersTraveledCountry(cin)
    res2 = ta_obj.getTravelerTravelledMaxCountry()
    print(res1)
    print(res2)
