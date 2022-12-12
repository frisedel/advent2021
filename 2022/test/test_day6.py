from day6.adv_6 import adv6_1, adv6_2
from test_input.test_data_day6 import test_stream_1, test_stream_2, test_stream_3, test_stream_4, test_stream_5

def test_adv6_1():
    index_1 = adv6_1(test_stream_1)
    index_2 = adv6_1(test_stream_2)
    index_3 = adv6_1(test_stream_3)
    index_4 = adv6_1(test_stream_4)
    index_5 = adv6_1(test_stream_5)

    assert index_1 == 7
    assert index_2 == 5
    assert index_3 == 6
    assert index_4 == 10
    assert index_5 == 11

def test_adv6_2():
    index_1 = adv6_2(test_stream_1)
    index_2 = adv6_2(test_stream_2)
    index_3 = adv6_2(test_stream_3)
    index_4 = adv6_2(test_stream_4)
    index_5 = adv6_2(test_stream_5)

    assert index_1 == 19
    assert index_2 == 23
    assert index_3 == 23
    assert index_4 == 29
    assert index_5 == 26