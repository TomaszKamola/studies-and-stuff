import pytest
import numpy as np


## Exercise 1
def add(x, y):
    if isinstance(x, list) and not isinstance(y, list):
        return [i + y for i in x]
    elif not isinstance(x, list) and isinstance(y, list):
        return [x + i for i in y]
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            raise IndexError(
                "Przy operacji dodawania na dwóch listach, "
                "obie listy muszą mieć taką samą długość."
            )
        else:
            x = np.array(x)
            y = np.array(y)
            return list(np.add(x, y))
    else:
        return x + y

def substr(x, y):
    if isinstance(x, list) and not isinstance(y, list):
        return [i - y for i in x]
    elif not isinstance(x, list) and isinstance(y, list):
        return [x - i for i in y]
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            raise IndexError(
                "Przy operacji odejmowania na dwóch listach, "
                "obie listy muszą mieć taką samą długość."
            )
        else:
            x = np.array(x)
            y = np.array(y)
            return list(np.subtract(x, y))
    else:
        return x - y
    
def mult(x, y):
    if isinstance(x, list) and not isinstance(y, list):
        return [i * y for i in x]
    elif not isinstance(x, list) and isinstance(y, list):
        return [i * x for i in y]
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            raise IndexError(
                "Przy operacji mnożenia na dwóch listach, "
                "obie listy muszą mieć taką samą długość."
            )
        else:
            x = np.array(x)
            y = np.array(y)
            return list(np.multiply(x, y))
    else:
        return x * y
    
def div(x, y):
    if isinstance(x, list) and not isinstance(y, list):
        return [i / y for i in x]
    elif not isinstance(x, list) and isinstance(y, list):
        return [x / i for i in y]
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            raise IndexError(
                "Przy operacji dzielenia na dwóch listach, "
                "obie listy muszą mieć taką samą długość."
            )
        else:
            x = np.array(x)
            y = np.array(y)
            return list(np.divide(x, y))
    else:
        return x / y
    
def power(x, y):
    if isinstance(x, list) and not isinstance(y, list):
        return [i ** y for i in x]
    elif not isinstance(x, list) and isinstance(y, list):
        return [x ** i for i in y]
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            raise IndexError(
                "Przy operacji pierwiastkowania na dwóch listach, "
                "obie listy muszą mieć taką samą długość."
            )
        else:
            x = np.array(x)
            y = np.array(y)
            return list(np.power(x, y))
    else:
        return x ** y
    
def log(x):
    if isinstance(x, list):
        return list(np.log(x))
    else:
        return np.log(x)


# Tests
def test_add_two_int():
    assert add(3, 4) == 7
    assert add(5, 6) == 11
    assert add(0, 4) == 4

def test_add_list_and_int():
    assert add([1, 2, 3], 4) == [5, 6, 7]
    assert add(9, [2, 4, 6, 8]) == [11, 13, 15, 17]

def test_add_list_and_list():
    assert add([1, 5, 10], [1, 2, 3]) == [2, 7, 13]
    assert add([1, 1, 1], [2, 2, 2]) == [3, 3, 3]

def test_add_list_and_list_len_non_equal():
    with pytest.raises(IndexError):
        add([1, 3, 5], [2, 4])
    with pytest.raises(IndexError):
        add([1, 3], [2, 4, 6, 8])


def test_substr_two_int():
    assert substr(3, 4) == -1
    assert substr(6, 5) == 1
    assert substr(5, -4) == 9

def test_substr_list_and_int():
    assert substr([1, 2, 3], 4) == [-3, -2, -1]
    assert substr(2, [2, 4, 6, 8]) == [0, -2, -4, -6]

def test_substr_list_and_list():
    assert substr([2, 5, 10], [1, 2, 3]) == [1, 3, 7]
    assert substr([3, 3, 3], [2, 2, 2]) == [1, 1, 1]

def test_substr_list_and_list_len_non_equal():
    with pytest.raises(IndexError):
        substr([1, 3, 5], [2, 4])
    with pytest.raises(IndexError):
        substr([1, 3], [2, 4, 6, 8])


def test_mult_two_int():
    assert mult(3, 4) == 12
    assert mult(6, 5) == 30
    assert mult(5, -4) == -20

def test_mult_list_and_int():
    assert mult([1, 2, 3], 4) == [4, 8, 12]
    assert mult(2, [2, 4, 6, 8]) == [4, 8, 12, 16]

def test_mult_list_and_list():
    assert mult([2, 5, 10], [1, 2, 3]) == [2, 10, 30]
    assert mult([3, 3, 3], [2, 2, 2]) == [6, 6, 6]

def test_mult_list_and_list_len_non_equal():
    with pytest.raises(IndexError):
        mult([1, 3, 5], [2, 4])
    with pytest.raises(IndexError):
        mult([1, 3], [2, 4, 6, 8])


def test_div_two_int():
    assert div(3, 4) == 0.75
    assert div(6, 5) == 1.2
    assert div(5, -4) == -1.25

def test_div_list_and_int():
    assert div([1, 2, 3], 4) == [0.25, 0.5, 0.75]
    assert div(8, [2, 4, 6, 8]) == [4.0, 2.0, 1.3333333333333333333333333333333, 1.0]

def test_div_list_and_list():
    assert div([2, 10, 90], [1, 2, 3]) == [2, 5, 30]
    assert div([30, 30, 30], [2, 2, 2]) == [15, 15, 15]

def test_div_list_and_list_len_non_equal():
    with pytest.raises(IndexError):
        div([1, 3, 5], [2, 4])
    with pytest.raises(IndexError):
        div([1, 3], [2, 4, 6, 8])


def test_power_two_int():
    assert power(3, 4) == 81
    assert power(6, 5) == 7776
    assert power(5, -4) == 0.0016

def test_power_list_and_int():
    assert power([1, 2, 3], 4) == [1, 16, 81]
    assert power(8, [2, 4, 6, 8]) == [64, 4096, 262144, 16777216]

def test_power_list_and_list():
    assert power([2, 10, 90], [1, 2, 3]) == [2, 100, 729000]
    assert power([30, 30, 30], [2, 2, 2]) == [900, 900, 900]

def test_power_list_and_list_len_non_equal():
    with pytest.raises(IndexError):
        power([1, 3, 5], [2, 4])
    with pytest.raises(IndexError):
        power([1, 3], [2, 4, 6, 8])


def test_log_int():
    assert log(4**4) == 5.545177444479562
    assert log(6) == 1.791759469228055
    assert log(5**-4) == -6.437751649736401

def test_log_list():
    assert log([1, 8, 21, 6**3]) == [0.0, 2.0794415416798357, 3.044522437723423, 5.375278407684165]
    assert log([2, 4, 6, 8]) == [0.6931471805599453, 1.3862943611198906, 1.791759469228055, 2.0794415416798357]

# An example of an operation where the result 
# should be correct, but the test does not succeed, 
# is dividing or multiplying with one argument as an 
# int and the other as a list with one element of 
# type int. 
# Although the result from a mathematical point of 
# view should be correct, the test will return an 
# assertion error due to the result being a 
# single-element list.
#
# def test_fail():
#     assert div(3, [3]) == 1
#     assert mult([3], 3) == 9


## Exercise 2
class Calc:

    def add(self, x, y):
        if isinstance(x, list) and not isinstance(y, list):
            return [i + y for i in x]
        elif not isinstance(x, list) and isinstance(y, list):
            return [x + i for i in y]
        elif isinstance(x, list) and isinstance(y, list):
            if len(x) != len(y):
                raise IndexError(
                    "Przy operacji dodawania na dwóch listach, "
                    "obie listy muszą mieć taką samą długość."
                )
            else:
                x = np.array(x)
                y = np.array(y)
                return list(np.add(x, y))
        else:
            return x + y

    def substr(self, x, y):
        if isinstance(x, list) and not isinstance(y, list):
            return [i - y for i in x]
        elif not isinstance(x, list) and isinstance(y, list):
            return [x - i for i in y]
        elif isinstance(x, list) and isinstance(y, list):
            if len(x) != len(y):
                raise IndexError(
                    "Przy operacji odejmowania na dwóch listach, "
                    "obie listy muszą mieć taką samą długość."
                )
            else:
                x = np.array(x)
                y = np.array(y)
                return list(np.subtract(x, y))
        else:
            return x - y
        
    def mult(self, x, y):
        if isinstance(x, list) and not isinstance(y, list):
            return [i * y for i in x]
        elif not isinstance(x, list) and isinstance(y, list):
            return [i * x for i in y]
        elif isinstance(x, list) and isinstance(y, list):
            if len(x) != len(y):
                raise IndexError(
                    "Przy operacji mnożenia na dwóch listach, "
                    "obie listy muszą mieć taką samą długość."
                )
            else:
                x = np.array(x)
                y = np.array(y)
                return list(np.multiply(x, y))
        else:
            return x * y
        
    def div(self, x, y):
        if isinstance(x, list) and not isinstance(y, list):
            return [i / y for i in x]
        elif not isinstance(x, list) and isinstance(y, list):
            return [x / i for i in y]
        elif isinstance(x, list) and isinstance(y, list):
            if len(x) != len(y):
                raise IndexError(
                    "Przy operacji dzielenia na dwóch listach, "
                    "obie listy muszą mieć taką samą długość."
                )
            else:
                x = np.array(x)
                y = np.array(y)
                return list(np.divide(x, y))
        else:
            return x / y
        
    def power(self, x, y):
        if isinstance(x, list) and not isinstance(y, list):
            return [i ** y for i in x]
        elif not isinstance(x, list) and isinstance(y, list):
            return [x ** i for i in y]
        elif isinstance(x, list) and isinstance(y, list):
            if len(x) != len(y):
                raise IndexError(
                    "Przy operacji pierwiastkowania na dwóch listach, "
                    "obie listy muszą mieć taką samą długość."
                )
            else:
                x = np.array(x)
                y = np.array(y)
                return list(np.power(x, y))
        else:
            return x ** y
        
    def log(self, x):
        if isinstance(x, list):
            return list(np.log(x))
        else:
            return np.log(x)
        

@pytest.fixture(scope='function')
def calc(request):
    c = Calc()
    return c


# Tests
class TestCalc:

    @pytest.mark.parametrize('x, y, result', [
        (3, 4, 7), 
        (5, 6, 11), 
        (0, 4, 4)
    ])
    def test_add_method_two_int(self, calc, x, y, result):
        assert calc.add(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([1, 2, 3], 4, [5, 6, 7]), 
        (9, [2, 4, 6, 8], [11, 13, 15, 17])
    ])
    def test_add_method_list_and_int(self, calc, x, y, result):
        assert calc.add(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([1, 5, 10], [1, 2, 3], [2, 7, 13]), 
        ([1, 1, 1], [2, 2, 2], [3, 3, 3])
    ])
    def test_add_method_list_and_list(self, calc, x, y, result):
        assert calc.add(x, y) == result

    @pytest.mark.parametrize('x, y, exp', [
        ([1, 3, 5], [2, 4], pytest.raises(IndexError)),
        ([1, 3], [2, 4, 6, 8], pytest.raises(IndexError))
    ])
    def test_add_method_list_and_list_non_equal(self, calc, x, y, exp):
        with exp:
            calc.add(x, y)

    
    @pytest.mark.parametrize('x, y, result', [
        (3, 4, -1), 
        (6, 5, 1), 
        (5, -4, 9)
    ])
    def test_substr_method_two_int(self, calc, x, y, result):
        assert calc.substr(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([1, 2, 3], 4, [-3, -2, -1]), 
        (2, [2, 4, 6, 8], [0, -2, -4, -6])
    ])
    def test_substr_method_list_and_int(self, calc, x, y, result):
        assert calc.substr(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([2, 5, 10], [1, 2, 3], [1, 3, 7]), 
        ([3, 3, 3], [2, 2, 2], [1, 1, 1])
    ])
    def test_substr_method_list_and_list(self, calc, x, y, result):
        assert calc.substr(x, y) == result

    @pytest.mark.parametrize('x, y, exp', [
        ([1, 3, 5], [2, 4], pytest.raises(IndexError)),
        ([1, 3], [2, 4, 6, 8], pytest.raises(IndexError))
    ])
    def test_substr_method_list_and_list_non_equal(self, calc, x, y, exp):
        with exp:
            calc.substr(x, y)

    
    @pytest.mark.parametrize('x, y, result', [
        (3, 4, 12), 
        (6, 5, 30), 
        (5, -4, -20)
    ])
    def test_mult_method_two_int(self, calc, x, y, result):
        assert calc.mult(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([1, 2, 3], 4, [4, 8, 12]), 
        (2, [2, 4, 6, 8], [4, 8, 12, 16])
    ])
    def test_mult_method_list_and_int(self, calc, x, y, result):
        assert calc.mult(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([2, 5, 10], [1, 2, 3], [2, 10, 30]), 
        ([3, 3, 3], [2, 2, 2], [6, 6, 6])
    ])
    def test_mult_method_list_and_list(self, calc, x, y, result):
        assert calc.mult(x, y) == result

    @pytest.mark.parametrize('x, y, exp', [
        ([1, 3, 5], [2, 4], pytest.raises(IndexError)),
        ([1, 3], [2, 4, 6, 8], pytest.raises(IndexError))
    ])
    def test_mult_method_list_and_list_non_equal(self, calc, x, y, exp):
        with exp:
            calc.mult(x, y)

    
    @pytest.mark.parametrize('x, y, result', [
        (3, 4, 0.75), 
        (6, 5, 1.2), 
        (5, -4, -1.25)
    ])
    def test_div_method_two_int(self, calc, x, y, result):
        assert calc.div(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([1, 2, 3], 4, [0.25, 0.5, 0.75]), 
        (8, [2, 4, 6, 8], [4.0, 2.0, 1.3333333333333333333333333333333, 1.0])
    ])
    def test_div_method_list_and_int(self, calc, x, y, result):
        assert calc.div(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([2, 10, 90], [1, 2, 3], [2, 5, 30]), 
        ([30, 30, 30], [2, 2, 2], [15, 15, 15])
    ])
    def test_div_method_list_and_list(self, calc, x, y, result):
        assert calc.div(x, y) == result

    @pytest.mark.parametrize('x, y, exp', [
        ([1, 3, 5], [2, 4], pytest.raises(IndexError)),
        ([1, 3], [2, 4, 6, 8], pytest.raises(IndexError))
    ])
    def test_div_method_list_and_list_non_equal(self, calc, x, y, exp):
        with exp:
            calc.div(x, y)

    
    @pytest.mark.parametrize('x, y, result', [
        (3, 4, 81), 
        (6, 5, 7776), 
        (5, -4, 0.0016)
    ])
    def test_power_method_two_int(self, calc, x, y, result):
        assert calc.power(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([1, 2, 3], 4, [1, 16, 81]), 
        (8, [2, 4, 6, 8], [64, 4096, 262144, 16777216])
    ])
    def test_power_method_list_and_int(self, calc, x, y, result):
        assert calc.power(x, y) == result

    @pytest.mark.parametrize('x, y, result', [
        ([2, 10, 90], [1, 2, 3], [2, 100, 729000]), 
        ([30, 30, 30], [2, 2, 2], [900, 900, 900])
    ])
    def test_power_method_list_and_list(self, calc, x, y, result):
        assert calc.power(x, y) == result

    @pytest.mark.parametrize('x, y, exp', [
        ([1, 3, 5], [2, 4], pytest.raises(IndexError)),
        ([1, 3], [2, 4, 6, 8], pytest.raises(IndexError))
    ])
    def test_power_method_list_and_list_non_equal(self, calc, x, y, exp):
        with exp:
            calc.power(x, y)

    
    @pytest.mark.parametrize('x, result', [
        (4**4, 5.545177444479562),
        (6, 1.791759469228055),
        (5**-4, -6.437751649736401)
    ])
    def test_log_method_int(self, calc, x, result):
        assert calc.log(x) == result

    @pytest.mark.parametrize('x, result', [
        ([1, 8, 21, 6**3], [0.0, 2.0794415416798357, 3.044522437723423, 5.375278407684165]),
        ([2, 4, 6, 8], [0.6931471805599453, 1.3862943611198906, 1.791759469228055, 2.0794415416798357])
    ])
    def test_log_method_list(self, calc, x, result):
        assert calc.log(x) == result


## Exercise 3
import random

# Classic tests
def test_randbytes_type():
    assert isinstance(random.randbytes(10), bytes) == True
    assert isinstance(random.randbytes(10), str) == False

def test_randrange():
    assert (random.randrange(30) in [i for i in range(0,30)]) == True
    assert random.randrange(0, 21, 2) % 2 == 0
    assert (random.randrange(98, 100) > 99) == False

def test_sample():
    assert len(random.sample([10, 20, 30, 40, 50], k=4)) == 4
    assert (random.sample([10, 20, 30, 40, 50], k=4)[0] in [10, 20, 30, 40, 50]) == True

def test_choice():
    assert random.choice(['a', 'b', 'c']) == 'a' or 'b' or 'c'
    assert (len(random.choice(['55', '666', '7777'])) > 4) == False
    assert (len(random.choice(['55', '666', '7777'])) > 1) == True

def test_choices():
    choices = random.choices(['red', 'black', 'green'], [60, 18, 2], k=8)
    assert (choices.count('red') > choices.count('green')) == True
    assert (choices.count('red') < choices.count('green')) == False

# Parametrized tests
@pytest.mark.parametrize('x, type_, result', [
    (10, bytes, True),
    (10, str, False)
])
def test_randbytes_type(x, type_, result):
    assert isinstance(random.randbytes(x), type_) == result

@pytest.mark.parametrize('x, list_, result', [
    (30, [i for i in range(0,30)], True),
    (13, [i for i in range(0,13)], True)
])
def test_randrange_in_list(x, list_, result):
    assert (random.randrange(x) in list_) == result

@pytest.mark.parametrize('x, y, z, n, result', [
    (0, 21, 2, 2, 0),
    (10, 1000, 10, 10, 0)
])
def test_randrange_is_dividable_by_number(x, y, z, n, result):
    assert random.randrange(x, y, z) % n == result

@pytest.mark.parametrize('x, y, z, result', [
    (98, 100, 99, False),
    (98, 100, 100, False),
    (1, 10, 0, True)
])
def test_randrange_is_not_in_range(x, y, z, result):
    assert (random.randrange(x, y) > z) == result

@pytest.mark.parametrize('list_, k, result', [
    ([10, 20, 30, 40, 50], 4, 4),
    ([1, 10, 15], 3, 3),
    ([100], 1, 1)
])
def test_sample_length(list_, k, result):
    assert len(random.sample(list_, k=k)) == result

@pytest.mark.parametrize('list_, list_2, k, idx, result', [
    ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50], 4, 0, True),
    ([1, 2, 3], [4, 5, 6], 2, 1, False)
])
def test_sample_first_item(list_, list_2, k, idx, result):
    assert (random.sample(list_, k=k)[idx] in list_2) == result

@pytest.mark.parametrize('x, y, z', [
    (1, 2, 3),
    (10, 20, 30),
    (33, 33, 33),
    (0, 0, 0)
])
def test_choice(x, y, z):
    assert random.choice([x, y, z]) == x or y or z

@pytest.mark.parametrize('list_, n, result', [
    (['55', '666', '7777'], 4, False),
    (['55', '666', '7777'], 1, True)
])
def test_choice_len(list_, n, result):
    assert (len(random.choice(list_)) > n) == result

@pytest.mark.parametrize('item1, item2, result', [
    ('red', 'green', True),
    ('green', 'red', False)
])
def test_choices(item1, item2, result):
    choices = random.choices(['red', 'black', 'green'], [60, 18, 2], k=8)
    assert (choices.count(item1) > choices.count(item2)) == result
