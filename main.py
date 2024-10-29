from data_processing.file_processor import process
from ui.ui_utils import create_economy_data_plot

create_economy_data_plot(
    source=process('data_sources/inflation/forint_inflation_rate.json'),
    title="Forint Inflation",
    xlabel="Year",
    ylabel="Rate"
)

create_economy_data_plot(
    source=process('data_sources/interest_rates/forint_interest_rate.json'),
    title="Forint Interest Rate",
    xlabel="Year",
    ylabel="Value",
)
