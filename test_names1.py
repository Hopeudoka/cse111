from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Edrei", "Barajas") == "Barajas; Edrei"
    assert make_full_name("hope", "udoka") == "udoka; hope"
    assert make_full_name("christian", "mapundu") == "mapundu; christian"

def test_extract_family_name():
    assert extract_family_name("Barajas; Edrei") == "Barajas"
    assert extract_family_name("udoka; hope") == "udoka"
    assert extract_family_name("mapundu; christian") == "mapundu"

def test_extract_given_name():
    assert extract_given_name("Barajas; Edrei") == "Edrei"
    assert extract_given_name("udoka; hope") == "hope"
    assert extract_given_name("mapundu; christian") == "christian"

pytest.main(["-v", "--tb=line", "-rN", __file__])