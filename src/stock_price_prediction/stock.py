import typing
from datetime import date
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
from polygon import RESTClient
import os
from dotenv import load_dotenv


def getRecentStockData(ticker: str, from_date: str, to_date: str):
    """Fetches most up to data historical dataset to preform data analysis on"""
    load_dotenv()
    key: str = os.getenv("API_KEY")
    client = RESTClient(api_key=key)

    ticker: str = "AAPL"
    aggs = []
    count: int = 0

    for a in client.list_aggs(
        ticker=ticker,
        multiplier=1,
        timespan="day",
        from_=from_date,
        to=to_date,
    ):
        aggs.append(a)
        count = count + 1

        print("========================================")
        print(f"count: {count}")
        print(a)

    # print(aggs)

    return None


def getYesterdaysDate() -> str:
    today: str = datetime.now()
    yesterday: str = today - relativedelta(days=1)
    return yesterday


def getTwoYearsAgoDate(yesterday: str) -> str:
    two_years_ago: str = yesterday - relativedelta(years=2)
    return two_years_ago


# Testing functions
yesterday: str = getYesterdaysDate()
two_years_ago: str = getTwoYearsAgoDate(yesterday)
getRecentStockData("AAPL", two_years_ago, yesterday)
