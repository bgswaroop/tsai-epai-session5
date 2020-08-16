import inspect
import os
import re

import pytest

import session5
from session5 import *


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_time_it():
    """
    Test the correctness of the time it function
    :return: None
    """
    time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5)
    time_it(squared_power_list, 2, start=0, end=5, repetitions=5)
    time_it(polygon_area, 15, sides=3, repetitions=10)
    time_it(temp_converter, 100, temp_given_in='f', repetitons=100)
    time_it(speed_converter, 100, dist='km', time='min', repetitons=200)


def test_squared_power_list():
    """
    Checking the correctness of squared_power_list.
    :return: None
    """
    result = squared_power_list(2, start=0, end=5)
    assert result == [1, 2, 4, 8, 16, 32]


def test_temp_converter():
    """
    Checking the correctness of temp_converter.
    :return: None
    """
    result = temp_converter(100, temp_given_in='f')
    assert math.isclose(result, 37.77777777777778, abs_tol=1e-5)


def test_polygon_area():
    """
    Checking the correctness of polygon_area.
    :return: None
    """
    result = polygon_area(15, sides=3)
    assert math.isclose(result, 6.495190528383289, abs_tol=1e-5)


def test_speed_converter():
    """
    Checking the correctness of speed_converter.
    :return: None
    """
    result = speed_converter(100, dist='km', time='min')
    assert math.isclose(result, 1.6666666666666667, abs_tol=1e-5)


def test_time_it_invalid_repetitions():
    """
    Test invalid repetitions for time_it
    :return:
    """
    with pytest.raises(ValueError):
        time_it(polygon_area, 15, sides=3, repetitions='10')
    with pytest.raises(ValueError):
        time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5.6)
    with pytest.raises(ValueError):
        time_it(squared_power_list, 2, start=0, end=5, repetitions='three')
    with pytest.raises(ValueError):
        time_it(polygon_area, 15, sides=3, repetitions=10.01)
    with pytest.raises(ValueError):
        time_it(temp_converter, 100, temp_given_in='f', repetitions=-10)
    with pytest.raises(ValueError):
        time_it(speed_converter, 100, dist='km', time='min', repetitions='200')


def test_squared_power_list_invalid_arg1():
    """
    Argument power_of_number must be an integer
    :return: None
    """
    with pytest.raises(ValueError):
        squared_power_list(power_of_number='2', start=0, end=5)


def test_squared_power_list_invalid_arg2():
    """
    Test missing keyword arguments
    :return: None
    """
    with pytest.raises(ValueError):
        squared_power_list(2)


def test_squared_power_list_invalid_arg3():
    """
    Missing start argument
    :return: None
    """
    with pytest.raises(ValueError):
        squared_power_list(2, end=5)


def test_squared_power_list_invalid_arg4():
    """
    Missing end argument
    :return: None
    """
    with pytest.raises(ValueError):
        squared_power_list(2, start=0)


def test_squared_power_list_invalid_arg5():
    """
    Start should be an integer
    :return: None
    """
    with pytest.raises(ValueError):
        squared_power_list(2, start='0', end=5)


def test_squared_power_list_invalid_arg6():
    """
    End should be an integer
    :return: None
    """
    with pytest.raises(ValueError):
        squared_power_list(2, start=0, end='5')


def test_squared_power_list_invalid_arg7():
    """
    The end value should be greater than start
    :return: None
    """
    with pytest.raises(ValueError):
        squared_power_list(2, start=10, end=5)


def test_polygon_area_invalid_arg1():
    """
    side_length must be an integer
    :return: None
    """
    with pytest.raises(ValueError):
        polygon_area('15.7', sides=3)


def test_polygon_area_invalid_arg2():
    """
    Missing keyword arguments
    :return: None
    """
    with pytest.raises(ValueError):
        polygon_area(15)


def test_polygon_area_invalid_arg3():
    """
    Missing keywords arguments sides
    :return: None
    """
    with pytest.raises(ValueError):
        polygon_area(15, sides_invalid=3)


def test_polygon_area_invalid_arg4():
    """
    argument sides must be an integer
    :return: None
    """
    with pytest.raises(ValueError):
        polygon_area(15, sides='3')


def test_polygon_area_invalid_arg5():
    """
    sides must be > 2 and <= 6
    :return: None
    """
    with pytest.raises(ValueError):
        polygon_area(15, sides=2)


def test_temp_converter_invalid_arg1():
    """
    argument temperature must be an integer
    :return: None
    """
    with pytest.raises(ValueError):
        temp_converter('100', temp_given_in='f')


def test_temp_converter_invalid_arg2():
    """
    missing keyword arguments
    :return: None
    """
    with pytest.raises(ValueError):
        temp_converter(100)


def test_temp_converter_invalid_arg3():
    """
    missing keyword argument temp_given_in
    :return: None
    """
    with pytest.raises(ValueError):
        temp_converter(100, temp_given_in_invalid='f')


def test_temp_converter_invalid_arg4():
    """
    temp_given_in must be a string
    :return: None
    """
    with pytest.raises(ValueError):
        temp_converter(100, temp_given_in=10)


def test_temp_converter_invalid_arg5():
    """
    temp_given_in must be `f` or `c`
    :return: None
    """
    with pytest.raises(ValueError):
        temp_converter(100, temp_given_in='cf')


def test_speed_converter_invalid_arg1():
    """
    Check the data type for speed
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter('100', dist='km', time='min')


def test_speed_converter_invalid_arg2():
    """
    Missing keyword arguments
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter(100)


def test_speed_converter_invalid_arg3():
    """
    missing dist argument
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter(100, time='min')


def test_speed_converter_invalid_arg4():
    """
    missing time argument
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter(100, dist='km')


def test_speed_converter_invalid_arg5():
    """
    dist must be a string
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter(100, dist=10, time='min')


def test_speed_converter_invalid_arg6():
    """
    time must be a string
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter(100, dist='km', time=10)


def test_speed_converter_invalid_arg7():
    """
    Keyword argument `time` must be either ms|s|m|hr|d
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter(100, dist='km', time='minutes')


def test_speed_converter_invalid_arg8():
    """
    Keyword argument `dist` must be either km|m|ft|yrd
    :return: None
    """
    with pytest.raises(ValueError):
        speed_converter(100, dist='kilometers', time='m')
