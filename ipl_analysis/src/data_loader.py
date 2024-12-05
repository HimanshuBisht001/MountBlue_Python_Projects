import csv
from collections import defaultdict


def load_ipl_data():
    with open("data/deliveries.csv", mode="r") as file:
        matches_reader = list(csv.DictReader(file))
    return matches_reader


def load_umpire_data():
    with open("data/umpires.csv", mode="r") as file:
        umpires_reader = list(csv.DictReader(file))
    return umpires_reader


def load_matches_data():
    with open("data/matches.csv", mode="r") as file:
        matches_reader = list(csv.DictReader(file))
    return matches_reader
