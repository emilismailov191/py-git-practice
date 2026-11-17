def calculate_discount(price: float, percent: float) -> float:
    """Возвращает размер скидки в денежных единицах."""
    return price * percent / 10


if __name__ == "__main__":
    print(calculate_discount(1000, 10))
