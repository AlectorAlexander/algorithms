def find_duplicate(nums):
    counts = create_count(nums)

    if not counts:
        return False

    for num, count in counts.items():
        if count > 1:
            return num

    return False


def create_count(nums):
    counts = {}
    for num in nums:
        if isinstance(num, str) or num < 0:
            return False
        elif num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    return counts
