from temperature import fahrenheit_to_celsius
from pytest import approx

def test_fahrenheit_to_celsius():
    assert(fahrenheit_to_celsius(32) == 0)
    assert(fahrenheit_to_celsius(24521435) == approx (136233001, .1))
    assert(fahrenheit_to_celsius(-20) == approx (-28.8898, .1))
    assert(fahrenheit_to_celsius(32) == 0)

test_fahrenheit_to_celsius()