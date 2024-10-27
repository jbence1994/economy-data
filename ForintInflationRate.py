class ForintInflationRate:
    def __init__(self, year, month, rate):
        self._year = year
        self._month = month
        self._rate = rate

    def __str__(self):
        return f'{self._year} {self._month} {self._rate}'
