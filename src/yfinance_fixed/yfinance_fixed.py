from typing import Optional
import pandas as pd
import yfinance as yf
from curl_cffi import requests

session = requests.Session(impersonate="chrome")
session.verify = False


def req(ticker: str, start: Optional[str] = None, end: Optional[str] = None):
    df = yf.download(ticker, start=start, end=end, session=session)
    df.columns = df.columns.get_level_values(0)
    return df
