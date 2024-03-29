import csv
from datetime import datetime, timedelta

def get_dates(distances):
    # Start date (12 January 2014)
    start_date = datetime(2014, 1, 12)
    
    # List to store the dates
    dates = []
    
    # Iterate through the distances and calculate the corresponding dates
    for distance in distances:
        # Calculate the date by adding the distance (in days) to the start date
        date = start_date + timedelta(days=distance)
        # Append the calculated date to the list of dates
        dates.append(date.strftime('%Y-%m-%d'))  # Convert date to string in 'YYYY-MM-DD' format
        
    return dates

doc = []
column_values = []
with open('work_izbori.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            doc.append(row)
            # Check if row has enough elements
            if len(row) > 0 and row[0] != '':
                column_values.append(int(row[0]))

dates = get_dates(column_values)

for i in range (len(doc)):
    if i == 0:
        continue
    else:
        doc[i][0] = dates[i-1]

with open('final_work_izbori.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in doc:
        writer.writerow(row)
