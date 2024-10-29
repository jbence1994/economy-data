from matplotlib import pyplot


def create_economy_data_plot(source, title, xlabel, ylabel):
    dates = []
    rates = []

    for economy_data in source:
        dates.append(economy_data.date)
        rates.append(economy_data.rate)

    pyplot.plot(rates, marker='o')

    for i, rate in enumerate(rates):
        pyplot.text(i, rate, f"{rate}", ha='right', va='top')

    pyplot.xticks(ticks=range(len(dates)), labels=dates, rotation=45)

    pyplot.title(title)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)

    pyplot.tight_layout()

    pyplot.show()
