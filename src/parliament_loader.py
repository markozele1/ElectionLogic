import csv


with open("HR-parliament.json", "r") as file:
    parilament_data = eval(file.read())

trends = parilament_data["trends"]["kalmanSmooth"]

party_names = set()
for item in trends:
    for party_name in item['parties']:
        party_names.add(party_name)

# Write data to CSV-2007 file
csv_file_path = "poll_data.csv"
with open(csv_file_path, "w", newline='') as csvfile:
    fieldnames = ["date"] + list(party_names)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header row
    writer.writeheader()

    # Write data rows
    for item in trends:
        row_data = {"date": item["date"]}
        row_data.update(item["parties"])
        writer.writerow(row_data)

# Read data from CSV-2007 file
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Extract party names from header row
    party_names = reader.fieldnames[1:]

    # Print header row
    print("Date\t", "\t".join(party_names))

    # Print data rows
    for row in reader:
        date = row['date']
        votes = {party: row[party] for party in party_names}
        print(date, votes)
