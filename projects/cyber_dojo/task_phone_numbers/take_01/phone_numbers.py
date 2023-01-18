class PhoneNumbers:
    @staticmethod
    def get_digits(strs):
        """Gets only the digits of a sequence of strings."""
        return {''.join([ch for ch in line if ch.isdigit()]) for line in strs}

    @staticmethod
    def is_consistent(phone_numbers):
        if not phone_numbers:
            return False

        phone_numbers = PhoneNumbers.get_digits(phone_numbers)
        phone_numbers = sorted(phone_numbers)
        for phone_number in phone_numbers:
            if sum(1 if phone.startswith(phone_number) else 0 for phone in phone_numbers) > 1:
                return False
        return True
