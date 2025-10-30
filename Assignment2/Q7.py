def process_numbers(numbers):
    unique_numbers = {x for x in numbers}
    frequency = {x: numbers.count(x) for x in unique_numbers}
    sorted_by_freq = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
    print("Unique Numbers:", unique_numbers)
    print("Frequency Dictionary:", frequency)
    print("Sorted by Frequency (Descending):", sorted_by_freq)

numbers = [4, 2, 7, 4, 2, 4, 9, 7, 9, 9]
process_numbers(numbers)
