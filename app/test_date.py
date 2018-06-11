from app import logic
import pytest

future_date = '2025-01-05'
too_old_date = '2015-03-08'
proper_date = '2018-01-01'

error_date_future=logic.error_date_future
error_date_old=logic.error_date_old


def test_input_date_is_in_future():
    expected_output = True
    output=logic.date_future(future_date)
    assert output == expected_output

def test_input_date_is_too_old():
    expected_output = True
    output = logic.data_too_old(too_old_date)
    assert output == expected_output

@pytest.mark.parametrize('date, expected', [
    (proper_date, False),
    (future_date, error_date_future),
    (too_old_date, error_date_old),])

def test_check_if_date_invalid(date, expected):
    output = logic.check_if_date_invalid(date)
    assert output == expected




