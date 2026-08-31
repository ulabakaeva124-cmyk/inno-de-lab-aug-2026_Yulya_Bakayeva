from Task_1 import DEFAULT_RETURN_INDEX_BASE
from typing import Any
def  calculate_overdue_fine(movie : str, days_overdue: Any, fine_rate: Any) -> tuple[float, float] | None:
    """
        Функция обрабатывает ошибки: TypeError, ValueError, ZeroDivisionError

        Args:
            movie(Any): Название фильма
            days_overdue(Any): Количество дней
            fine_rate(Any): Сумма за день
        Returns:
            tuple[float, float] | None: Преобразованные данные
    """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        print(f'Фильм: "{movie}" | Итоговый штраф: {total_fine}$ | Индекс: {return_index}')
        return total_fine, return_index

    except TypeError as e:
        print(f'[ОШИБКА ТИПА] Некорректный тип данных для {movie}: {e}')
    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для {movie}: {e}")
    except ZeroDivisionError as e:
        print(f'[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для {movie}: {e}')
    finally:
        print(' --- Проверка транзакции возврата завершена ---')
    return None
datasets = [
    ['Matrix', 5, 1.5],
    ['Inception', 'пять', 2.0],
    ['Avatar', 0, 2.5],
    ['Interstellar', [3,], 3.0]
]

print('=== ПРОВЕРКА ВОЗВРАТОВ ===')
for dataset in datasets:
    calculate_overdue_fine(*dataset)
