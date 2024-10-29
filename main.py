from fileProcessingUtils import process
from uiUtils import create_economy_data_plot

create_economy_data_plot(
    process('forint_inflation_rate.json'),
    "Forint Inflation",
    "Year",
    "Rate"
)

create_economy_data_plot(
    process('forint_interest_rate.json'),
    "Forint Interest Rate",
    "Year",
    "Value",
)
