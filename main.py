from data_processing.file_processor import process
from ui.ui_utils import create_economy_data_plot

create_economy_data_plot(
    source=process('sources/inflation/forint/all.json'),
    title="Forint Inflation",
    xlabel="Year",
    ylabel="Rate"
)

create_economy_data_plot(
    source=process('sources/interest_rates/forint/all.json'),
    title="Forint Interest Rate",
    xlabel="Year",
    ylabel="Value",
)
