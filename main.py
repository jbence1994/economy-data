from data_processing.file_processor import process
from ui.ui_utils import create_economy_data_plot

create_economy_data_plot(
    source=process('sources/forint_inflation_rate.json'),
    title="Forint Inflation",
    xlabel="Year",
    ylabel="Rate"
)

create_economy_data_plot(
    source=process('sources/forint_interest_rate.json'),
    title="Forint Interest Rate",
    xlabel="Year",
    ylabel="Value",
)
