from collections import Counter


def sw_has_substring_anagram(s: str, anagram: str) -> bool:
    k = len(anagram)

    if k == 0:
        return True

    if k > len(s):
        return False

    anagram_counter = Counter(anagram)
    window_counter = Counter(s[:k])

    if window_counter == anagram_counter:
        return True

    for i in range(k, len(s)):
        left_char = s[i - k]
        right_char = s[i]

        window_counter[left_char] -= 1
        if window_counter[left_char] == 0:
            del window_counter[left_char]

        window_counter[right_char] += 1

        if window_counter == anagram_counter:
            return True

    return False


def main():
    str_ = 'thecambridgehistoryofwarfare'
    sub_str = 'frwa'

    rv = sw_has_substring_anagram(str_, sub_str)
    expected = True
    print(f"Result: {rv}")
    assert rv == expected


if __name__ == '__main__':
    main()
