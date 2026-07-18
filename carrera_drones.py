drons = {}
winner = []
temporary_km = {}

n = int(input())
for i in range (0,n):
    dron, km = input().split()
    km = int(km)
    drons[dron] = drons.get(dron, 0) + km

    record.append([dron,km])

highest = max(drons.values())

for dron, km in drons.items():
    if km == highest:
        winner.append(dron)

for dron, km in record:
    temporary_km[dron] = temporary_km.get(dron,0) + km

    if dron in winner and temporary_km[dron] >= 100:
        print(dron)
        break
