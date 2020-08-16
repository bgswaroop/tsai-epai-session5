# EPAi session5 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session5 objectives
This assignment, helps to code the concepts that are learnt in the session 5 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 
 - Arguments & Parameters ; Positional and Keyword Arguments
 - Unpacking
 - Extending Unpacking
 - *args
 - Keyword arguments
 - **kwargs

---

The test cases can be executed by executing _pytest_, from python shell

---
### Functions


**time_it(fn, \*args, repetitions=1, \*\*kwargs)**

    This method, evaluates the function fn with the arguments fn(*args, **kwargs)
    The function fn is evaluated for repetitions times, and the time_it method returns the average time.
     : param fn :  a callable function
     : param args :  positional parameters
     : param repetitions :  a keyword argument, with type int. Denotes the number of times the to run the method and
    evaluate the mean time for each run.

**squared_power_list(power_of_number, \*\*kwargs)**

    Method to compute the power series in the specified range
     : param power_of_number :  integer
     : param kwargs :  'start' :  integer and 'end' :  integer
     : return :  power series as a list

**polygon_area(side_length, \*\*kwargs)**

    Compute the area of the polygon, upto 6 sides.
     : param side_length :  integer
     : param kwargs :  'sides' :  int
     : return :  area of the polygon.

**temp_converter(temperature, \*\*kwargs)**

    Convert fahrenheit to celsius and vice versa.
     : param temperature :  float
     : param kwargs :  'temp_given_in' keyword argument
     : return :  converted temperature

**speed_converter(speed, \*\*kwargs)**

    Convert speed from km/hr
     : param speed :  speed in km/hr
     : param kwargs :  'time' :  str - target units for time <ms|s|m|hr|d>. 'dist' :  str - target units for dist <km|m|ft|yrd>
     : return :  Converted speed

---

### Unit tests


**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_time_it()**

    Test the correctness of the time it function
     : return :  None

**test_squared_power_list()**

    Checking the correctness of squared_power_list.
     : return :  None

**test_temp_converter()**

    Checking the correctness of temp_converter.
     : return :  None

**test_polygon_area()**

    Checking the correctness of polygon_area.
     : return :  None

**test_speed_converter()**

    Checking the correctness of speed_converter.
     : return :  None

**test_time_it_invalid_repetitions()**

    Test invalid repetitions for time_it
     : return : 

**test_squared_power_list_invalid_arg1()**

    Argument power_of_number must be an integer
     : return :  None

**test_squared_power_list_invalid_arg2()**

    Test missing keyword arguments
     : return :  None

**test_squared_power_list_invalid_arg3()**

    Missing start argument
     : return :  None

**test_squared_power_list_invalid_arg4()**

    Missing end argument
     : return :  None

**test_squared_power_list_invalid_arg5()**

    Start should be an integer
     : return :  None

**test_squared_power_list_invalid_arg6()**

    End should be an integer
     : return :  None

**test_squared_power_list_invalid_arg7()**

    The end value should be greater than start
     : return :  None

**test_polygon_area_invalid_arg1()**

    side_length must be an integer
     : return :  None

**test_polygon_area_invalid_arg2()**

    Missing keyword arguments
     : return :  None

**test_polygon_area_invalid_arg3()**

    Missing keywords arguments sides
     : return :  None

**test_polygon_area_invalid_arg4()**

    argument sides must be an integer
     : return :  None

**test_polygon_area_invalid_arg5()**

    sides must be > 2 and <= 6
     : return :  None

**test_temp_converter_invalid_arg1()**

    argument temperature must be an integer
     : return :  None

**test_temp_converter_invalid_arg2()**

    missing keyword arguments
     : return :  None

**test_temp_converter_invalid_arg3()**

    missing keyword argument temp_given_in
     : return :  None

**test_temp_converter_invalid_arg4()**

    temp_given_in must be a string
     : return :  None

**test_temp_converter_invalid_arg5()**

    temp_given_in must be `f` or `c`
     : return :  None

**test_speed_converter_invalid_arg1()**

    Check the data type for speed
     : return :  None

**test_speed_converter_invalid_arg2()**

    Missing keyword arguments
     : return :  None

**test_speed_converter_invalid_arg3()**

    missing dist argument
     : return :  None

**test_speed_converter_invalid_arg4()**

    missing time argument
     : return :  None

**test_speed_converter_invalid_arg5()**

    dist must be a string
     : return :  None

**test_speed_converter_invalid_arg6()**

    time must be a string
     : return :  None

**test_speed_converter_invalid_arg7()**

    Keyword argument `time` must be either ms|s|m|hr|d
     : return :  None

**test_speed_converter_invalid_arg8()**

    Keyword argument `dist` must be either km|m|ft|yrd
     : return :  None
    
---

#### 