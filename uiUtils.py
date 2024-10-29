from matplotlib import pyplot


def display_inflation_rate(source):
    inflation_dates = []
    inflation_rates = []

    for inflation_rate in source:
        inflation_dates.append(inflation_rate.date)
        inflation_rates.append(inflation_rate.rate)

    pyplot.plot(inflation_rates, marker='o')

    for i, rate in enumerate(inflation_rates):
        pyplot.text(i, rate, f"{rate}", ha='right', va='top')

    pyplot.xticks(ticks=range(len(inflation_dates)), labels=inflation_dates, rotation=45)

    pyplot.title("Forint Inflation")
    pyplot.xlabel("Year")
    pyplot.ylabel("Rate")

    pyplot.tight_layout()

    pyplot.show()


def display_interest_rate(source):
    interest_rate_dates = []
    interest_rate_values = []

    for interest_rate in source:
        interest_rate_dates.append(interest_rate.date)
        interest_rate_values.append(interest_rate.rate)

    pyplot.plot(interest_rate_values, marker='o')

    for i, rate in enumerate(interest_rate_values):
        pyplot.text(i, rate, f"{rate}", ha='right', va='top')

    pyplot.xticks(ticks=range(len(interest_rate_dates)), labels=interest_rate_dates, rotation=45)

    pyplot.title("Forint Interest Rate")
    pyplot.xlabel("Year")
    pyplot.ylabel("Value")

    pyplot.tight_layout()

    pyplot.show()
