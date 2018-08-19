from arabic_pronunciation import phonetise_Arabic
import pytest

# @pytest.mark.skip(reason="integration slow test")
def test_pronounciations():
    actual = phonetise_Arabic.phonetise_word("بِمُسْتَطِيل")
    expected = ['b i0 m u0 s t A T ii0 l']
    if(actual != expected):
        raise AssertionError(f'Expected {expected}, but found {actual}')



