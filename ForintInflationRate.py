class ForintInflationRate:
    def __init__(self, year, month, rate):
        self._year = year
        self._month = month
        self._rate = rate

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def rate(self):
        return self._rate

    def __str__(self):
        return f'{self._year} {self._month} {self._rate}'
