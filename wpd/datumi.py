import csv
from datetime import datetime, timedelta

#doc = []
#column_values = []
#with open('final_work_data.csv', 'r', newline='') as csvfile:
#        reader = csv.reader(csvfile)
#        for row in reader:
#            doc.append(row)
#            # Check if row has enough elements
#            if len(row) > 0:
#                column_values.append(row[0])
#
#ankete = []
#with open('ankete-bez-datuma.csv', 'r', newline='') as csvfile:
#        reader = csv.reader(csvfile, delimiter=';')
#        for row in reader:
#            ankete.append(row)
#
#for i in range (len(ankete)):
#    ankete[i].insert(0,column_values[i])
#
#with open('ankete_s_datumom.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    for row in ankete:
#        writer.writerow(row)

################################################################################

izbori = []
with open('final_work_izbori.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            izbori.append(row)

for i in range(len(izbori)):
    for j in range(len(izbori[i])):
        if izbori[i][j] == 'nan':
            izbori[i][j] = 0

with open('izbori_s_datumom.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in izbori:
        writer.writerow(row)
