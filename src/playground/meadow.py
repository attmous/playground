def rolling_average(values: list[float], window: int) -> list[float]:
    if window <= 0:
        raise ValueError("window must be positive")

    averages: list[float] = []
    total = 0.0

    for index, value in enumerate(values):
        total += value
        if index >= window:
            total -= values[index - window]

        count = min(index + 1, window)
        averages.append(total / count)

    return averages
