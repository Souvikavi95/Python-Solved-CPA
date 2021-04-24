class Employee:
    def __init__(self, employeeId, employeeName, department, salary, role):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.department = department
        self.salary = salary
        self.role = role

    def calculateIncentive(self, roleIncentivePercentage):  # a dict is passed
        for k, v in roleIncentivePercentage.items():
            if k.lower() == self.role.lower():
                incentive = self.salary * (v / 100)
                return incentive
        return None


def calculateEmployeeSalaryByRole(r, e_list, i_dict):
    res_list = []
    for p in e_list:
        if r.lower() == p.role.lower():
            increment = Employee.calculateIncentive(p, i_dict)
            p.salary += increment
            res_list.append(p)
    if len(res_list) == 0:
        return None
    else:
        return  res_list


if __name__ == "__main__":
    nor = int(input())
    role_d = {}
    for i in range(nor):
        r_name = input()
        r_inc = int(input())
        role_d[r_name] = r_inc
    noe = int(input())
    em_list = []
    for s in range(noe):
        e_id = int(input())
        e_name = input()
        e_dep = input()
        e_sal = int(input())
        e_role = input()
        e_obj = Employee(e_id, e_name, e_dep, e_sal, e_role)
        em_list.append(e_obj)
    target_role = input()
    res1 = em_list[0].calculateIncentive(role_d)
    if res1 is None:
        print("Employee Not Found")
    else:
        print(res1)
    res2 = calculateEmployeeSalaryByRole(target_role,em_list,role_d)
    if res2 is None:
        print("Employee Not Found")
    else:
        for x in res2:
            print(f"{x.employeeId} {x.employeeName} {x.salary}")

