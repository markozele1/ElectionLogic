import pandas as pd

from src.past_elections.main import dhondt_method

with open("poll_data2024.txt", "r", encoding="windows-1250") as file:
    text = file.read().split("\n")

    constituencies = {}
    cur_const = ""
    for line in text:
        if not line: continue
        if len(line) <= 4:
            constituencies[line] = {}
            cur_const = line
        else:
            party, prediction = line.split(" ")
            constituencies[cur_const][party] = float(prediction)

df = pd.read_excel("party_errors.xlsx")
rows = list(df["STRANKA"])

party_percentages = {c: {} for c in constituencies}
party_seats = {c: {} for c in constituencies}
uk = {}
for c in constituencies:
    print()
    print("Izborna jedinica", c)
    indexes = list(df[c])
    for party, percentage in constituencies[c].items():
        if party in rows and indexes[rows.index(party)] != float("nan"):
            percentage *= indexes[rows.index(party)]
        party_percentages[c][party] = percentage

    party_seats[c] = {k: v for k, v in dhondt_method(14, party_percentages[c]).items() if v}

    for party in party_seats[c]:
        if party not in uk:
            uk[party] = 0
        uk[party] += party_seats[c][party]

    print("P%:", party_percentages[c])
    print("SEATS:", party_seats[c])

print()
print("UK: ", uk)
