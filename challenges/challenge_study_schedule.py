def study_schedule(permanence_period, target_time):
    count_hour = 0
    if not target_time:
        return None

    for i, j in permanence_period:
        if not i or not j or type(i) == str or type(j) == str:
            return None
        elif target_time >= i and target_time <= j:
            count_hour += 1

    return count_hour
