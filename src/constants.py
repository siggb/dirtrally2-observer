import re

URL = "https://psnprofiles.com/trophy/8745-dirt-rally-20/9-fire-up-that-car-again"

# https://regex101.com/r/kkFCVZ/4
REGEX_PATTERN = r"(?<=\>)(\d{1,2})(?:\S+?)(\s\w{3}\s\d{4})(?:\D+?)(\d{1,2}\:\d{1,2}\:\d{1,2}\s\w{2})(?=\<)"
DATETIME_FORMAT = "%d  %b %Y %I:%M:%S %p"

FIRST_ACHIEVERS_COUNT = 50
LATEST_ACHIEVERS_COUNT = 50
TOTAL_ACHIEVERS = FIRST_ACHIEVERS_COUNT + LATEST_ACHIEVERS_COUNT
MAX_AVG_DAILY_ACHIEVERS = 10

FIGURE_PATH = "resources/barchart.png"
DATE_FORMAT = "%Y-%m-%d"
