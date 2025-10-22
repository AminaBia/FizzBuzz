import pytest
from FuzzBuzz import FuzzBuzz


def test_FuzzBuzz_is_0_return_0():
    assert FuzzBuzz(0) == 0

