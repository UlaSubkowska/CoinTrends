from app import logic


def test_input_date_is_in_future():
    assert logic.date_future('2025-01-05')==True

def test_input_date_is_too_old():
    assert logic.data_too_old('2015-03-08')==True

def test_check_if_date_invalid_date_is_ok():
    assert logic.check_if_date_invalid('2018-01-01') == False

def test_date_invalid_future_error_message():
    assert logic.check_if_date_invalid('2025-01-05')=="Sorry you can't type start date in the future, please try type " \
                                                      "proper date."

def test_date_invalid_too_old_error_message():
    assert logic.check_if_date_invalid('2015-03-08')=='Sorry but we do not have such an archival data, beginning data ' \
                                                      'for ETHUSD and LTCUSD is 2016-03-08, please type date once again.'


