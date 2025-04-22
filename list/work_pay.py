work_hours = [int(x) for x in input("enter work done in day with space").split()]
print(work_hours)
hour_pay = 70
Total_work = 0

for i in range( len(work_hours)):
    Total_work = Total_work + work_hours[i]
total_pay = Total_work * hour_pay
print(total_pay)

print(" ------------------- ")

Total = sum(work_hours)

total_pays = Total*hour_pay
print(total_pays)