# -*- coding: windows-1250 -*-

import os
from dataclasses import dataclass

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

    def __init__(self, year: int) -> None:
        assert os.path.exists(os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}")),\
            f"Couldn't locate folder with election data from {year}"

        # učitavanje csv fileova
        csv_regular_results = os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}/001_00_rezultati.csv")
        self.df_regular = pd.read_csv(csv_regular_results, encoding="windows-1250", sep=";")

        csv_special_results = os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}/001_00_rezultati_posebna.csv")
        self.df_special = pd.read_csv(csv_special_results, encoding="windows-1250", sep=";")

        csv_abroad_results = os.path.join(PROJECT_PATH, f"past_elections/CSV-{year}/001_00_rezultati_inozemstvo.csv")
        self.df_abroad = pd.read_csv(csv_abroad_results, encoding="windows-1250", sep=";")

        self.candidates = {}

    def load_candidates(self) -> None:
        columns = self.df_regular.columns

        # dict kandidata po strankama
        self.candidates = {}

        start = 15
        party = ""
        for i, column in enumerate(columns):  # ide po kolonama u csv fileu i dodaje kandidate u stranke
            if i < start:
                continue
            if (i - start) % 15 == 0:
                party = column
                votes = sum(self.df_regular[column].tolist()) + sum(self.df_special[column].tolist()) + sum(self.df_abroad[column].tolist())
                self.candidates[column] = Party(party, [], votes=votes)
            else:
                votes = sum(self.df_regular[column].tolist()) + sum(self.df_special[column].tolist()) + sum(self.df_abroad[column].tolist())
                self.candidates[party].add_candidate(Candidate(column, votes))


