import pytest
from FuzzBuzz import FuzzBuzz


@pytest.mark.parametrize("n" ,"expected_result",
        [(0,"0"),
         (1,"1"),
         (2,"2"),
         (3,"Fizz"),
         (5,"Buzz"),
         (6,"Fizz"),
         (9,"Fizz"),
         (10,"Buzz"),
         (12,"Fizz"),
         (15,"FizzBuzz"),
         (18,"Fizz"),
         (20,"FizzBuzz"),
         (21,"Fizz"),
         (25,"Buzz"),
         ],)
def test_numbers_return_expected(n, expected_result:str):
        actual_result = FuzzBuzz(n)
        assert actual_result == expected_result


