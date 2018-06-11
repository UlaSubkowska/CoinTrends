from app import logic
import pytest

example_data=[{'date': '2018-01-01', 'price': 13545.61}]
label=['18-01-01']

example_data_20th=[{'date': '2018-01-20', 'price': 12464.23}]
label_20th=['18-01-20']


@pytest.mark.parametrize('data, label', [
    (example_data, label),
    (example_data_20th, label_20th)])

def test_labels_for_chart(data, label):
    output = logic.data_for_chart_labels(data)
    assert output == label


