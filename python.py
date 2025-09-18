# Создание кортежа (неизменяемая последовательность)
a_tuple = ('x', 'y', 'z')

# Организация очереди с помощью collections.deque
from collections import deque

# Создание очереди
queue = deque()

# Добавление в очередь
queue.append(10)    # [10]
queue.append(20)    # [10, 20]
queue.append(30)    # [10, 20, 30]
queue.append(40)    # [10, 20, 30, 40]

# Добавление в начало очереди
queue.appendleft(5)  # [5, 10, 20, 30, 40]

# Удаление из очереди (первый элемент)
front = queue.popleft()  # возвращает 5, queue = [10, 20, 30, 40]

print(f"Первый элемент очереди: {front}")
print(f"Размер очереди после popleft: {len(queue)}")
print(f"Следующий элемент в очереди: {queue[0]}")

# Вывод элементов кортежа
print(f"\nЭлементы кортежа: {a_tuple}")

# Дополнительные операции с очередью
print(f"Очередь пустая? {len(queue) == 0}")
print(f"Текущий размер очереди: {len(queue)}")

# Преобразование очереди в список
queue_list = list(queue)
print(f"Очередь как список: {queue_list}")

# Очистка очереди
queue.clear()
print(f"Очередь после очистки: {list(queue)}")
print(f"Очередь пустая теперь? {len(queue) == 0}")