def calculate_average(numbers):
    total_sum = 0
    count = 0

    # Find average of two numbers
    for num in numbers:
        total_sum += num
        count += 1

    avg = total_sum / count

    return avg