Приклад результатів:

Для масиву розміру 5000:

Сортування злиттям: 0.011609 секунд

Сортування вставками: 0.503248 секунд

Timsort: 0.000000 секунд

Для масиву розміру 20000:

Сортування злиттям: 0.054074 секунд

Сортування вставками: 8.002434 секунд

Timsort: 0.001522 секунд


Висновки:

Timsort — найшвидший і найефективніший алгоритм серед трьох. Він ідеально підходить для великих наборів даних, оскільки поєднує найкращі властивості сортування злиттям і вставками.
Сортування злиттям — теж показало хорошу продуктивність і підходить для великих масивів, хоча і трохи поступається Timsort за швидкістю.
Сортування вставками — працює повільно на великих масивах, тому підходить тільки для малих наборів даних. На великих масивах його швидкодія різко падає.

Ці результати підтверджують, що вбудовані алгоритми Python, такі як Timsort, забезпечують найкращу продуктивність для більшості практичних випадків, і тому девелопери рідко реалізують свої власні алгоритми сортування.
