from data_processing.file_processor import process
from ui.ui_utils import create_economy_data_plot

# Sample code
create_economy_data_plot(
    source=process('Add the path for the processable source file'),
    width=13,
    height=8,
    title='Add a title',
    xlabel='Add a label to the X axis',
    ylabel='Add a label to the Y axis'
)
