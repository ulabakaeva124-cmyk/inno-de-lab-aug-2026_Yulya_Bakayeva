import time
from Task_1 import PERFORMANCE_LOG_PREFIX, TIME_DECIMALS
attempt = 0

def  performance_logger(func):
    """
        Декоратор для замера времени выполнения

        Args:
            func (Callable[..., Any]): Целевая функция, которую необходимо обернуть
        Return:
            Callable[..., Any]: Результат выполнения функции
    """
    def wrapper(*args, **kwargs):
        """
            Функция рассчитывает разницу между временем запуска и завершением расчетов основной функции

            Args:
                (*args, **kwargs): Любые аргументы, нужные для выполнения функции
            Return:
                Callable[..., Any]: Результат выполнения функции
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        print(f'{PERFORMANCE_LOG_PREFIX} Функция "{func.__name__}" выполнена за {time_taken:.{TIME_DECIMALS}f} сек.')
        return result
    return wrapper

@performance_logger
def get_sorted_data(data : list[dict[str, str | float]]):
    """
        Функция распаковывает список словарей и сортирует его

        Args:
            data(list[dict[str, str | float]]): Список данных

        Return:
            list: Отсортированный список
                """
    sorted_data = sorted(data, key=lambda item: item['total_sales'], reverse=True)
    return sorted_data

datasets = [
    [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55}
    ],
    [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00}
    ],
    [
        {"category": "Drama", "total_sales": 500.00}
    ]
]

print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
for data_set in datasets:
    attempt += 1
    sorted_data = get_sorted_data(data_set)
    print(f"--- ТЕСТ {attempt} ---")
    print('Топ категорий по выручке:')
    for index, item in enumerate(sorted_data, start=1):
        print(f"{index}. {item['category']}: {item['total_sales']}")