from fileProcessingUtils import process
from uiUtils import display_inflation_rate, display_interest_rate

display_inflation_rate(process('forint_inflation_rate.json'))
display_interest_rate(process('forint_interest_rate.json'))
