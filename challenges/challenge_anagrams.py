def bubble_sort(numbers):
    n = len(numbers)
    for ordered_elements in range(n - 1):
        for item in range(0, n - 1 - ordered_elements):
            if numbers[item] > numbers[item + 1]:
                current_element = numbers[item]
                numbers[item] = numbers[item + 1]
                numbers[item + 1] = current_element
    return "".join(numbers)


def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    f = bubble_sort(list(first_string.lower()))
    s = bubble_sort(list(second_string.lower()))
    c = f == s

    return (f, s, c)
