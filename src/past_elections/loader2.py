# -*- coding: windows-1250 -*-

import os
from dataclasses import dataclass
from typing import Tuple

import pandas as pd


PROJECT_PATH = os.path.abspath(__file__).split("src")[0]


@dataclass(repr=True)
class Candidate:

    name: str
    votes: int


@dataclass(repr=True)
class Party:

    name: str
    candidates: list[Candidate]
    votes: int = 0

    def add_candidate(self, candidate: Candidate) -> None:
        self.candidates.append(candidate)


class ElectionLoader:

    def __init__(self, year: int, constituency: str) -> None:
        assert os.path.exists(os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}")),\
            f"Couldn't locate folder with election data from {year}"

        self.year = year

        names = {"01": "I", "02": "II", "03": "III", "04": "IV", "05": "V", "06": "VI", "07": "VII", "08": "VIII", "09": "IX", "10": "X", "11": "XI"}

        # učitavanje csv fileova
        csv_file_name = ""
        if year in {2007, 2011}:
            if "12" in constituency:
                csv_file_name = "12_XII_" + f"nm{constituency[3]}"
            else:
                csv_file_name = constituency + "_" + names[constituency]
            csv_file_name += "_izborna_jedinica_REDOVITA_BM.csv"
            self.df = pd.read_csv(os.path.join(PROJECT_PATH, f"past_elections\CSV-{year}\{csv_file_name}"), encoding="windows-1250", sep=";")
        else:
            csv_regular_results, csv_special_results, csv_abroad_results = self.load_constituency_files(year, constituency)

            self.df_regular = pd.read_csv(csv_regular_results, encoding="windows-1250", sep=";")
            self.df_special = pd.read_csv(csv_special_results, encoding="windows-1250", sep=";")
            try:
                self.df_abroad = pd.read_csv(csv_abroad_results, encoding="windows-1250", sep=";")
            except FileNotFoundError:
                self.df_abroad = None

        self.candidates = {}

    def load_candidates(self) -> None:
        if self.year in {2007, 2011}:
            self.load_candidates2011()
            return

        columns = self.df_regular.columns

        start = 15
        party = ""
        for i, column in enumerate(columns):  # ide po kolonama u csv fileu i dodaje kandidate u stranke
            if i < start:
                continue
            if (i - start) % 15 == 0:
                party = column
                votes = sum(self.df_regular[column].tolist()) + sum(self.df_special[column].tolist()) + \
                           (sum(self.df_abroad[column].tolist()) if self.df_abroad is not None else 0)
                self.candidates[column] = Party(party, [], votes=votes)
            else:
                votes = sum(self.df_regular[column].tolist()) + sum(self.df_special[column].tolist()) + \
                           (sum(self.df_abroad[column].tolist()) if self.df_abroad is not None else 0)
                self.candidates[party].add_candidate(Candidate(column, votes))

    def load_candidates2011(self):
        last = self.df[self.df.columns[11:]].tail(1).to_dict(orient='records')[0]
        for party in last:
            last[party] = Party(party, [], votes=last[party])
        self.candidates = last

    @staticmethod
    def load_constituency_files(year: int, constituency: str) -> Tuple[str, str, str]:
        c = ""
        if year == 2016:
            c = "0" + constituency
            if "12" not in constituency:
                c += "_00"
        elif year in {2020, 2015}:
            if "12" in constituency:
                constituency = constituency[3:5] + "_" + constituency[0:2]
            else:
                c = "02_"
            c += constituency

        csv1 = os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}/{c}_rezultati.csv")
        csv2 = os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}/{c}_rezultati_posebna.csv")
        csv3 = os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}/{c}_rezultati_inozemstvo.csv")

        return csv1, csv2, csv3


if __name__ == "__main__":
    loader = ElectionLoader(2007, "08")
    loader.load_candidates()

