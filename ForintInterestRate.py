class ForintInterestRate:
    def __init__(self, date, rate):
        self._date = date
        self._rate = rate

    def __str__(self):
        return f'{self._rate} {self._date}'
