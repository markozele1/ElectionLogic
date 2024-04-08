# -*- coding: windows-1250 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

from src.past_elections.constituency_loader import ElectionLoader
from src.past_elections.party_mappings import parties_mapping, get_full_name


def dhondt_method(n_seats, parties):
    t_votes = parties.copy()
    seats = {key: 0 for key in parties}
    while sum(seats.values()) < n_seats:
        max_v = max(t_votes.values())
        next_seat = list(t_votes.keys())[list(t_votes.values()).index(max_v)]
        if next_seat in seats:
            seats[next_seat] += 1
        else:
            seats[next_seat] = 1
        t_votes[next_seat] = parties[next_seat] / (seats[next_seat] + 1)
    return seats


def format_name(name) -> str:
    party_names = ["HDZ", "SDP", "HSLS", "HSS", "HSU", "SNAGA", "GLAS", "IDS", "PGS", "MO?EMO!", "ZA GRAD", "NL",
                   "RF", "ORAH", "DOMOVINSKI POKRET", "BLOK", "HRVATSKI SUVERENISTI", "HKS", "HRAST", "SU", "MOST",
                   "IP", "PAMETNO", "FOKUS", "?IVI ZID", "PH", "A - HSP", "HSS - SR", "SIP",
                   "POKRET ZA MODERNU HRVATSKU", "BUZ", "NHR", "HSP", "GO", "HNS", "SRP", "STRANKA RADA",
                   "REFORMISTI", "HDS", "MVH", "BDSH", "HBPS", "ABECEDA", "SMS", "NLSP", "HRS"]

    parties = [party for party in party_names if " " + party in name]
    if parties:
        name = ", ".join(parties)

    return name


def predict_next_point(inpt_years, inpt_percentages):
    years = np.array(inpt_years).reshape(-1, 1)  # Reshaping to column vector
    percentages = np.array(inpt_percentages).reshape(-1, 1)  # Percentages of votes for each election year

    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(years, percentages)

    # Predict the outcome for the 2024 election
    predicted_year = np.array([[2021]])  # Reshaping to column vector
    predicted_percentage = model.predict(predicted_year)[0][0]
    if predicted_percentage < 0:
        predicted_percentage = 0

    return inpt_years + [2024], inpt_percentages + [predicted_percentage]


def get_constituency_past_data(constituency):
    return {
        year: {party.name: party.votes for party in election_data[year][constituency]}
        for year in election_data.keys()
    }


def get_constituency_party_votes_and_percentages(constituency):
    d = get_constituency_past_data(constituency)

    data = {}
    for year in d.keys():
        data[year] = {}
        for party in d[year].keys():
            name = party
            if name in parties_mapping[year]:
                name = parties_mapping[year][name]
            data[year][name] = d[year][party]

    years = list(data.keys())
    parties = set()
    for y in years:
        for p in data[y].keys():
            if p in parties_mapping[y]:
                p = parties_mapping[y][p]
            parties.add(p)

    num_votes = {y: 0 for y in years}
    party_votes = {}
    for party in parties:
        name = party
        party_votes[name] = []
        for year in years:
            if party in data[year]:
                if name in parties_mapping[year]:
                    name = parties_mapping[year][party]
                if name not in party_votes:
                    party_votes[name] = []
                party_votes[name].append(data[year][party])
                num_votes[year] += data[year][party]
            else:
                party_votes[name].append(0)

    party_percentages = {}
    for party in parties:
        name = party
        party_percentages[name] = []
        for year in years:
            if party in data[year]:
                if name in parties_mapping[year]:
                    name = parties_mapping[year][party]
                if name not in party_votes:
                    party_percentages[name] = []
                party_percentages[name].append(data[year][party] / num_votes[year])
            else:
                party_percentages[name].append(0)

    return years, party_votes, party_percentages


def show_constituency_past_data(constituency):
    years, party_votes, party_percentages = get_constituency_party_votes_and_percentages(constituency)

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.4)
    plt.xticks(list(range(2007, 2025, 2)))

    # Plot each party's votes over the years
    for party, votes in party_votes.items():
        axs[0].plot(years, votes, label=party)
        if max(votes) > 15000 and len(party) < 20:
            x = years[votes.index(max(votes))]
            if votes.index(max(votes)) == 4:
                x -= 3
            axs[0].text(x, max(votes), party, ha='left', va='center', fontsize=9, color='black')

    # Customize the graph
    axs[0].set_xlabel('Godina izbora')
    axs[0].set_ylabel('Ukupni glasovi stranke')
    axs[0].set_title('Izborna Jedinica ' + constituency)
    # plt.legend()

    # Show the plot
    axs[0].grid(True)

    new_party_percentages = {}

    # Plot each party's votes over the years
    for party, percentages in party_percentages.items():
        percentages = [(p * 100 if str(p) != "nan" else 0) for p in percentages]
        years2, percentages = predict_next_point(years, percentages)
        new_party_percentages[party] = percentages[-1]
        axs[1].plot(years2, percentages, label=party)
        if max(percentages) > 8 and len(party) < 20:
            axs[1].text(years2[percentages.index(max(percentages))], max(percentages), party, ha='left', va='center', fontsize=9, color='black')

    # Customize the graph
    axs[1].set_xlabel('Godina izbora')
    axs[1].set_ylabel('Postotak glasova stranke (%)')
    axs[1].set_title('Izborna Jedinica ' + constituency)
    # plt.legend()

    # Show the plot
    axs[1].grid(True)

    plt.show()


def predict_new_elections(constituency):
    years, party_votes, party_percentages = get_constituency_party_votes_and_percentages(constituency)
    new_party_percentages = {}

    for party, percentages in party_percentages.items():
        percentages = [(p * 100 if str(p) != "nan" else 0) for p in percentages]
        years2, percentages = predict_next_point(years, percentages)
        new_party_percentages[party] = percentages[-1]

    return new_party_percentages


def show_election_results():
    years = list(election_data.keys())

    uk = {year: {} for year in years}
    for year in years:
        for c in constituencies:
            if c == "11":
                break

            parties2 = {}
            for party in election_data[year][c]:
                name = party.name
                if party.name in parties_mapping[year]:
                    name = parties_mapping[year][party.name]
                parties2[name] = party.votes
                if year in {2007, 2011}:
                    if str(party.votes) == "nan":
                        parties2[name] = 0
                    else:
                        parties2[name] = int(str(party.votes).replace(".", ""))

            seats = {k: v for k, v in dhondt_method(14, parties2).items() if v}

            for party, seat in seats.items():
                if seat > 0:
                    if party in uk[year]:
                        uk[year][party] += seat
                    else:
                        uk[year][party] = seat

    uk[2024] = {}
    for c in constituencies:
        if c == "11": break

        predicted = predict_new_elections(c)

        seats = {k: v for k, v in dhondt_method(14, predicted).items() if v}

        for party, seat in seats.items():
            if party in uk[2024]:
                uk[2024][party] += seat
            else:
                uk[2024][party] = seat

    years.append(2024)

    all_party_names = set(party for year_data in uk.values() for party in year_data.keys())
    party_seat_counts = {party: [0] * len(years) for party in all_party_names}

    for year in years:
        year_data = uk[year]
        for party, seats in year_data.items():
            party_seat_counts[party][years.index(year)] = seats

    fig, ax = plt.subplots()
    plt.xticks(list(range(2007, 2025, 2)))

    for party, seats in party_seat_counts.items():
        if party == "HDZ":
            ax.plot(years, seats, label=party, color="blue")
        elif party == "SDP":
            ax.plot(years, seats, label=party, color="red")
        else:
            ax.plot(years, seats, label=party)
        y = max(seats)
        x = years[seats.index(max(seats))]
        if party == "HDSSB":
            y -= 3
        if party == "HSS":
            y -= 3
            x += 1
        if max(seats) > 2:
            ax.text(x, y, party)

    # Set labels and title
    ax.set_xlabel('Godina')
    ax.set_ylabel('Broj mandata')
    ax.set_title('Broj mandata svih stranaka od 2007.')

    # Add legend
    # ax.legend()

    # Show the plot
    plt.show()


constituencies = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
                  "12_13", "12_23", "12_33", "12_43", "12_53", "12_63"]

election_data = {2007: {}, 2011: {}, 2015: {}, 2016: {}, 2020: {}}
for year in election_data.keys():
    for c in constituencies:
        election_data[year][c] = []

        loader = ElectionLoader(year, c)
        loader.load_candidates()

        for party in sorted(loader.candidates.values(), key=lambda x: x.votes, reverse=True):
            if str(party.votes) == "nan":
                party.votes = 0
            election_data[year][c].append(party)


# for year in election_data.keys():
#     print("Year", year)
#     print("-------------")
#     dhondt = {}
#     for c in election_data[year].keys():
#         if c == "11":
#             break
#         print()
#         print("\tConstituency", c)
#         parties2 = {}
#         for party in election_data[year][c]:
#             name = party.name
#             if party.name in parties_mapping[year]:
#                 name = parties_mapping[year][party.name]
#             parties2[name] = party.votes
#             if year in {2007, 2011}:
#                 if str(party.votes) == "nan":
#                     parties2[name] = 0
#                 else:
#                     parties2[name] = int(str(party.votes).replace(".", ""))
#             print("\t\t-", name, " " * (40 - len(name)), party.votes)
#         d = {k: v for k, v in dhondt_method(14, parties2).items() if v}.items()
#         for k, v in d:
#             if k in dhondt:
#                 dhondt[k] += v
#             else:
#                 dhondt[k] = v
#     print()
#     print("D'HONDT: ", dhondt)
#     print()


uk = {}
for c in constituencies:
    if c == "11":
        break
    p = predict_new_elections(c)
    seats = dhondt_method(14, p)
    print()
    print("Constituency", c)
    for party, seat in seats.items():
        if seat > 0:
            print(party, " - ", seat)
            if party in uk:
                uk[party] += seat
            else:
                uk[party] = seat

print(uk)

show_election_results()
