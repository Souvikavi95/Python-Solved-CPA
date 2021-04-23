class Table:
    def __init__(self, tableNo, waiterName, status):
        self.tableNo = tableNo
        self.waiterName = waiterName
        self.status = status

    def findWaiterWiseTotalNoOfTables(list_of_table_obj):
        res_dict = {}
        for i in list_of_table_obj:
            res_dict[i.waiterName] = 0
        for j in list_of_table_obj:
            res_dict[j.waiterName] += 1
        return res_dict

    def findWaiterNameByTableNo(list_of_table_obj, table_no):
        for l in list_of_table_obj:
            if l.tableNo == table_no:
                table_waiter = l.waiterName
                return table_waiter
        else:
            return None


if __name__ == "__main__":
    nt = int(input())
    table_list = []
    for t in range(nt):
        t_no = int(input())
        w_name = input()
        st = input()
        t_obj = Table(t_no, w_name, st)
        table_list.append(t_obj)
    target_t_no = int(input())

    res1 = Table.findWaiterWiseTotalNoOfTables(table_list)
    res2 = Table.findWaiterNameByTableNo(table_list, target_t_no)

    # sorted_keys = list(reversed(list((res1.keys()))))
    final_list = []
    for k in list(res1.keys()):
        final_list.append(k + '-' + str(res1[k]))
    final_list.sort()
    for n in final_list:
        print(n)
    if res2 is None:
        print("No Table Found")
    else:
        print(res2)
