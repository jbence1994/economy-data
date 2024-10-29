import json

from model.economy_data import EconomyData


def process(file_name):
    economy_data = []

    with open(file_name) as file:
        data = json.load(file)
        for index, item in enumerate(data):
            economy_data.append(EconomyData(date=item['date'], rate=item['rate']))

    return economy_data
