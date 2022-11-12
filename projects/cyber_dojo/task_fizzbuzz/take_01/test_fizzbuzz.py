from fizzbuzz import Fizzbuzz


class TestFizzbuzz:
    def test_return_fizz_for_three(self):
        result = Fizzbuzz.fizzbuzz(3)
        expected = 'Fizz'
        assert result == expected

    def test_return_buzz_for_five(self):
        result = Fizzbuzz.fizzbuzz(5)
        expected = 'Buzz'
        assert result == expected

    def test_return_two_for_two(self):
        result = Fizzbuzz.fizzbuzz(2)
        expected = 2
        assert result == expected

    def test_return_fizz_for_multiples_of_three(self):
        result = Fizzbuzz.fizzbuzz(18)
        expected = 'Fizz'
        assert result == expected

    def test_return_buzz_for_multiples_of_five(self):
        result = Fizzbuzz.fizzbuzz(35)
        expected = 'Buzz'
        assert result == expected

    def test_return_fizzbuzz_for_multiples_of_three_and_five(self):
        result = Fizzbuzz.fizzbuzz(75)
        expected = 'FizzBuzz'
        assert result == expected

    def test_fizzbuzz_range_until_fifteen(self):
        result = list(Fizzbuzz.fizzbuzz_range(15))
        expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
                    'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        assert result == expected

    def test_fizzbuzz_range_until_one_hundred(self):
        result = list(Fizzbuzz.fizzbuzz_range(100))
        expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                    'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26,
                    'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz',
                    'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz',
                    52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64,
                    'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz', 76,
                    77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89,
                    'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']
        assert result == expected
        result_formated = '\n'.join([str(num) for num in result])
        print(f"Output: \nFizzbuzz of the first 100 numbers:\n{result_formated}\n")
