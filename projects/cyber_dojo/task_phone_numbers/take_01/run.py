import os
from timeit import repeat

from phone_numbers import PhoneNumbers

APP_VERSION = 'take_01'
REPEAT_TIMEIT = 5
FILE_PATH_PHONES_CONSISTENT = os.path.join('..', 'data', 'phone_numbers_consistent_7000.txt')
FILE_PATH_PHONES_NOT_CONSISTENT = os.path.join('..', 'data', 'phone_numbers_not_consistent_7000.txt')
FILE_PATH_OUT = os.path.join('..', 'out', f'{APP_VERSION}_log.txt')


def is_consistent_phone_numbers(phone_numbers):
    return PhoneNumbers.is_consistent(phone_numbers)


def process_phone_data_file(phone_numbers_file, file_write_mode, is_consistent, end_of_log_txt=''):
    with open(phone_numbers_file, 'r', encoding='utf8') as fin:
        phone_numbers = fin.readlines()

    intro_txt = f"Time task_phone_numbers {APP_VERSION}, best time of {REPEAT_TIMEIT} executions\n" \
                f"File: {phone_numbers_file}"
    print(intro_txt)
    res = repeat(stmt="is_consistent_phone_numbers(phone_numbers)",
                 setup=f"phone_numbers={phone_numbers}",
                 globals=globals(),
                 repeat=REPEAT_TIMEIT,
                 number=1)

    time_txt = f"Time {APP_VERSION} {'NOT ' if not is_consistent else '    '}" \
               f"consistent data: {min(res)}{end_of_log_txt}"
    print(time_txt)
    with open(FILE_PATH_OUT, file_write_mode, encoding='utf8') as file_out:
        file_out.write(f"{intro_txt}\n")
        file_out.write(f"{time_txt}\n")


def main():
    process_phone_data_file(FILE_PATH_PHONES_CONSISTENT,
                            file_write_mode='w',
                            is_consistent=True,
                            end_of_log_txt='\n')
    process_phone_data_file(FILE_PATH_PHONES_NOT_CONSISTENT,
                            file_write_mode='a',
                            is_consistent=False)


if __name__ == '__main__':
    main()
 