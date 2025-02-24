

from basicFunctions import *

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 2) == 1
    assert add(0, 0) == 0
    assert add(1.5, 2.7) == 4.2
    assert add(-5, 5) == 0
    assert add(1000000000, -1000000000) == 0
    assert add(float('inf'), float('inf')) == float('inf')
    assert add(float('-inf'), float('-inf')) == float('-inf')
    assert add(float('nan'), float('nan')) == float('nan')
    print("All tests for add passed.")

def test_subtract():
    assert subtract(7, 4) == 3
    assert subtract(-1, 2) == -3
    assert subtract(0, 0) == 0
    assert subtract(1.5, 2.7) == -1.2
    assert subtract(-5, 5) == -10
    assert subtract(1000000000, -1000000000) == 2000000000
    assert subtract(float('inf'), float('inf')) == float('nan')
    assert subtract(float('-inf'), float('-inf')) == float('nan')
    assert subtract(float('nan'), float('nan')) == float('nan')
    print("All tests for subtract passed.")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 2) == -2
    assert multiply(0, 0) == 0
    assert multiply(1.5, 2.7) == 4.05
    assert multiply(-5, 5) == -25
    assert multiply(1000000000, -1000000000) == -1000000000000000000
    assert multiply(float('inf'), float('inf')) == float('inf')
    assert multiply(float('-inf'), float('-inf')) == float('-inf')
    assert multiply(float('nan'), float('nan')) == float('nan')
    print("All tests for multiply passed.")

def test_divide():
    assert divide(7, 4) == 1.75
    assert divide(-1, 2) == -0.5
    assert divide(0, 0) == float('nan')
    assert divide(1.5, 2.7) == 0.5555555555555556
    assert divide(-5, 5) == -1.0
    assert divide(1000000000, -1000000000) == -1.0
    assert divide(float('inf'), float('inf')) == float('nan')
    assert divide(float('-inf'), float('-inf')) == float('-nan')
    assert divide(float('nan'), float('nan')) == float('nan')
    print("All tests for divide passed.")

def test_power():
    assert pow(3, 2) == 9
    assert pow(-1, 2) == 1
    assert pow(0, 0) == 1
    assert pow(1.5, 2) == 2.25
    assert pow(-5, 2) == 25
    assert pow(1000000000, 2) == 1000000000000000000
    assert pow(float('inf'), 2) == float('inf')
    assert pow(float('-inf'), 2) == float('-inf')
    assert pow(float('nan'), 2) == float('nan')
    print("All tests for power passed.")