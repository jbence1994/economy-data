class ForintInflationRate:
    def __init__(self, date, rate):
        self._date = date
        self._rate = rate

    @property
    def date(self):
        return self._date

    @property
    def rate(self):
        return self._rate

    def __str__(self):
        return f'{self._date} {self._rate}'
