import random
import time
import functools

# Декоратор для вимірювання часу виконання функцій
def time_measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time, result
    return wrapper

# Алгоритм сортування злиттям
@time_measure
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
@time_measure
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Вбудований Timsort через функцію sorted()
@time_measure
def timsort(arr):
    return sorted(arr)

# Генерація випадкових масивів
def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Порівняння часу виконання алгоритмів
def compare_algorithms():
    sizes = [5000, 20000]  # Розміри масивів для тестування
    results = {}
    print(f"\nВідбувається сортування 5000 та 20000 елементів в масиві, зачекайте 2-3 хвилини")

    for size in sizes:
        arr = generate_random_array(size)

        # Копії масивів для уникнення зміни оригіналу
        arr_merge = arr.copy()
        arr_insertion = arr.copy()
        arr_timsort = arr.copy()

        # Вимірювання часу для кожного алгоритму
        merge_time, _ = merge_sort(arr_merge)
        insertion_time, _ = insertion_sort(arr_insertion)
        timsort_time, _ = timsort(arr_timsort)

        # Збереження результатів для виводу
        results[size] = {
            'merge_sort': merge_time,
            'insertion_sort': insertion_time,
            'timsort': timsort_time
        }

    # Виведення результатів
    print("\nРезультати порівняння:")
    for size, times in results.items():
        print(f"\nДля масиву розміру {size}:")
        print(f"  Сортування злиттям: {times['merge_sort']:.6f} секунд")
        print(f"  Сортування вставками: {times['insertion_sort']:.6f} секунд")
        print(f"  Timsort: {times['timsort']:.6f} секунд")

# Виконання порівняння
if __name__ == "__main__":
    compare_algorithms()
