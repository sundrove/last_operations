from func import open_json_file, filter_list, sort_operation_list, date_converting, hide_from, hide_to


def test_open_json_file():
    assert type(open_json_file('test_data.json')) == dict
    assert open_json_file('test_data.json') == {"test": "test"}


def test_filter_list():
    assert filter_list(
        [{'num': "1", 'state': "CANCELED"}, {'num': "2", 'state': 'EXECUTED'}, {'num': "3", 'state': "CANCELED"},
         {'num': "4", 'state': 'EXECUTED'}]) == [{'num': "2", 'state': "EXECUTED"}, {'num': "4", 'state': 'EXECUTED'}]


def test_sort_operation_list():
    assert sort_operation_list([{'date': 1}, {'date': 5}, {'date': 2}, {'date': 9}]) == [{'date': 9}, {'date': 5}, {'date': 2}, {'date': 1}]


def test_date_converting():
    assert date_converting("2018-11-19T04:27:37.904916") == "19.11.2018"
    assert date_converting("2019-04-04T23:20:05.206878") == "04.04.2019"


def test_hide_from():
    assert hide_from('Visa Classic 2842878893689012') == "Visa Classic 2842 87** **** 9012"
    assert hide_from(None) is None


def test_hide_to():
    assert hide_to('Счет 77613226829885488381') == "Счет **8381"
    assert hide_to(None) is None


