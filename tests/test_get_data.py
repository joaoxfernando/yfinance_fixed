from yfinance_fixed import download


def test_get_data_req():
    res = download("PETR4.SA")
    assert res is not None


def test_get_data_req_start_date():
    res = download("PETR4.SA", start="2020-01-01")
    assert res is not None


def test_get_data_req_start_end_date():
    res = download("PETR4.SA", start="2020-01-01", end="2020-12-31")
    assert res is not None
