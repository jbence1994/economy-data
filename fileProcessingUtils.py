import json

from ForintInflationRate import ForintInflationRate
from ForintInterestRate import ForintInterestRate


def getInflationRates():
    inflationRates = []
    with open('forint-inflation.json') as file:
        data = json.load(file)
        for index, item in enumerate(data):
            inflationRates.append(
                ForintInflationRate(
                    year=item['year'],
                    month=item['month'],
                    rate=item['rate']['prevYear'],
                )
            )
    return inflationRates


def getInterestRates():
    forintInterestRates = []
    with open('forint-interest-rates.txt') as file:
        data = file.readlines()
        for line in data:
            parts = line.strip().split(';')
            forintInterestRates.append(
                ForintInterestRate(
                    date=parts[0],
                    rate=parts[1],
                )
            )

    return forintInterestRates
