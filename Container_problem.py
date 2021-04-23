class Container:
    def __init__(self, iid, l, b, h, price):
        self.iid = iid
        self.length = l
        self.breadth = b
        self.height = h
        self.pricePerSqrFt = price

    def findVolume(self):
        volume = (self.length * self.breadth * self.height)
        return volume


class PackagingCompany:
    def __init__(self, listOfContainers):
        self.listOfContainers = listOfContainers

    def findContainerCost(self, container_id):
        for c in self.listOfContainers:
            if c.iid == container_id:
                c_vol = c.findVolume()
                total_cost = c_vol * c.pricePerSqrFt
                return total_cost
        return None

    def findLargestContainer(self):
        vol_list = []
        for p in self.listOfContainers:
            p_vol = p.findVolume()
            vol_list.append(p_vol)
        max_pos = vol_list.index(max(vol_list))
        max_cont = self.listOfContainers[max_pos]
        return max_cont

if __name__ == "__main__":
    noc = int(input())
    container_list = []
    for cont in range(noc):
        i = int(input())
        l = int(input())
        b = int(input())
        h = int(input())
        ps = int(input())
        c_obj = Container(i, l, b, h, ps)
        container_list.append(c_obj)
    target_con = int(input())
    pc_obj = PackagingCompany(container_list)
    res1 = pc_obj.findContainerCost(target_con)
    res2 = pc_obj.findLargestContainer()

    if res1 is None:
        print("No Container Found")
    else:
        print(res1)
    print(res2.iid, end=" ")
    print(res2.findVolume())
