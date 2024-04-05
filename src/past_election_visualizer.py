# -*- coding: windows-1250 -*-


import pandas as pd
import matplotlib.pyplot as plt

from src.past_election_loader import ElectionLoader


class ElectionVisualizer:

    def __init__(self, year: int) -> None:
        self.year = year

        self.election_loader = ElectionLoader(year)
        self.election_loader.load_candidates()

    def visualize(self) -> None:
        sorted_candidates = sorted(self.election_loader.candidates.items(), key=lambda s: s[1].votes)

        party_names = self.format_names(sorted_candidates)

        data = {
            "Party": party_names,
            "Votes": [p.votes for _, p in sorted_candidates]
        }

        df = pd.DataFrame(data)

        plt.figure(figsize=(8, 8))
        bars = plt.barh(df["Party"], df["Votes"], color="lightgreen", height=0.8)
        plt.xlabel("Party")
        plt.ylabel("Votes")
        plt.title(f"Vote Count for Parties in {self.year}")

        for i, bar in enumerate(bars):
            plt.text(2000, bar.get_y() + bar.get_height() / 2, party_names[i],
                     va='center', ha='left')

        plt.yticks([])

        plt.tight_layout()

        plt.show()

    @staticmethod
    def format_names(candidates) -> list[str]:
        names = []

        party_names = ["HDZ", "SDP", "HSLS", "HSS", "HSU", "SNAGA", "GLAS", "IDS", "PGS", "MOŽEMO!", "ZA GRAD", "NL",
                       "RF", "ORAH", "DOMOVINSKI POKRET", "BLOK", "HRVATSKI SUVERENISTI", "HKS", "HRAST", "SU", "MOST",
                       "IP", "PAMETNO", "FOKUS", "ŽIVI ZID", "PH", "A - HSP", "HSS - SR", "SIP",
                       "POKRET ZA MODERNU HRVATSKU", "BUZ", "NHR", "HSP", "GO", "HNS", "SRP", "STRANKA RADA",
                       "REFORMISTI", "HDS", "MVH", "BDSH", "HBPS", "ABECEDA", "SMS", "NLSP", "HRS"]

        for name, _ in candidates:
            parties = []
            for party in party_names:
                if " " + party in name:
                    parties.append(party)
            if parties:
                names.append(", ".join(parties))
            else:
                names.append(name)

        return names


if __name__ == "__main__":
    visualizer = ElectionVisualizer(2020)
    visualizer.visualize()
