import constants
import requests
import re
from datetime import datetime
from datetime import date
from collections import Counter
from matplotlib import pyplot as plt


def getDatesList(text: str) -> [date]:
    r = re.findall(constants.REGEX_PATTERN, text)
    list = []
    for group in r:
        s = ' '.join(map(str, group))
        d = datetime.strptime(s, constants.DATETIME_FORMAT)
        list.append(d.date())
    return list


def filterPrevYears(dates: [date]) -> [date]:
    list = []
    currYear = date.today().year
    for d in dates:
        if d.year == currYear:
            list.append(d)
    return list[::-1]


def groupByDate(dates: [date]) -> {date: int}:
    c = Counter(dates)
    return dict(c)


def drawBarChart(datesDict: {date: int}):
    xValues = datesDict.values()
    yValues = list(map(lambda k: k.strftime(
        constants.DATE_FORMAT), datesDict.keys()))
    colors = ['grey' if (x <= constants.MAX_AVG_DAILY_ACHIEVERS)
              else 'blue' for x in xValues]

    plt.barh(yValues, xValues, color=colors, align="center")
    plt.xlabel("No. of achievers")
    plt.ylabel("Date")
    plt.title("Latest 50 Achievers")

    plt.savefig(constants.FIGURE_PATH, dpi=300, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    print("# Making a GET request")
    r = requests.get(url=constants.URL)

    print("# Parsing the response")
    allDates = getDatesList(r.text)
    assert len(allDates) == constants.TOTAL_ACHIEVERS

    print("# Filtering out previous years")
    filteredDates = filterPrevYears(allDates)
    assert len(filteredDates) == constants.LATEST_ACHIEVERS_COUNT

    print("# Drawing a 2D bar chart")
    datesDict = groupByDate(filteredDates)
    drawBarChart(datesDict)
