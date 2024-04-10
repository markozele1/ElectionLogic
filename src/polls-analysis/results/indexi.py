import csv

def prediction(p0, p4, r):
    a = p0/r
    p = p4/a
    return p

with open('2020_rez5.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Skip the header row
    next(reader)
    
    data = []
    for row in reader:
        data.append(row)

final = []

for i in range(len(data)):
    stranka = []
    for j in range(len(data[i])):
        if j == 0 or j >= 11:
            continue
        stranka.append(prediction(float(data[i][-2]),float(data[i][-1]),float(data[i][j])))
    final.append(stranka)
    
with open('polls-analysis.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in final:
        writer.writerow(row)
