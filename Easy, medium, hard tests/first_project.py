def avg(*list_numbers:float) -> float:
    total = 0
    for num in list_numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise TypeError("Wrong type of data. We need only numbers")
    return total / len(list_numbers)

