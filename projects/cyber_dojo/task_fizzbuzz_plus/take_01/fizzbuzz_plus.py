class FizzbuzzPlus:
    @staticmethod
    def is_fizz(number):
        if '3' in str(number):
            return True
        if number % 3 == 0:
            return True
        return False

    @staticmethod
    def is_buzz(number):
        if '5' in str(number):
            return True
        if number % 5 == 0:
            return True
        return False

    @staticmethod
    def fizzbuzz(number):
        res = 'Fizz' if FizzbuzzPlus.is_fizz(number) else ''
        res += 'Buzz' if FizzbuzzPlus.is_buzz(number) else ''
        if not res:
            res = number
        return res

    @classmethod
    def fizzbuzz_range(cls, max_number):
        for number in range(1, max_number + 1):
            yield cls.fizzbuzz(number)
