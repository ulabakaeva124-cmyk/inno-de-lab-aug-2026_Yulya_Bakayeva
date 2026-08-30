MAX_RENTAL_BATCH_LIMIT = 150.0
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8
DEFAULT_RETURN_INDEX_BASE = 10.0
def calculate_rental_batch(quantity : int, rental_rate : float, discount : float=0.0) -> tuple[float, bool]:
    """
    Функция рассчитывает стоимость партии дисков с учетом жанровой скидки

    Args:
        quantity(int): Количество
        rental_rate(float): Цена

    Return:
        float: Кортеж с суммой и булевым значением о превышении максимальной суммы
    """

    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

test_batches = [
    (1, "Academy Dinosaur", 30, 2.99, 0.0),
    (2, "Affair Prejudice", 40, 4.99, 0.1),
    (3, "Agent Truman", 10, 1.99, 0.0),
    (4, "African Egg", 50, 3.50, 0.2)
]

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")
for index, title, quantity, rental_rate, discount in test_batches:
    final_sum, limit_exceeded = calculate_rental_batch(quantity, rental_rate, discount)
    print(f'Партия {index}({title}):  Сумма: {final_sum}$. Превышение лимита: {limit_exceeded}')