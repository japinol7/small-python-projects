class Fizzbuzz:
    @staticmethod
    def fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        if number % 3 == 0:
            return 'Fizz'
        if number % 5 == 0:
            return 'Buzz'
        return number

    @classmethod
    def fizzbuzz_range(cls, max_number):
        for number in range(1, max_number + 1):
            yield cls.fizzbuzz(number)
