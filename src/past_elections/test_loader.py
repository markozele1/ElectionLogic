# -*- coding: windows-1250 -*-

from src.past_elections.constituency_loader import ElectionLoader
from src.past_elections.party_mappings import parties_mapping


def format_name(name) -> str:
    party_names = ["HDZ", "SDP", "HSLS", "HSS", "HSU", "SNAGA", "GLAS", "IDS", "PGS", "MOŽEMO!", "ZA GRAD", "NL",
                   "RF", "ORAH", "DOMOVINSKI POKRET", "BLOK", "HRVATSKI SUVERENISTI", "HKS", "HRAST", "SU", "MOST",
                   "IP", "PAMETNO", "FOKUS", "ŽIVI ZID", "PH", "A - HSP", "HSS - SR", "SIP",
                   "POKRET ZA MODERNU HRVATSKU", "BUZ", "NHR", "HSP", "GO", "HNS", "SRP", "STRANKA RADA",
                   "REFORMISTI", "HDS", "MVH", "BDSH", "HBPS", "ABECEDA", "SMS", "NLSP", "HRS"]

    parties = [party for party in party_names if " " + party in name]
    if parties:
        name = ", ".join(parties)

    return name


constituencies = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
                  "12_13", "12_23", "12_33", "12_43", "12_53", "12_63"]

election_data = {2015: {}, 2016: {}, 2020: {}}
for year in election_data.keys():
    for c in constituencies:
        election_data[year][c] = []

        loader = ElectionLoader(year, c)
        loader.load_candidates()

        for party in sorted(loader.candidates.values(), key=lambda x: x.votes, reverse=True):
            election_data[year][c].append(party)


for year in election_data.keys():
    print("Year", year)
    print("-------------")
    for c in election_data[year].keys():
        print()
        print("\tConstituency", c)
        for party in election_data[year][c]:
            name = party.name
            if party.name in parties_mapping[year]:
                name = parties_mapping[year][party.name]
            print("\t\t-", name, " " * (40 - len(name)), party.votes)
