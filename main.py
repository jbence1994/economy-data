from fileProcessingUtils import process
from uiUtils import create_economy_data_plot

create_economy_data_plot(
    source=process('forint_inflation_rate.json'),
    title="Forint Inflation",
    xlabel="Year",
    ylabel="Rate"
)

create_economy_data_plot(
    source=process('forint_interest_rate.json'),
    title="Forint Interest Rate",
    xlabel="Year",
    ylabel="Value",
)
