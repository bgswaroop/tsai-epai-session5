import math
import time


def time_it(fn, *args, repetitions=1, **kwargs):
    """
    This method, evaluates the function fn with the arguments fn(*args, **kwargs)
    The function fn is evaluated for repetitions times, and the time_it method returns the average time.
    :param fn: a callable function
    :param args: positional parameters
    :param repetitions: a keyword argument, with type int. Denotes the number of times the to run the method and
    evaluate the mean time for each run.
    """

    if not isinstance(repetitions, int):
        raise ValueError('Keyword argument `repetitions` must be an integer')
    if repetitions < 0:
        raise ValueError('`repetitions` must be > 0')

    begin = time.perf_counter()
    for _ in range(repetitions):
        fn(*args, **kwargs)
    end = time.perf_counter()
    time_elapsed = end - begin
    average_time = time_elapsed / repetitions
    return average_time


def squared_power_list(power_of_number, **kwargs):
    """
    Method to compute the power series in the specified range
    :param power_of_number: integer
    :param kwargs: 'start': integer and 'end': integer
    :return: power series as a list
    """
    if not isinstance(power_of_number, int):
        raise ValueError('Keyword argument `power_of_number` must be an integer')

    if not kwargs:
        raise ValueError('Missing keyword arguments!')
    else:
        if 'start' not in kwargs:
            raise ValueError('Missing keyword argument `start`')
        if 'end' not in kwargs:
            raise ValueError('Missing keyword argument `end`')

        start = kwargs['start']
        end = kwargs['end']

        if not isinstance(start, int):
            raise ValueError('Keyword argument `start` must be an integer')
        if not isinstance(end, int):
            raise ValueError('Keyword argument `end` must be an integer')

        if end < start:
            raise ValueError('end value {end}, must be greater than the start {start}'.format(end=end, start=start))

    return [power_of_number ** x for x in range(start, end + 1)]


def polygon_area(side_length, **kwargs):
    """
    Compute the area of the polygon, upto 6 sides.
    :param side_length: integer
    :param kwargs: 'sides': int
    :return: area of the polygon.
    """
    if not isinstance(side_length, int):
        raise ValueError('Positional argument `side_length` must be an integer')

    if not kwargs:
        raise ValueError('Missing keyword arguments!')
    else:
        if 'sides' not in kwargs:
            raise ValueError('Missing keyword argument `sides`')

        sides = kwargs['sides']

        if not isinstance(sides, int):
            raise ValueError('Keyword argument `sides` must be an integer')

        if sides < 3 or sides > 6:
            raise ValueError('Number of polygon sides must be within 3-6, but found {}'.format(sides))

        if sides == 3:
            return side_length * math.sqrt(3) / 4
        elif sides == 4:
            return side_length ** 2
        if sides == 5:
            return 5 * side_length ** 2 / (4 * math.tan(36))
        if sides == 6:
            return (3 * math.sqrt(3)) * side_length ** 2 / 2


def temp_converter(temperature, **kwargs):
    """
    Convert fahrenheit to celsius and vice versa.
    :param temperature: float
    :param kwargs: 'temp_given_in' keyword argument
    :return: converted temperature
    """
    if not isinstance(temperature, float) and not isinstance(temperature, int):
        raise ValueError('Positional argument `temperature` must be a float / int')

    if not kwargs:
        raise ValueError('Missing keyword argument!')
    else:
        if 'temp_given_in' not in kwargs:
            raise ValueError('Missing keyword argument `temp_given_in`')

        temp_given_in = kwargs['temp_given_in']

        if not isinstance(temp_given_in, str):
            raise ValueError('Keyword argument `temp_given_in` must be a str')

        if temp_given_in == 'c':
            return temperature * 1.8 + 32
        elif temp_given_in == 'f':
            return (temperature - 32) / 1.8
        else:
            raise ValueError('Temperature type must be `c` or `f`'.format(temp_given_in))


def speed_converter(speed, **kwargs):
    """
    Convert speed from km/hr
    :param speed: speed in km/hr
    :param kwargs: 'time': str - target units for time <ms|s|m|hr|d>. 'dist': str - target units for dist <km|m|ft|yrd>
    :return: Converted speed
    """
    if not isinstance(speed, float) and not isinstance(speed, int):
        raise ValueError('Keyword argument `speed` must be an float/integer')

    if not kwargs:
        raise ValueError('Missing keyword arguments!')
    else:
        if 'dist' not in kwargs:
            raise ValueError('Missing keyword argument `dist`')
        if 'time' not in kwargs:
            raise ValueError('Missing keyword argument `time`')

        dist = kwargs['dist']
        time = kwargs['time']

        if not isinstance(dist, str):
            raise ValueError('Keyword argument `dist` must be a string')
        if not isinstance(time, str):
            raise ValueError('Keyword argument `time` must be a string')

        if time == 'ms':
            time_multiplier = 60 * 60 * 100
        elif time == 's':
            time_multiplier = 60 * 60
        elif time == 'min' or time == 'm':
            time_multiplier = 60
        elif time == 'hr':
            time_multiplier = 1
        elif time == 'day':
            time_multiplier = 1 / 24
        else:
            raise ValueError('Keyword argument `time` must be either ms|s|m|hr|d')

        if dist == 'km':
            distance_multiplier = 1
        elif dist == 'm':
            distance_multiplier = 1000
        elif dist == 'ft':
            distance_multiplier = 3280.8398950131
        elif dist == 'yrd':
            distance_multiplier = 1093.6
        else:
            raise ValueError('Keyword argument `dist` must be either km|m|ft|yrd')

        return speed * distance_multiplier / time_multiplier


if __name__ == '__main__':
    print(time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5), 'sec')
    print(time_it(squared_power_list, 2, start=0, end=5, repetitions=5))
    print(time_it(polygon_area, 15, sides=3, repetitions=10))
    print(time_it(temp_converter, 100, temp_given_in='f', repetitons=100))
    print(time_it(speed_converter, 100, dist='km', time='min', repetitons=200))
