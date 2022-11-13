class Fizzbuzz:
    @staticmethod
    def fizzbuzz(number):
        res = 'Fizz' if number % 3 == 0 else ''
        res += 'Buzz' if number % 5 == 0 else ''
        if not res:
            res = number
        return res

    @classmethod
    def fizzbuzz_range(cls, max_number):
        for number in range(1, max_number + 1):
            yield cls.fizzbuzz(number)
