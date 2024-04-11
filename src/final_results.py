import pandas

from src.past_elections.main import dhondt_method

with open("polls-analysis/results/2020_rez5.csv", "r", encoding="windows-1250") as file:
    text = file.read()
    rows = text.split("\n")[1:]

    parties_global_prediction = {}
    for row in rows:
        data = row.split(",")
        parties_global_prediction[data[0]] = float(data[-1])


df = pandas.read_csv("past_elections/2020_prediction_errors.csv", encoding="windows-1250")

constituencies = [f"0{i}" for i in range(1, 10)] + ["10"]

parties_past_elections_prediction = {c: {} for c in constituencies}
for row in df.values.tolist():
    for j, c in enumerate(constituencies):
        if row[0] == "DOMOVINSKI POKRET":
            row[0] = "DP"
        if row[j+23] != float("nan") and float(row[j+23]) > 4:
            parties_past_elections_prediction[c][row[0]] = float(row[j+23])


df = pandas.read_csv("poll_data2024.csv", encoding="windows-1250")

parties_polls_prediction = {c: {} for c in constituencies}
for row in df.values.tolist():
    for j, c in enumerate(constituencies):
        if row[j+1] != float("nan") and row[j+1] > 2:
            if row[0] == "DOMOVINSKI POKRET":
                row[0] = "DP"
            parties_polls_prediction[c][row[0]] = float(row[j+1])

print("GLOBAL PREDICTION")
print(parties_global_prediction)
print()
print("PAST ELECTIONS PREDICTION")
for c in constituencies:
    print(c, parties_past_elections_prediction[c])
print()
print("POLL DATA PREDICTION")
for c in constituencies:
    print(c, parties_polls_prediction[c])

print()
parties_uk_prediction = {c: {} for c in constituencies}
uk_seats = {}
for c in constituencies:
    for party in set(list(parties_past_elections_prediction[c].keys()) + list(parties_polls_prediction[c].keys()) + list(parties_global_prediction.keys())):
        if party not in parties_uk_prediction[c]:
            parties_uk_prediction[c][party] = 0
        num = 0
        if party in parties_past_elections_prediction[c]:
            num += 1
            parties_uk_prediction[c][party] += parties_past_elections_prediction[c][party]
        if party in parties_polls_prediction[c]:
            num += 1
            parties_uk_prediction[c][party] += parties_polls_prediction[c][party]
        if party in parties_global_prediction:
            num += 1
            parties_uk_prediction[c][party] += parties_global_prediction[party]
        parties_uk_prediction[c][party] /= num

    dhondt = {k: v for k, v in dhondt_method(14, parties_uk_prediction[c]).items() if v}
    print(c, "P%", parties_uk_prediction[c])
    print(c, "SEATS", dhondt)
    for party in dhondt:
        if party not in uk_seats:
            uk_seats[party] = 0
        uk_seats[party] += dhondt[party]

print("\nUK SEATS")
print(uk_seats)
