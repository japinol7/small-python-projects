def print_test_result(result, expected):
    failed = result != expected
    print(f"Res: {'FAILED' if failed else 'OK'} : "
          f"\n\t> {result}"
          f"\n\t> {expected}")
    return 1 if failed else 0
