import pytest

from fizzbuzz import fizzbuzz, fizzbuzz_range, to_str


@pytest.mark.parametrize('val, expected', [
    (1, '1'),
    (2, '2'),
    (3, 'Fizz'),
    (4, '4'),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (10, 'Buzz'),
    (13, '13'),
    (15, 'FizzBuzz'),
    (52, '52'),
    ])
def test_fizzbuzz(val, expected):
    assert fizzbuzz(val) == expected


@pytest.mark.parametrize('val, expected', [
    (1, '1'),
    (2, '1\n2'),
    (15, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz"),
    ])
def test_fizzbuzz_range(val, expected):
    assert to_str(fizzbuzz_range(val)) == expected


def test_fizzbuzz_range_until_one_hundred():
    result = to_str(fizzbuzz_range(100))
    expected = ', '.join([
        "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\n"
        "FizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\n"
        "Fizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\n"
        "Buzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n"
        "52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\n"
        "Buzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n"
        "77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\n"
        "FizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz"
    ])
    assert result == expected
    print(f"Output: \nFizzbuzzPlus of the first 100 numbers:\n{result}\n")
