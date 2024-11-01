from matplotlib import pyplot


def create_economy_data_plot(source, width, height, title, xlabel, ylabel):
    dates = []
    rates = []

    for economy_data in source:
        dates.append(economy_data.date)
        rates.append(economy_data.rate)

    pyplot.figure(figsize=(width, height))
    pyplot.plot(rates, marker='.', linewidth=1)

    for i, rate in enumerate(rates):
        pyplot.text(i, rate, f'{rate}%', ha='left', va='bottom', fontdict={'size': 12})

    pyplot.xticks(ticks=range(len(dates)), labels=dates, rotation=45)

    pyplot.title(title, fontdict={'fontsize': 15})
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)

    pyplot.tight_layout()

    pyplot.show()
