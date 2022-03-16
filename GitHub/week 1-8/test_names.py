from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Brendan', 'Willis') 
    assert make_full_name('Brendon', 'Alder') 
    assert make_full_name('Noelia', 'Paz') 
    assert make_full_name('Radhika', 'Dhanpal') 
    assert make_full_name('Dusan', 'Vasica') 

def test_extract_family_name():
    assert extract_family_name('Willis; Brendan') 
    assert extract_family_name('Alder; Brendon') 
    assert extract_family_name('Paz; Noelia') 
    assert extract_family_name('Dhanpal; Radhika') 
    assert extract_family_name('Vasica; Dusan') 

def test_extract_given_name():
    assert extract_given_name('Willis/ Brendan') 
    assert extract_given_name('Alder/ Brendon') 
    assert extract_given_name('Paz/ Noelia') 
    assert extract_given_name('Dhanpal/ Radhika') 
    assert extract_given_name('Vasica/ Dusan') 

pytest.main(["-v", "--tb=line", "-rN", __file__])

