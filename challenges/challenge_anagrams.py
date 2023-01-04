def is_anagram(first_string, second_string):
    str1 = sort_str(first_string.lower())
    str2 = sort_str(second_string.lower())

    if len(first_string) != len(second_string):
        return str1, str2, False

    if not first_string or not second_string:
        return str1, str2, False

    return str1, str2, str1 == str2


def sort_str(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = string[:mid]
    right = string[mid:]

    left = sort_str(left)
    right = sort_str(right)

    return merge(left, right)


def merge(left, right):
    result = ""
    while left and right:
        if left[0] < right[0]:
            result += left[0]
            left = left[1:]
        else:
            result += right[0]
            right = right[1:]

    result += left
    result += right

    return result
