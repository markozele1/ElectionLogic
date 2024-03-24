#MAKNUTI REZULTATE IZBORA ODAVDE 664, 970, 2356
import csv
from datetime import datetime

def distance(date, earliest_date='2014/01/12'):
    earliest = datetime.strptime(earliest_date, '%Y/%m/%d')
    date_time = datetime.strptime(date, '%Y/%m/%d')
    distance = (date_time - earliest)
    return distance.days

F = []
with open('all.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        F.append(row)

C = [row[0] for row in F]
L = [['nan'] * 20 for _ in range(292)]
N = []

for i in range(len(C)):
    d = distance(C[i])
    L[i][0] = d
    N.append(d)

def closest(target, numbers=N):
    closest_index = 0
    min_difference = abs(numbers[0] - target)

    for i in range(1, len(numbers)):
        difference = abs(numbers[i] - target)
        if difference < min_difference:
            min_difference = difference
            closest_index = i

    return closest_index

for i in range(len(F)):
    for j in range(len(F[i])):
        if j == 0:
            continue
        elif j == 1:
            L[i][1] = F[i][j]
        elif F[i][j] != '':
            if j%2 == 0:
                index = closest(distance(F[i][j]))
            elif j%2 != 0:
                if L[index][j//2+1] == 'nan':
                    L[index][j//2+1] = F[i][j]
                else:
                    if index == 291:
                        L[index][j//2+1] = F[i][j]
                    else:
                        L[index+1][j//2+1] = F[i][j]

with open('final_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in L:
        writer.writerow(row)
