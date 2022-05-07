# Expresso Problem ICPC 2022
first_line = [int(num) for num in input().split(" ")]
students = first_line[0]
ounces = first_line[1]
refill = 0
for _ in range(students):
    order = input()
    curr = 0
    if order.__contains__("L"):
        curr = int(order[0]) + 1
    else:
        curr = int(order)
    if ounces - curr < 0:
        refill += 1
        ounces = first_line[1]
        ounces -= curr
    else:
        ounces -= curr
print(refill)