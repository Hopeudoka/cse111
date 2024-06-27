from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("mary", "peter") == "peter; mary"
    assert make_full_name("johnson", "trustworthy") == "trustworthy; johnson"
    assert make_full_name("king-gift", "chosen-one") == "chosen-one; king-gift"

def test_extract_family_name():
    assert extract_family_name("peter; mary") == "peter"
    assert extract_family_name("trustworthy; johnson") == "trustworthy"
    assert extract_family_name("chosen-one; king-gift") == "chosen-one"

def test_extract_given_name():
    assert extract_given_name("peter; mary") == "mary"
    assert extract_given_name("trustworthy; johnson") == "johnson"
    assert extract_given_name("chosen-one; king-gift") == "king-gift"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])