from fizzbuzz_plus import FizzbuzzPlus


class TestFizzbuzzPlus:
    def test_return_fizz_for_three(self):
        result = FizzbuzzPlus.fizzbuzz(3)
        expected = 'Fizz'
        assert result == expected

    def test_return_buzz_for_five(self):
        result = FizzbuzzPlus.fizzbuzz(5)
        expected = 'Buzz'
        assert result == expected

    def test_return_two_for_two(self):
        result = FizzbuzzPlus.fizzbuzz(2)
        expected = 2
        assert result == expected

    def test_return_fizz_for_multiples_of_three(self):
        result = FizzbuzzPlus.fizzbuzz(18)
        expected = 'Fizz'
        assert result == expected

    def test_return_buzz_for_multiples_of_five(self):
        result = FizzbuzzPlus.fizzbuzz(35)
        expected = 'FizzBuzz'
        assert result == expected

    def test_return_fizzbuzz_for_multiples_of_three_and_five(self):
        result = FizzbuzzPlus.fizzbuzz(75)
        expected = 'FizzBuzz'
        assert result == expected

    def test_fizzbuzz_range_until_fifteen(self):
        result = list(FizzbuzzPlus.fizzbuzz_range(15))
        expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
                    'Buzz', 11, 'Fizz', 'Fizz', 14, 'FizzBuzz']
        assert result == expected

    def test_fizzbuzz_range_until_one_hundred(self):
        result = list(FizzbuzzPlus.fizzbuzz_range(100))
        expected = [
            1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 'Fizz', 14,
            'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 'Fizz', 'Fizz', 'Buzz', 26,
            'Fizz', 28, 29, 'FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Fizz', 'FizzBuzz', 'Fizz',
            'Fizz', 'Fizz', 'Fizz', 'Buzz', 41, 'Fizz', 'Fizz', 44, 'FizzBuzz', 46, 47,
            'Fizz', 49, 'Buzz', 'FizzBuzz', 'Buzz', 'FizzBuzz', 'FizzBuzz', 'Buzz', 'Buzz',
            'FizzBuzz', 'Buzz', 'Buzz', 'FizzBuzz', 61, 62, 'Fizz', 64,
            'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 'Fizz', 74, 'FizzBuzz', 76,
            77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 'Fizz', 'Fizz', 'Buzz', 86, 'Fizz', 88, 89,
            'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz'
            ]
        assert result == expected
        result_formated = '\n'.join([str(num) for num in result])
        print(f"Output: \nFizzbuzzPlus of the first 100 numbers:\n{result_formated}\n")
