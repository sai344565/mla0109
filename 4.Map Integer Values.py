from itertools import permutations
def get_numeric_value(word, char_to_digit):
    return int(''.join([char_to_digit[char] for char in word]))
def is_valid_mapping(arr, s, mapping):
    char_to_digit = dict(zip(set(''.join(arr + [s])), mapping))
    sum_arr = sum([get_numeric_value(word, char_to_digit) for word in arr])
    value_s = get_numeric_value(s, char_to_digit)
    return sum_arr == value_s
def find_mapping(arr, s):
    unique_chars = set(''.join(arr + [s]))
    for mapping in permutations('0123456789', len(unique_chars)):
        if is_valid_mapping(arr, s, mapping):
            return True
    return False
arr = ["SEND", "MORE"]
s = "MONEY"
result = find_mapping(arr, s)
if result:
    print("Yes, it is possible to map integers to characters.")
else:
    print("No, it is not possible to map integers to characters.")
