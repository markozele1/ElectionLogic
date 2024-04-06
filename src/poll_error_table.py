# -*- coding: windows-1250 -*-

import openpyxl


def create_blank_excel(constituencies, parties):
    # Create a new blank Excel workbook
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Column names (constituencies)
    for col, constituency in enumerate(constituencies, start=2):
        sheet.cell(row=1, column=col, value=constituency)

    # Row names (political parties)
    for row, party in enumerate(parties, start=2):
        sheet.cell(row=row, column=1, value=party)

    return wb, sheet


def populate_party_votes(workbook, sheet, party_votes):
    for row, party in enumerate(party_votes, start=2):
        for col, votes in enumerate(party_votes[party], start=2):
            sheet.cell(row=row, column=col, value=votes)
    workbook.save("party_errors.xlsx")


constituencies_names = [str(i) + ". izborna jedinica" for i in range(1, 11)]
parties = ["HDZ", "RESTART", "MOŽEMO", "MOST", "DP"]

with open("poll_errors.txt", "r") as file:
    text = file.read().split("\n")

    constituencies = {}
    cur_const = ""
    for line in text:
        if not line: continue
        if len(line) <= 4:
            constituencies[line] = []
            cur_const = line
        else:
            line2 = line.split(" ")
            party = line2[0]
            predicted, actual = line2[1].split(",")
            constituencies[cur_const].append((party, predicted, actual))

party_errors = {party: [] for party in parties}
for party in parties:
    for c in constituencies.keys():
        for p in constituencies[c]:
            if p[0] == party:
                party_errors[party].append(float(p[2]) / float(p[1]))

# Create blank Excel file and populate with party votes
workbook, sheet = create_blank_excel(constituencies, parties)
populate_party_votes(workbook, sheet, party_errors)
