import typing
import pandas as pd
from datetime import date
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
from polygon import RESTClient
import os
from dotenv import load_dotenv
from typing import cast
from urllib3 import HTTPResponse
import json


def getRecentStockData(ticker: str, from_date: str, to_date: str) -> pd.DataFrame:
    """Fetches most up to data historical dataset to preform data analysis on"""

    load_dotenv()
    key: str = os.getenv("API_KEY")
    client = RESTClient(api_key=key)
    df = pd.DataFrame(columns=["date", "price"])
    ticker: str = "AAPL"

    request = cast(
        HTTPResponse,
        client.get_aggs(
            ticker=ticker,
            multiplier=1,
            timespan="day",
            from_=from_date,
            to=to_date,
            raw=True,
        ),
    )

    json_response = json.loads(request.data.decode("utf-8"))
    result_amount = json_response["resultsCount"]
    print(f"count {result_amount}")

    for i in range(result_amount):
        stock_name = json_response["ticker"]
        stock_date = json_response["results"][i]["t"]
        stock_price = json_response["results"][i]["vw"]
        df.loc[i] = stock_date, stock_price

    print(df)

    return df


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
