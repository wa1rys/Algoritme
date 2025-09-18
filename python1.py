создание списка на Python
a_dict = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}




создание масива на Python
# Создание словаря
a_dict = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}

# Организация стека для работы со словарем
stack = []

# Добавление элементов в стек (ключи словаря)
stack.append("Alice")     # ['Alice']
stack.append("Bob")       # ['Alice', 'Bob']
stack.append("Charlie")   # ['Alice', 'Bob', 'Charlie']

# Получение значения из словаря через стек
top_key = stack.pop()     # возвращает 'Charlie'
top_value = a_dict[top_key]

print(f"Верхний элемент стека: {top_key}")
print(f"Значение из словаря: {top_value}")
print(f"Размер стека после pop: {len(stack)}")

# Дополнительные операции
stack.append("David")     # Добавляем новый ключ
a_dict["David"] = 28      # Добавляем значение в словарь

print(f"Обновленный словарь: {a_dict}")
print(f"Текущий стек: {stack}")

