import pytest

from fizzbuzz_plus import fizzbuzz, fizzbuzz_range, to_str


@pytest.mark.parametrize('val, expected', [
    (1, '1'),
    (2, '2'),
    (3, 'Fizz'),
    (4, '4'),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (10, 'Buzz'),
    (13, 'Fizz'),
    (15, 'FizzBuzz'),
    (31, 'Fizz'),
    (52, 'Buzz'),
    ])
def test_fizzbuzz(val, expected):
    assert fizzbuzz(val) == expected


def test_fizzbuzz_range_until_fifteen():
    result = list(fizzbuzz_range(15))
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz',
                'Buzz', '11', 'Fizz', 'Fizz', '14', 'FizzBuzz']
    assert result == expected


@pytest.mark.parametrize('val, expected', [
    (1, '1'),
    (2, '1\n2'),
    (18, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\nFizz\n14\n"
         "FizzBuzz\n16\n17\nFizz"),
    ])
def test_fizzbuzz_range(val, expected):
    assert to_str(fizzbuzz_range(val)) == expected


def test_fizzbuzz_range_until_one_hundred():
    result = to_str(fizzbuzz_range(100))
    expected = ', '.join([
        "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\nFizz\n14\n"
        "FizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\nFizz\nFizz\nBuzz\n26\n"
        "Fizz\n28\n29\nFizzBuzz\nFizz\nFizz\nFizz\nFizz\nFizzBuzz\nFizz\n"
        "Fizz\nFizz\nFizz\nBuzz\n41\nFizz\nFizz\n44\nFizzBuzz\n46\n47\n"
        "Fizz\n49\nBuzz\nFizzBuzz\nBuzz\nFizzBuzz\nFizzBuzz\nBuzz\nBuzz\n"
        "FizzBuzz\nBuzz\nBuzz\nFizzBuzz\n61\n62\nFizz\n64\n"
        "Buzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\nFizz\n74\nFizzBuzz\n76\n"
        "77\nFizz\n79\nBuzz\nFizz\n82\nFizz\nFizz\nBuzz\n86\nFizz\n88\n89\n"
        "FizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz"
        ])
    assert result == expected
    print(f"Output: \nFizzbuzzPlus of the first 100 numbers:\n{result}\n")
