from yfinance_fixed import req


def test_get_data_req():
    res = req("PETR4.SA")
    assert res is not None


def test_get_data_req_start_date():
    res = req("PETR4.SA", start="2020-01-01")
    assert res is not None


def test_get_data_req_start_end_date():
    res = req("PETR4.SA", start="2020-01-01", end="2020-12-31")
    assert res is not None
