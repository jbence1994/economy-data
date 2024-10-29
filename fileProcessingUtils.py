import json

from ForintInflationRate import ForintInflationRate
from ForintInterestRate import ForintInterestRate


def getInflationRates():
    inflationRates = []
    with open('forint_inflation_rate.json') as file:
        data = json.load(file)
        for index, item in enumerate(data):
            inflationRates.append(
                ForintInflationRate(
                    date=item['date'],
                    rate=item['rate'],
                )
            )
    return inflationRates


def getInterestRates():
    forintInterestRates = []
    with open('forint_interest_rate.json') as file:
        data = json.load(file)
        for index, item in enumerate(data):
            forintInterestRates.append(
                ForintInterestRate(
                    date=item['date'],
                    rate=item['rate'],
                )
            )
    return forintInterestRates
