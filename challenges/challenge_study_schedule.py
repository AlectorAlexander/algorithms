def study_schedule(permanence_period, target_time):
    if not confer_values(permanence_period, target_time):
        return None
    count = 0
    for first_period, second_period in permanence_period:
        if first_period is not None and second_period is not None:
            if first_period <= target_time and second_period >= target_time:
                count += 1
    return count


def confer_values(permanence_period, target_time):
    if not isinstance(target_time, int) or not all(
        isinstance(item, tuple) for item in permanence_period
    ):
        return False
    for first_period, second_period in permanence_period:
        if not all(isinstance(x, int) for x in (first_period, second_period)):
            return False
    return True
